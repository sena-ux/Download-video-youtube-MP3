from pytube import YouTube
import os
def on_progress(stream, chunk, remaining):
    # Mendapatkan total bytes dari video yang akan diunduh
    total_size = stream.filesize
    
    # Menghitung jumlah bytes yang telah diunduh
    bytes_downloaded = total_size - remaining
    
    # Menghitung persentase kemajuan unduhan
    progress = (bytes_downloaded / total_size) * 100
    
    # Menampilkan proses unduhan
    print(f"\rDownloading... {progress:.2f}%", end='')

    
def download_youtube_audio(url, output_path):
    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)
    print("Download completed successfully!")



# Contoh penggunaan
if __name__ == "__main__":
    while True:
        urls = []
        youtube_url = input('Masukkan URL video youtube (tekan Enter untuk berhenti) : ')  # URL video YouTube
        if youtube_url == "":
            break
        urls.append(youtube_url)

        output_directory = "./download"  # Direktori tempat menyimpan file audio

        for url in urls:
            download_youtube_audio(url, output_directory)
