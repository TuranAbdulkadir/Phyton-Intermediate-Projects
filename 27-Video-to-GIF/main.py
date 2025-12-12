from moviepy.editor import VideoFileClip
import os

print("--- VIDEO TO GIF CONVERTER ---")
video_name = "video.mp4"

if os.path.exists(video_name):
    print("Video işleniyor, lütfen bekleyin... ⏳")
    
    # Videonun ilk 3 saniyesini al (Uzun sürmesin diye)
    clip = VideoFileClip(video_name).subclip(0, 3) 
    
    # GIF olarak kaydet
    clip.write_gif("output.gif", fps=10)
    print("✅ Başarılı! 'output.gif' oluşturuldu.")
else:
    print(f"❌ '{video_name}' dosyası bulunamadı!")