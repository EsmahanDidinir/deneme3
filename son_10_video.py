#1. Adım: Kanalın son 10 videosunun ID’lerini çek

import requests

API_KEY = "AIzaSyD5ZVaqU5SwssneO3ElPp1yZzo34vXBniw" 
CHANNEL_ID = "UCatnasFAiXUvWwH8NlSdd3A"

search_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=10"

response = requests.get(search_url)
video_ids = []

if response.status_code == 200:
    results = response.json()
    for item in results['items']:
        if item['id']['kind'] == 'youtube#video':
            video_ids.append(item['id']['videoId'])
else:
    print("❌ Video ID'leri alınamadı:", response.status_code)
    print(response.text)

print(video_ids)


