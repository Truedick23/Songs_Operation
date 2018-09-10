import os
import mutagen


def songTitleFormat(oriTitle):
    if oriTitle[-1] == ')':
        i = oriTitle.find('(')
        j = oriTitle.find(')')
        flag1 = oriTitle.find('Remastered')
        flag2 = oriTitle.find('Version')
        flag3 = oriTitle.find('Remaster')
        if flag1 != -1 or flag2 != -1 or flag3 != -1:
            return oriTitle[0:i-1]
        return oriTitle
    return oriTitle


def acquireInfo(src):
    mu = mutagen.File(src)
    trackNum = mu.get("TRCK").text[0]  # 得到音轨号
    performer = mu.get("TPE1").text[0]  # 得到表演者
    songName = songTitleFormat(mu.get("TIT2").text[0])  # 得到歌曲名称
    albumName = mu.get("TALB").text[0]
    if int(trackNum) < 10:
        trackNum = '0' + trackNum
    # print(trackNum, performer, songName, albumName)
    return trackNum, performer, songName, albumName


def main():
    dir = "E:/CloudMusic/Television/Marquee Moon"  # 需要处理的歌曲目录，请根据实际情况替换
    os.chdir(dir)
    songsList = os.listdir(dir)
    for song in songsList:
        srcFile = dir + "/" + song
        trackNum, performer, songName, _ = acquireInfo(srcFile)
        newName = trackNum + ' - ' + songName + ' - ' + performer + '.mp3'
        print(newName)
        os.rename(song, newName)

# main()