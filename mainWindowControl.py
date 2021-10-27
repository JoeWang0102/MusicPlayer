from PyQt5 import QtCore, QtGui, QtWidgets
from mainUI import Ui_MainWindow
import os
from env import userParameters as Param, musicPlayerEvent as playEv, uiHandleEvent as uiEv
import threadControl
import random
import time
import function as fun
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.5)
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.currentMusicIdx = 0
        self.playList = []
        self.uiInit()
        self.eventDefine()
        self.threadDefine()

    def threadDefine(self):
        self.musicPlayer_T = threadControl.musicPlayer()
        self.musicPlayer_T.signal.connect(self.musicPlayerHandle)
        self.uiDisplay_T = threadControl.uiDisplay()
        self.uiDisplay_T.signal.connect(self.uiDisplayHandle)
        self.keyboradListener_T = threadControl.keyboardListener()
        self.keyboradListener_T.next.connect(self.nextMusic)
        self.keyboradListener_T.previous.connect(self.previousMusic)
        self.keyboradListener_T.musicControl.connect(self.musicControl)
        self.keyboradListener_T.downloadControl.connect(self.downloadControl)

    def eventDefine(self):
        self.ui.listWidget_playlist.itemClicked.connect(self.setMusic)
        self.ui.pushBtn_musicControl.clicked.connect(self.musicControl)
        self.ui.pushBtn_playType.clicked.connect(self.playType)
        self.ui.hSlider_time.sliderMoved.connect(self.playTimeSet)
        # self.ui.hSlider_time.
        self.ui.vSlider_volume.sliderMoved.connect(self.volumeSet)
        self.ui.pushBtn_nextSong.clicked.connect(self.nextMusic)
        self.ui.pushBtn_previousSong.clicked.connect(self.previousMusic)
        self.ui.checkBox_downloadMode.clicked.connect(self.downloadMode)

    def uiInit(self):
        os.chdir(Param.musicPath)
        for item in os.listdir(Param.musicPath):
            if os.path.isfile(item) and item[-3:]=='mp3':
                self.ui.listWidget_playlist.insertItem(0,item)
        self.ui.listWidget_playlist.setCurrentRow(self.currentMusicIdx)
        Param.totalMusicFileNum = self.ui.listWidget_playlist.count()
        if Param.totalMusicFileNum != 0:
            Param.currentMusicName = self.ui.listWidget_playlist.currentItem().text()
        self.setPlayList()
        self.ui.vSlider_volume.setSliderPosition(Param.volume*99)
        self.ui.checkBox_downloadMode.setChecked(Param.downloadMode)


    def setMusic(self,musicFile):
        self.setPlayList()
        self.currentMusicIdx = self.playList.index(self.ui.listWidget_playlist.currentRow())
        Param.currentMusicName = musicFile.text()
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.LOAD

    def musicControl(self):
        fun.waitPlayerThread(self.musicPlayer_T)
        if Param.playing:
            self.musicPlayer_T.state = playEv.PAUSE
        else:
            self.musicPlayer_T.state = playEv.PLAY

    def playType(self):
        if Param.playType == playEv.SORTED:
            Param.playType = playEv.RANDOM
        elif Param.playType == playEv.RANDOM:
            Param.playType = playEv.SORTED
        self.setPlayList()

    def setPlayList(self):
        self.playList = range(0,Param.totalMusicFileNum)
        if Param.playType == playEv.SORTED:
            self.playList = list(self.playList)
            self.currentMusicIdx = self.playList.index(self.ui.listWidget_playlist.currentRow())
        elif Param.playType == playEv.RANDOM:
            self.playList = random.sample(self.playList,Param.totalMusicFileNum)
            idx = self.playList.index(self.ui.listWidget_playlist.currentRow())
            self.playList = [self.playList[idx]]+self.playList[:idx]+self.playList[idx+1:]
    
    def musicPlayerHandle(self,cmd):
        if cmd == 'playFinish':
            self.nextMusic()

    def uiDisplayHandle(self,signal):
        if signal == uiEv.BTN:
            # About Play/Pause button
            self.ui.pushBtn_musicControl.setEnabled(Param.totalMusicFileNum)
            if Param.playing:
                self.ui.pushBtn_musicControl.setText('Pause')
            else:
                self.ui.pushBtn_musicControl.setText('Play')
            # About playting type button
            if Param.playType == playEv.SORTED:
                self.ui.pushBtn_playType.setText('Sorted')
            elif Param.playType == playEv.RANDOM:
                self.ui.pushBtn_playType.setText('Random')

        if signal == uiEv.LABEL:
            self.ui.label_songName.setText(Param.currentMusicName)
            self.ui.label_currentTime.setText(fun.timeConvert(Param.offsetTime+Param.currentTime))
            self.ui.label_totalTime.setText(' / '+fun.timeConvert(Param.totalTime))
        
        if signal == uiEv.PLAYTIME:
            if Param.totalTime !=0 :
                self.ui.hSlider_time.setValue((Param.offsetTime+Param.currentTime)/Param.totalTime*99)
    
    def nextMusic(self):
        self.currentMusicIdx += 1
        if self.currentMusicIdx == Param.totalMusicFileNum:
            self.currentMusicIdx = 0
        self.ui.listWidget_playlist.setCurrentRow(self.playList[self.currentMusicIdx])
        Param.currentMusicName = self.ui.listWidget_playlist.currentItem().text()
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.LOAD
        fun.waitPlayerThread(self.musicPlayer_T)
        if Param.autoPlay:
            self.musicPlayer_T.state = playEv.PLAY

    def previousMusic(self):
        self.currentMusicIdx -= 1
        if self.currentMusicIdx < 0:
            self.currentMusicIdx = Param.totalMusicFileNum-1
        self.ui.listWidget_playlist.setCurrentRow(self.playList[self.currentMusicIdx])
        Param.currentMusicName = self.ui.listWidget_playlist.currentItem().text()
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.LOAD
    
    def downloadControl(self):
        if Param.downloadMode:
            self.download_T = threadControl.downloadURL()
            self.download_T.signal.connect(self.downloadHandle)
        else:
            print('Not download mode now')
        
    def downloadHandle(self,res):
        if res == 'False':
            pass
        else:
            self.ui.listWidget_playlist.insertItem(Param.totalMusicFileNum,res)
            Param.totalMusicFileNum += 1
            self.setPlayList()

    def downloadMode(self,type):
        Param.downloadMode = type

    def playTimeSet(self,pos):
        Param.currentTime = (pos/99)*Param.totalTime
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.SETPLAYTIME

    def volumeSet(self,pos):
        Param.volume = (pos/99)
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.SETVOLUME

    def closeEvent(self,ev):
        fun.waitPlayerThread(self.musicPlayer_T)
        self.musicPlayer_T.state = playEv.KILL
        self.keyboradListener_T.state = False
        ev.accept()
