from pytube import YouTube

def download_youtube_audio(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)
    print("Download completed successfully!")

# Contoh penggunaan
if __name__ == "__main__":
    while True:
        url = []
        while True:
            youtube_url = input('Masukkan URL video youtube : ')  # URL video YouTube
            if youtube_url == "":
                break
            url.append(youtube_url)

        output_directory = "./download"  # Direktori tempat menyimpan file audio

        for x in url:
            download_youtube_audio(x, output_directory)
