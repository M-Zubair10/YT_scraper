import subprocess
import os

urls = [
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSHfomCtXWV_hp0AZo_d_fa",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZTd2rKxXdy-_I0JDHlwdy6j",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQEBlbUr3GePc_aRK1US_Df",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQtQnllF2ecgXpCPd33QfF2",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQmeMz0CnyUaeO_P4v4bq1W",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZTOIcqpWp_s4uXa3X_Co8ko",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQFCBYrF01ZXjWgBFhTgalQ",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZTyjR7IsAsSyHEOp0KxOOIh",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSL5LgA0BHNobNODJiiz1nk",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQvwdyM080FxE2xmWeoTKY_",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSivBpJnQtnCeLpD3T8OqT1",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZRvGqHusQcmB3tIOv1rD10_",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQwhjc0XwnziWpYsNmN5TXn",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQRfRFyd9wHJay7F3qu-F7S",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZQoUqkMT8P2eV6JP90GDGpt",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZS-_OSf5O32yfuJJ_rfvdmC",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSDI508JYcq2fTxiEDvfiwc",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZT4pNemi-7M5xFRfkuw3z-Z",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZSwJbzAIRSDN_2IKInKEaUe",
    "https://www.youtube.com/playlist?list=PLjkaUn6QNTZRFNiu0a8z3QmioVuZhWob2"
]

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

# Loop over each URL in the list and download the videos and captions
for playlist_url in urls:
    download_video_and_captions(playlist_url)
