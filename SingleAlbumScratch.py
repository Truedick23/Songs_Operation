import os
import mutagen
dir = "E:/CloudMusic/Television/Marquee Moon" #需要处理的歌曲目录，请根据实际情况替换
os.chdir(dir)
songsList = os.listdir(dir)
for song in songsList:
    srcFile = dir + "/" + song
    mu = mutagen.File(srcFile)
    trackNum = mu.get("TRCK").text[0]          #得到音轨号
    performer = mu.get("TPE1").text[0]         #得到表演者
    songName = mu.get("TIT2").text[0]          #得到歌曲名称
    if(int(trackNum) < 10):
        trackNum = '0' + trackNum
    newName = trackNum + ' - ' + songName + ' - ' + performer + '.mp3'
    print(newName)
    os.rename(song, newName)
