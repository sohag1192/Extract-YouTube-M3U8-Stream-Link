import re
import requests

def get_live_m3u8(channel_url):
    # Append /live to ensure we route to the active live stream
    live_url = f"{channel_url.rstrip('/')}/live"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Fetching live stream data from: {live_url}...")
    
    try:
        response = requests.get(live_url, headers=headers, timeout=10)
        response.raise_for_status()
        html = response.text

        # Search for the HLS manifest URL in the page source
        match = re.search(r'"hlsManifestUrl":"([^"]+)"', html)
        
        if match:
            # Clean up YouTube's escaped JSON formatting
            clean_m3u8_url = match.group(1).replace('\\/', '/').replace('\\u0026', '&')
            return clean_m3u8_url
        else:
            return "Error: Could not find an active live stream (.m3u8) on this page. The channel might not be live right now."
            
    except requests.exceptions.RequestException as e:
        return f"Network Error: {e}"

# The target channel
CHANNEL_URL = "https://www.youtube.com/@bcbtigercricket"

# Run the function
m3u8_link = get_live_m3u8(CHANNEL_URL)

print("\n--- EXTRACTED M3U8 LINK ---")
print(m3u8_link)