import yt_dlp

def get_m3u8_url(video_url):
    # Configure yt-dlp to extract information without downloading the video
    ydl_opts = {
        'format': 'best',   # Gets the best quality stream available
        'quiet': True,      # Suppresses console output
        'noplaylist': True  # Ensures only the single video is processed
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            # For YouTube live streams, the direct 'url' is the .m3u8 manifest
            m3u8_url = info_dict.get('url', None)
            
            if m3u8_url and '.m3u8' in m3u8_url:
                return m3u8_url
            else:
                return "Stream is not currently live or no m3u8 format was found."
                
    except Exception as e:
        return f"An error occurred: {e}"


# The target YouTube Live Stream
url = "https://www.youtube.com/watch?v=Y5A7zHc8hNY"

stream_link = get_m3u8_url(url)

print("Extracted M3U8 URL:\n")
print(stream_link)