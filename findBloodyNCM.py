import os
dir = "E:/CloudMusic/"
performerList = os.listdir(dir)
ncmDirs = list()
for performer in performerList:
    performerDir = dir + performer + '/'
    try:
        albumList = os.listdir(performerDir)
        for album in albumList:
            albumDir = performerDir + album + '/'
            songsList = os.listdir(albumDir)
            for song in songsList:
                if os.path.splitext(song)[-1] == '.ncm':
                    ncmDirs.append(albumDir)
                    break
    except:
        pass

for ncmDir in ncmDirs:
    print(ncmDir)
