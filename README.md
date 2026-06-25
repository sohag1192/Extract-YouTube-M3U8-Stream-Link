# Extract-YouTube-M3U8-Stream-Link

---

## 📖 README Overview

### 🔹 Project Purpose
This tool/script extracts the **direct M3U8 (HLS) stream link** from YouTube videos or live streams.  
That link can then be used in IPTV players, ffmpeg, VLC, or streaming servers.

### 🔹 Features
- Fetches YouTube video metadata using `yt-dlp` or `youtube-dl`.
- Extracts the `.m3u8` playlist URL from live streams.
- Outputs the direct stream link for integration into IPTV playlists.
- Can be automated to refresh links (since YouTube stream URLs expire).

### 🔹 Requirements
- **Python 3.x**
- **yt-dlp** (`pip install yt-dlp`)
- Optional: Flask/PHP wrapper if you want a web interface.

### 🔹 Installation
```bash
git clone https://github.com/sohag1192/Extract-YouTube-M3U8-Stream-Link.git
cd Extract-YouTube-M3U8-Stream-Link
pip install -r requirements.txt
```

### 🔹 Usage
```bash
python extract.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Output:
```
https://manifest.googlevideo.com/api/manifest/hls_playlist/.../index.m3u8
```

### 🔹 Example Integration
- Add the extracted link to an `.m3u` playlist:
  ```
  #EXTINF:-1, YouTube Live
  https://manifest.googlevideo.com/api/manifest/hls_playlist/.../index.m3u8
  ```
- Play it in VLC or IPTV software.

### ⚠️ Notes
- YouTube stream links **expire quickly** (often within hours).
- You must refresh them regularly with `yt-dlp`.
- Redistribution of YouTube streams may violate YouTube’s Terms of Service — use responsibly.

---
