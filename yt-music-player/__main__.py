import re
import subprocess
import time
from ytmusicapi import YTMusic

# yt = YTMusic('oauth.json')
# playlistId = yt.create_playlist('test', 'test description')
# search_results = yt.search('Oasis Wonderwall')
# yt.add_playlist_items(playlistId, [search_results[0]['videoId']])


def extract_video_id(url):
    """
    Extracts the video ID from a YouTube Music URL.
    """
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    return None


def play_song_in_safari(video_id):
    """
    Opens Safari and plays the song on YouTube Music using osascript.
    """
    url = f"https://music.youtube.com/watch?v={video_id}"
    apple_script = f'''
    tell application "Safari"
        activate
        open location "{url}"
    end tell
    '''
    subprocess.run(["osascript", "-e", apple_script])

def pause_playback_in_safari():
    """
    Pauses playback on the currently open YouTube Music tab in Safari using osascript.
    """
    apple_script = '''
    tell application "Safari"
        set currentTab to current tab of window 1
        do JavaScript "document.querySelector('.play-pause-button').click();" in currentTab
    end tell
    '''
    subprocess.run(["osascript", "-e", apple_script])

def resume_playback_in_safari():
    """
    Resumes playback on the currently open YouTube Music tab in Safari using osascript.
    """
    apple_script = '''
    tell application "Safari"
        set currentTab to current tab of window 1
        do JavaScript "document.querySelector('.play-pause-button').click();" in currentTab
    end tell
    '''
    subprocess.run(["osascript", "-e", apple_script])

# https://music.youtube.com/watch?v=JCf7lKL1UQ4&list=RDAMVMJCf7lKL1UQ4

saijo_id = extract_video_id("https://music.youtube.com/watch?v=XROXWv-KtXM")

# play_song_in_safari("JCf7lKL1UQ4&list=RDAMVMJCf7lKL1UQ4") # big dawgs
# play_song_in_safari(saijo_id)
resume_playback_in_safari()
print("starting 10 second delay")
# Add a 10-second delay
time.sleep(10)
print("ending delay")

pause_playback_in_safari()