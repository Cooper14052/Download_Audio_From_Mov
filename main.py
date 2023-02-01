import moviepy.editor
from pathlib import Path
import time
import threading

video_file = Path('.mp4')
video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')
