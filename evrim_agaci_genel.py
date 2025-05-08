import requests


API_KEY = "AIzaSyD5ZVaqU5SwssneO3ElPp1yZzo34vXBniw" # YouTube API Anahtarı


CHANNEL_ID = "UCatnasFAiXUvWwH8NlSdd3A" # Evrim Ağacı kanalının ID'si


url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={CHANNEL_ID}&key={API_KEY}" # API URL


response = requests.get(url) # API isteği

# Yanıt başarılıysa veriyi al
if response.status_code == 200:
    data = response.json()
    snippet = data['items'][0]['snippet']
    stats = data['items'][0]['statistics']

    print("📊 Evrim Ağacı Kanal Analizi")
    print(f"Kanal Adı         : {snippet['title']}")
    print(f"Açıklama          : {snippet['description'][:600]}...")  # İlk 600 karakter
    print(f"Ülke              : {snippet.get('country', 'Belirtilmemiş')}")
    print(f"Abone Sayısı      : {stats.get('subscriberCount', 'Gizli')}")
    print(f"Toplam Video Sayısı: {stats.get('videoCount')}")
    print(f"Toplam Görüntülenme: {stats.get('viewCount')}")
else:
    print("❌ Bir hata oluştu:", response.status_code)
    print(response.text)
