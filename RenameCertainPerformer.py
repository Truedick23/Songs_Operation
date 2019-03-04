import os
import BasicSongsOperator as bso
import sys

def rename_performers(dir, performerList):
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

if __name__ == '__main__':
    dir = "E:/CloudMusic/"
    performerList = ['Victor Wooten', 'Kraftwerk', 'Radiohead', 'The Yardbirds', 'Marcus Miller', 'Jaco Pastorius']
    rename_performers(dir, performerList)

