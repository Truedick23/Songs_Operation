import os
import BasicSongsOperator as bso
dir = "E:/CloudMusic/"
performerList = ['The Killers', 'Queen', 'The Flying Burrito Brothers', 'Scissor Sisters', 'New York Dolls', 'Elton John',
                 'Björk', 'Albert King', 'Sonny Boy Williamson', "Flamin' Groovies", 'Moby Grape', 'X', 'The Smiths',
                 'Patti Smith', 'Sleater-Kinney', 'Bronski Beat', 'Tori Amos', 'Yazoo', 'Erasure', 'Danse Society',
                 'Danse Society', 'New Order', 'The Sound']
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
                if newName != song:
                    os.rename(song, newName)
                    print(newName, song)
            except:
                continue
