from pytube import YouTube

def download_video(link):
    try:
        youtube_object = YouTube(link)
        video_stream = youtube_object.streams.get_highest_resolution()
        video_stream.download()

        print("Download completed successfully!")
    except Exception as e:
        print(f"An error has occurred: {e}")

# Ask user for the YouTube video URL
if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    download_video(link)
