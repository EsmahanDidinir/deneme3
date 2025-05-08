#2. Adım: Video ID'lerine göre detaylı istatistik 


import requests
video_ids = ['VxzYMeFKg20', '_CWfViJWCSE', '3t_bn6tZ_m4', 'qQdpWsGxm_E', 'OoxDAmjiVR4',
             'SuT9J9wEwyw', '49y1f9sZiBs', 'kcCGHpwGETo', 'Dvbm_aksZMs', 'jp74jgo6Nnc']
API_KEY = "AIzaSyD5ZVaqU5SwssneO3ElPp1yZzo34vXBniw"  

# ID'leri virgülle birleştir
ids = ",".join(video_ids)

# Video detayları için istek gönder
stats_url = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&part=snippet,statistics,contentDetails&id={ids}"

stats_response = requests.get(stats_url)

import isodate  # süreyi formatlamak için

def convert_duration(iso_duration):
    duration = isodate.parse_duration(iso_duration)
    return str(duration)

stats_url = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&part=snippet,statistics,contentDetails&id={ids}"
stats_response = requests.get(stats_url)

if stats_response.status_code == 200:
    videos = stats_response.json()['items']
    print("\n📺 Genişletilmiş Son 10 Video Analizi:\n")
    for video in videos:
        title = video['snippet']['title']
        published = video['snippet']['publishedAt']
        views = video['statistics'].get('viewCount', 'Yok')
        likes = video['statistics'].get('likeCount', 'Yok')
        comments = video['statistics'].get('commentCount', 'Yok')
        duration = convert_duration(video['contentDetails']['duration'])

        print(f"🎬 Başlık         : {title}")
        print(f"📅 Yayın Tarihi   : {published}")
        print(f"👁️ Görüntüleme   : {views}")
        print(f"👍 Beğeni Sayısı  : {likes}")
        print(f"💬 Yorum Sayısı   : {comments}")
        print(f"⏱️ Süre           : {duration}")
        print("-" * 50)
else:
    print("❌ Video istatistikleri alınamadı:", stats_response.status_code)
    print(stats_response.text)



import pandas as pd

video_list = []

for video in videos:
    title = video['snippet']['title']
    published = video['snippet']['publishedAt']
    views = video['statistics'].get('viewCount', '0')
    likes = video['statistics'].get('likeCount', '0')
    comments = video['statistics'].get('commentCount', '0')
    duration = convert_duration(video['contentDetails']['duration'])

    video_list.append({
        'Başlık': title,
        'Yayın Tarihi': published,
        'Görüntüleme': int(views),
        'Beğeni': int(likes),
        'Yorum': int(comments),
        'Süre': duration
    })

df = pd.DataFrame(video_list)
df.to_csv("evrim_agaci_videolar.csv", index=False, encoding="utf-8-sig")

print(df)  # Tüm tabloyu yazdırır
