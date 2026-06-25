import yt_dlp

def get_m3u8_url(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': False  # allow playlists (channel streams page)
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

            if 'entries' in info_dict:  # channel streams page
                m3u8_links = []
                for entry in info_dict['entries']:
                    m3u8_url = entry.get('url', None)
                    if m3u8_url and '.m3u8' in m3u8_url:
                        m3u8_links.append(m3u8_url)
                return m3u8_links if m3u8_links else "No live .m3u8 streams found."
            else:  # single video case
                m3u8_url = info_dict.get('url', None)
                if m3u8_url and '.m3u8' in m3u8_url:
                    return m3u8_url
                else:
                    return "Stream is not currently live or no m3u8 format was found."

    except Exception as e:
        return f"An error occurred: {e}"


# Channel streams page
url_channel = "https://www.youtube.com/@bcbtigercricket/streams"
stream_links = get_m3u8_url(url_channel)

print("\nExtracted M3U8 URL(s) (channel streams):\n")
if isinstance(stream_links, list):
    for link in stream_links:
        print(link)
else:
    print(stream_links)