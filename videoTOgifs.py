from moviepy.editor import *

video = VideoFileClip("your_video_file.mp4").subclip(0, 5).rotate(60)

text = TextClip("Your Text Here", fontsize=40, color='white', font='Arial')

text = text.crossfadein(1).crossfadeout(1)

text = text.resize(lambda t: 1 + 0.5 * t)

text = text.set_opacity(lambda t: min(1, max(0, t)))

video_with_text = CompositeVideoClip([video, text])

audio = AudioFileClip("your_audio_file.mp3").subclip(0, 5)  # Ensure the audio duration matches the video
video_with_text = video_with_text.set_audio(audio)

video_with_text.write_gif("your_animated_gif_with_audio.gif", fps=10)
