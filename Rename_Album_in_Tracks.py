import os
import mutagen
import BasicSongsOperator as bso
dir = "E:/CloudMusic/"
performerList = os.listdir(dir)
for performer in performerList:
    performerDir = dir + performer + '/'
    if performerDir == 'E:/CloudMusic/musiclibrary.db/':
        continue


    albumList = os.listdir(performerDir)
    for album in albumList:
        albumDir = performerDir + album + '/'
        #print(albumDir)
        try:
            os.chdir(albumDir)
            songsList = os.listdir(albumDir)
            for song in songsList:
                srcFile = albumDir + song
                try:
                    if song[-1] == 'c':
                        trackNum, performer, songName, _ = bso.acquireInfo(srcFile)
                        newName = trackNum + ' - ' + songName + ' - ' + performer + '.flac'
                        if song != newName:
                            os.rename(song, newName)
                            print(newName, song)
                    elif song[-1] == '3':
                        trackNum, performer, songName, _ = bso.acquireFlacInfo(srcFile)
                        newName = trackNum + ' - ' + songName + ' - ' + performer + '.mp3'
                        if song != newName:
                            os.rename(song, newName)
                            print(newName, song)
                except:
                    continue
        except:
            continue
