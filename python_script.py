# to make a script that will download top 10 youtube meme videos and upload them on my channel
# Step 1   : make function to find top 10 videos
# Step 2   : make a function to download those videos
# Step 3   : make somehow python interact with my youtube account
# Step 3.5 : copy files to a folder
# Step 4   : upload them in timely manner

#step 1
from googleapiclient.discovery import build
import yt_dlp
import os
from filesys import move_files

api_key = 'jjj'


def top_videos(api_key, max_results=2):
  youtube = build('youtube', 'v3', developerKey=api_key)
  request = youtube.videos().list(
    part ="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults = max_results,
        videoCategoryId="23"
)
  response = request.execute()
  return [item['id'] for item in response['items']]
print(top_videos(api_key))  # Returns list of trending video IDs


#step 2

base_url = "https://www.youtube.com/watch?v="
video_ids = top_videos(api_key)


for video_id in video_ids:
  
  video = str(base_url + video_id)
  print(base_url + video_id)
  yt_dlp.YoutubeDL().download([video])
  
#step 3.5
move_files()


