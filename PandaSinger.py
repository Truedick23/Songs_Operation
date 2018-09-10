import os
import mutagen
import pandas as pd
import numpy as np
import BasicSongsOperator as bso
performerDir = "E:/CloudMusic/Iron Maiden"
trackList = list()
performerList = list()
songNamesList = list()
albumNamesList = list()
data = {'Track': trackList, 'Song Title': songNamesList, 'Performer': performerList, 'Album': albumNamesList}
pdList = pd.DataFrame(data=data)
pd.set_option('display.max_columns',None)
print(pdList)

albumPathsList = os.listdir(performerDir)
for albumPath in albumPathsList:
    albumDir = performerDir + '/' + albumPath
    os.chdir(albumDir)
    songsPathsList = os.listdir(albumDir)
    trackList = list()
    performerList = list()
    songNamesList = list()
    albumNamesList = list()
    for songPath in songsPathsList:
        srcFile = albumDir + '/' + songPath
        mu = mutagen.File(srcFile)
        if mu is None or mu.get("TRCK") is None:
            continue
        trackNum, performer, songName, albumName = bso.acquireInfo(srcFile)
        trackList.append(trackNum)
        performerList.append(performer)
        songNamesList.append(songName)
        albumNamesList.append(albumName)
    temp_data = {'Track': trackList, 'Song Title': songNamesList, 'Performer': performerList, 'Album': albumNamesList}
    temp_pdList = pd.DataFrame(data=temp_data)
    temp_pdList = temp_pdList.sort_values(by="Track")
    temp_pdList = temp_pdList.reset_index(drop=True)
    # print(temp_pdList)
    pdList = pd.concat([pdList, temp_pdList])
    pdList = pdList.reset_index(drop=True)

# pdList['Track'] = pdList['Track'].astype('int64')
pd_track = pdList.Track
pd_SongTitle = pdList.get('Song Title')
pd_Performer = pdList.Performer

pdList = pdList.drop('Song Title', axis=1)
pdList.insert(0, 'Song Title', pd_SongTitle)
pdList = pdList.drop('Track', axis=1)
pdList.insert(0, 'Track', pd_track)
print(pdList)

