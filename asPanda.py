import pandas as pd
import os
import BasicSongsOperator as bso
dir = "E:/CloudMusic/"
html = "D:/CloudInfo.html"

trackList = list()
performerList = list()
songNamesList = list()
data = {'Track': trackList, 'Song Title': songNamesList, 'Performer': performerList}
pdList = pd.DataFrame(data=data)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

performerPathsList = os.listdir(dir)
for performerPath in performerPathsList:
    performerDir = dir + performerPath + '/'
    albumPathsList = os.listdir(performerDir)
    for albumPath in albumPathsList:
        albumDir = performerDir + albumPath + '/'
        os.chdir(albumDir)
        songsPathsList = os.listdir(albumDir)
        trackList = list()
        performerList = list()
        songNamesList = list()
        albumNamesList = list()
        for songPath in songsPathsList:
            srcFile = albumDir + songPath
            try:
                trackNum, performer, songName, albumName = bso.acquireInfo(srcFile)
                trackList.append(trackNum)
                performerList.append(performer)
                songNamesList.append(songName)
                albumNamesList.append(albumName)
            except:
                continue
        temp_data = {'Track': trackList, 'Song Title': songNamesList, 'Performer': performerList, 'Album': albumNamesList}
        temp_pdList = pd.DataFrame(data=temp_data)
        temp_pdList = temp_pdList.sort_values(by="Track")
        temp_pdList = temp_pdList.reset_index(drop=True)
        pdList = pd.concat([pdList, temp_pdList], sort=False)
        pdList = pdList.reset_index(drop=True)

pd_track = pdList.Track
pd_SongTitle = pdList.get('Song Title')
pd_Performer = pdList.Performer

pdList = pdList.drop('Song Title', axis=1)
pdList.insert(0, 'Song Title', pd_SongTitle)
pdList = pdList.drop('Track', axis=1)
pdList.insert(0, 'Track', pd_track)
# print(pdList[pdList['Performer'].isin(['Television'])])
# print(pdList.groupby('Album').get_group('Marquee Moon'))
txt = pdList.to_html(justify='center')
with open('D:/PycharmProjects/Songs_Operation/files/CloudMusic.html', 'w', encoding='utf-8') as f:
    f.write(txt)
f.close()
pdList.to_csv('D:/PycharmProjects/Songs_Operation/files/CloudMusic.csv', encoding='utf-8')
# pdList.to_hdf('D:/PycharmProjects/Songs_Operation/files/CloudMusic.hdf', 'w')


