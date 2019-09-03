import youtube_dl

import urllib.request
from bs4 import BeautifulSoup
#------------------------------------------------------------------------

def downVideo(vidURL):
    ydl_opts = {
        'format' : 'best',
        'ignoreerrors': True,
        #matchtitle: '',
        #rejecttitle: 
        #min_views:
        #noplaylist:
        'outtmpl': 'c:\\temp\\videos\\%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vidURL])
#------------------------------------------------------------------------

def getVideoURL(searchString):
    textToSearch = searchString
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    myVideoList = []
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        vidURL = 'https://www.youtube.com' + vid['href']
        myVideoList.append(vidURL)

    return myVideoList
#------------------------------------------------------------------------        

#print(getVideoURL("funck"))
#videoList = getVideoURL("funck")
videoList = getVideoURL("extraterrestrials")

for i in videoList:
    downVideo(i)

#print(videoList)
#downVideo(videoList[0])
