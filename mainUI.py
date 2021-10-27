# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hSlider_time = QtWidgets.QSlider(self.centralwidget)
        self.hSlider_time.setGeometry(QtCore.QRect(30, 90, 331, 22))
        self.hSlider_time.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider_time.setObjectName("hSlider_time")
        self.pushBtn_nextSong = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_nextSong.setGeometry(QtCore.QRect(180, 112, 60, 23))
        self.pushBtn_nextSong.setObjectName("pushBtn_nextSong")
        self.pushBtn_musicControl = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_musicControl.setGeometry(QtCore.QRect(110, 112, 60, 23))
        self.pushBtn_musicControl.setObjectName("pushBtn_musicControl")
        self.pushBtn_previousSong = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_previousSong.setGeometry(QtCore.QRect(40, 112, 60, 23))
        self.pushBtn_previousSong.setObjectName("pushBtn_previousSong")
        self.label_currentTime = QtWidgets.QLabel(self.centralwidget)
        self.label_currentTime.setGeometry(QtCore.QRect(248, 114, 51, 20))
        self.label_currentTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_currentTime.setObjectName("label_currentTime")
        self.label_totalTime = QtWidgets.QLabel(self.centralwidget)
        self.label_totalTime.setGeometry(QtCore.QRect(300, 114, 80, 20))
        self.label_totalTime.setObjectName("label_totalTime")
        self.label_songName = QtWidgets.QLabel(self.centralwidget)
        self.label_songName.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.label_songName.setObjectName("label_songName")
        self.label_singer = QtWidgets.QLabel(self.centralwidget)
        self.label_singer.setGeometry(QtCore.QRect(30, 50, 291, 30))
        self.label_singer.setObjectName("label_singer")
        self.vSlider_volume = QtWidgets.QSlider(self.centralwidget)
        self.vSlider_volume.setGeometry(QtCore.QRect(340, 20, 22, 61))
        self.vSlider_volume.setOrientation(QtCore.Qt.Vertical)
        self.vSlider_volume.setObjectName("vSlider_volume")
        self.listWidget_playlist = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_playlist.setGeometry(QtCore.QRect(24, 180, 340, 450))
        self.listWidget_playlist.setObjectName("listWidget_playlist")
        self.pushBtn_playType = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_playType.setGeometry(QtCore.QRect(140, 140, 60, 23))
        self.pushBtn_playType.setObjectName("pushBtn_playType")
        self.checkBox_downloadMode = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_downloadMode.setGeometry(QtCore.QRect(30, 140, 100, 23))
        self.checkBox_downloadMode.setObjectName("checkBox_downloadMode")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushBtn_nextSong.setText(_translate("MainWindow", "Next"))
        self.pushBtn_musicControl.setText(_translate("MainWindow", "Play"))
        self.pushBtn_previousSong.setText(_translate("MainWindow", "Previous"))
        self.label_currentTime.setText(_translate("MainWindow", "Time"))
        self.label_totalTime.setText(_translate("MainWindow", "/time"))
        self.label_songName.setText(_translate("MainWindow", "Song"))
        self.label_singer.setText(_translate("MainWindow", "Singer"))
        self.pushBtn_playType.setText(_translate("MainWindow", "Sorted"))
        self.checkBox_downloadMode.setText(_translate("MainWindow", "Download Mode"))
