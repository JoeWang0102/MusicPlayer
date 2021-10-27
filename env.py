from typing import Dict
import os
#-----USER PARAMETER-----#
class userParameters:
    # path = os.getcwd()
    appPath = os.getcwd()
    musicPath = os.path.join(os.path.abspath(os.path.join(appPath,'..')),'Music')
    playing = False
    currentMusicName = ''
    totalMusicFileNum = 0
    offsetTime = 0
    totalTime = 0
    currentTime = 0
    downloadMode = True
    playType = 8
    volume = 0.5
    autoPlay = True
#------------------------#

class musicPlayerEvent(Dict):
    WAIT = 1
    WORK = 2
    KILL = 3
    PLAY = 4
    PAUSE = 5
    STOP = 6
    LOAD = 7
    RANDOM = 8
    SORTED = 9
    SETPLAYTIME = 10
    SETVOLUME = 11

class uiHandleEvent(Dict):
    BTN = 1
    LABEL = 2
    PLAYTIME = 3
    VOLUME = 4
