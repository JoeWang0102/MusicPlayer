from PyQt5.QtCore import QThread, pyqtSignal
import pygame.mixer as mixer
from pygame import USEREVENT, event, init as pygame_init
from env import userParameters as Param, musicPlayerEvent as play, uiHandleEvent as ui
from downloader import download
import os
from pynput import keyboard
import time
import pyperclip

class musicPlayer(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super(musicPlayer,self).__init__()
        mixer.init()
        pygame_init()
        mixer.music.set_volume(Param.volume)
        self.MUSIC_END = USEREVENT+1
        mixer.music.set_endevent(self.MUSIC_END)
        self.state = play.LOAD
        self.start()
    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.msleep(10)
            if self.state == play.WAIT:
                if self.get_busy():
                    Param.offsetTime = mixer.music.get_pos()/1000
                    Param.playing = True
                else:
                    Param.playing = False
                for ev in event.get():
                    if ev.type == self.MUSIC_END:
                        self.signal.emit('playFinish')
            if self.state == play.PLAY:
                if mixer.music.get_pos() == -1:
                    mixer.music.play(0)
                else:
                    mixer.music.unpause()
                self.state = play.WAIT
            elif self.state == play.PAUSE:
                mixer.music.pause()
                self.state = play.WAIT
            elif self.state == play.STOP:
                mixer.music.stop()
                self.state = play.WAIT
            elif self.state == play.KILL:
                mixer.music.stop()
                self.msleep(50)
                break
            elif self.state == play.LOAD:
                mixer.music.stop()
                os.chdir(Param.musicPath)
                if Param.currentMusicName =='':
                    self.state - play.WAIT
                    continue
                for ev in event.get():
                    continue
                mixer.music.load(Param.currentMusicName)
                Param.totalTime = mixer.Sound(Param.currentMusicName).get_length()
                Param.currentTime = 0
                Param.offsetTime = 0
                self.state = play.WAIT
            elif self.state == play.SETPLAYTIME:
                mixer.music.play(0,Param.currentTime)
                for ev in event.get():
                    if ev.type == self.MUSIC_END:
                        pass
                self.state = play.WAIT
            elif self.state == play.SETVOLUME:
                mixer.music.set_volume(Param.volume)
                self.state = play.WAIT
    
    def get_busy(self):
        return mixer.music.get_busy()

class uiDisplay(QThread):
    signal = pyqtSignal(int)
    def __init__(self):
        super(uiDisplay,self).__init__()
        self.start()
    
    def __del__(self):
        self.wait()
    
    def run(self):
        while True:
            self.msleep(20)
            self.signal.emit(ui.BTN)
            self.signal.emit(ui.LABEL)
            self.signal.emit(ui.PLAYTIME)
                
class keyboardListener(QThread):
    next = pyqtSignal()
    previous = pyqtSignal()
    musicControl = pyqtSignal()
    downloadControl = pyqtSignal()
    def __init__(self):
        super(keyboardListener,self).__init__()
        self.state = True
        self.listener = keyboard.Listener(on_press = self.press)
        self.ctr = False
        self.timer = 0
        self.listener.start()
        self.start()
    
    def __del__(self):
        self.wait()

    def run(self):
        while self.state:
            self.msleep(20)
            if self.ctr:
                if time.time() - self.timer > 0.5:
                    self.ctr = False

    def press(self,key):
        if self.ctr:
            if key == keyboard.Key.page_up:
                self.next.emit()
            elif key == keyboard.Key.page_down:
                self.previous.emit()
            elif key == keyboard.Key.space:
                self.musicControl.emit()
            elif key == keyboard.Key.f1:
                self.downloadControl.emit()
        if key == keyboard.Key.ctrl_l:
            self.ctr = True
            self.timer = time.time()

class downloadURL(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super(downloadURL,self).__init__()
        originalPaste = pyperclip.paste()
        self.ctr = keyboard.Controller()
        with self.ctr.pressed(keyboard.Key.ctrl,'c'):
            time.sleep(0.01)
        self.url = pyperclip.paste()
        pyperclip.copy(originalPaste)
        self.start()
    
    def __del__(self):
        self.wait()
    
    def run(self):
        res = False
        if self.url.find('youtu') !=-1 :
            res = download(self.url)
        self.signal.emit(res)