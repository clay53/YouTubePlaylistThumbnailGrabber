import os

import urllib

import ytda

def getAllPlaylistVideoIds(_playlistId):
    results = []
    pageToken = None
    working = True
    while working:
        response = ytda.playlist_items_list_by_playlist_id(ytda.client,
            part='snippet,contentDetails',
            maxResults=50,
            pageToken=pageToken,
            playlistId=_playlistId
        )
        if 'nextPageToken' in response:
            pageToken = response.get('nextPageToken')
        else:
            working = False
        for video in response.get('items'):
            result = video.get('contentDetails').get('videoId')
            results.append(result)
    return results

id = raw_input("Enter Playlist Id")
print(id)
videoIds = getAllPlaylistVideoIds(id)
for i in range(0, len(videoIds)):
    videoId = videoIds[i]
    print(videoId + " " + str(i+1) + "/" + str(len(videoIds)))
    if not os.path.isdir('results'):
        os.makedirs('results')
    f = open('results/' + videoId + '.jpg','wb')
    f.write(urllib.urlopen('http://img.youtube.com/vi/' + videoId + '/default.jpg').read())
    f.close()