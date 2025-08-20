# youtube_downloader.py
from pytubefix import YouTube
from pytubefix.cli import on_progress
from tqdm import tqdm


def download_video(link: str, output_path: str = "D:\\to_be_deleted"):
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        print("Title:", yt.title)
        print("Views:", yt.views)

        stream = yt.streams.get_highest_resolution()
        file_size = stream.filesize
        print(
            f"Downloading: {stream.default_filename} ({file_size / (1024*1024):.2f} MB)"
        )

        # Custom progress bar
        progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Progress")

        def show_progress(stream, chunk, bytes_remaining):
            progress = file_size - bytes_remaining
            progress_bar.n = progress
            progress_bar.refresh()

        yt.register_on_progress_callback(show_progress)

        stream.download(output_path)
        progress_bar.close()

        print("✅ Download complete.")
    except Exception as e:
        print("❌ An error occurred:", e)


if __name__ == "__main__":
    link = "https://youtu.be/eWRfhZUzrAc?si=s9snly96henSHILa"
    download_video(link)
