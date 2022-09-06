# Convert Video filar to gif
# by Busyman.Inc

from moviepy.editor import VideoFileClip
videoClip = VideoFileClip("video.mp4")
videoClip.write_gif("video.gif") 
