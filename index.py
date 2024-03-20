from pytube import YouTube
from moviepy.editor import *

def download_youtube_audio(url, output_path):
    # Download video
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(output_path=output_path, filename='temp_video')

    # Convert to MP3
    video_path = f"{output_path}/temp_video.mp4"
    audio_path = f"{output_path}/audio.mp3"
    video_clip = AudioFileClip(video_path)
    video_clip.write_audiofile(audio_path)

    # Cleanup
    os.remove(video_path)
    print("Download and conversion completed successfully!")

# Example usage
if __name__ == "__main__":
    youtube_url = input('Masukkan Link video : ')  # URL of the YouTube video
    output_directory = "./download"  # Directory where you want to save the audio
    download_youtube_audio(youtube_url, output_directory)
