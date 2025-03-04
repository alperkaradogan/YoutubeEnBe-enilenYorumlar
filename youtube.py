
#en çok beğenilen zaman damgalı yorumlar beğeni sırasına göre başlığın adında txt'ye yazdırır.

import re
from googleapiclient.discovery import build

# YouTube API anahtarını buraya gir
API_KEY = "SENİN_API_ANAHTARIN"

# Video ID
video_id = "SENİN_VİDEO-İD'in"

# YouTube API istemcisi oluştur
youtube = build("youtube", "v3", developerKey=API_KEY)

# 1️⃣ Videonun başlığını al
video_request = youtube.videos().list(
    part="snippet",
    id=video_id
)
video_response = video_request.execute()
video_title = video_response["items"][0]["snippet"]["title"]

# Dosya ismi olarak geçerli karakterleri kullan
safe_filename = "".join(c if c.isalnum() or c in " _-" else "_" for c in video_title) + ".txt"

# 2️⃣ En çok beğenilen yorumları al
comments_request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=50,  # Daha fazla yorum alıp filtreleyelim
    order="relevance"  # En çok beğenilenler
)
comments_response = comments_request.execute()

# 3️⃣ Zaman damgalı yorumları filtrele
time_pattern = re.compile(r"\b\d{1,2}:\d{2}\b")  # 3:25, 12:40 gibi zaman formatlarını algılar
filtered_comments = []

for item in comments_response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]
    text = comment["textDisplay"]
    likes = comment["likeCount"]
    
    # Eğer yorumda zaman damgası varsa, listeye ekle
    if time_pattern.search(text):
        filtered_comments.append((likes, text))

# 4️⃣ Beğeniye göre sırala (Büyükten küçüğe)
filtered_comments.sort(reverse=True, key=lambda x: x[0])

# 5️⃣ Dosyaya yaz
with open(safe_filename, "w", encoding="utf-8") as file:
    file.write(f"Video Başlığı: {video_title}\n")
    file.write("=" * 50 + "\n\n")
    
    for likes, text in filtered_comments:
        file.write(f"👍 {likes} beğeni\n{text}\n\n")
    
print(f"Zaman damgalı yorumlar kaydedildi: {safe_filename}")
