import subprocess
import os


def download_video_and_captions(playlist_url, output_dir="downloads"):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the yt-dlp command to download the playlist
    command = [
        "yt-dlp",  # yt-dlp command
        playlist_url,  # Playlist URL
        "--write-subs",  # Option to download subtitles
        "--write-auto-subs",  # Option to download automatically generated subtitles
        "--sub-lang", "en",  # Language for subtitles (English)
        "--merge-output-format", "mp4",  # Merge video and audio into mp4
        "--output", f"{output_dir}/%(title)s.%(ext)s",  # Output directory and file name
        "--sleep-interval", "5",  # Delay between downloads
        "--max-sleep-interval", "15"  # Maximum delay between downloads
    ]

    try:
        # Run the command using subprocess
        subprocess.run(command, check=True)
        print("Download complete!")

        # Extract captions
        extract_captions(output_dir)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def extract_captions(output_dir):
    # Find all subtitle files in the output directory
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".en.srt"):  # Assuming the subtitle file has a 'en' language tag
                file_path = os.path.join(root, file)
                print(f"Extracted caption file: {file_path}")
                # You can save these files elsewhere or manipulate them if needed


# URL of the playlist you want to download
playlist_url = "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSwJbzAIRSDN_2IKInKEaUe"

# Call the function to download the playlist and scrape captions
download_video_and_captions(playlist_url)
