import os
import mutagen
import BasicSongsOperator as bso
dir = "E:/CloudMusic/"
performerList = os.listdir(dir)
for performer in performerList:
    performerDir = dir + performer + '/'
    albumList = os.listdir(performerDir)
    for album in albumList:
        albumDir = performerDir + album + '/'
        print(albumDir)
        os.chdir(albumDir)
        songsList = os.listdir(albumDir)
        for song in songsList:
            srcFile = albumDir + song
            try:
                trackNum, performer, songName, _ = bso.acquireInfo(srcFile)
                newName = trackNum + ' - ' + songName + ' - ' + performer + '.mp3'
                print(newName)
                os.rename(song, newName)
            except:
                continue
