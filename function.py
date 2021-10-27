import random
import time
from env import userParameters as Param, musicPlayerEvent as playEv

def randomChoose(currentIdx):
    ''' 
    Choose next song randomly
    
    Parameters
    ----------
    currentIdx : current idx from currentMusicIdx
    
    Returns
    ----------
    fileIdx : store to currentMusicIdx
    '''
    fileIdx = random.randrange(Param.totalMusicFileNum)
    while fileIdx == currentIdx:
        fileIdx = random.randrange(Param.totalMusicFileNum)
    return fileIdx

def sortedChoose(currentIdx):
    ''' 
    Choose next song sequentially
    
    Parameters
    ----------
    currentIdx : current idx from currentMusicIdx
    
    Returns
    ----------
    fileIdx : store to currentMusicIdx
    '''
    fileIdx = currentIdx + 1
    if fileIdx == Param.totalMusicFileNum:
        fileIdx = 0
    return fileIdx

def timeConvert(time):
    ''' 
    Convert time to minutes:seconds string
    
    Parameters
    ----------
    time : seconds
    
    Returns
    ----------
    timeString : (minutes : second) string
    '''
    time = int(time)
    timeMinute = int(time/60)
    timeSecond = int(time%60)
    return '{min:02d}:{sec:02d}'.format(min=timeMinute,sec=timeSecond)

def waitPlayerThread(thread):
    while thread.state != playEv.WAIT:
        time.sleep(0.02)