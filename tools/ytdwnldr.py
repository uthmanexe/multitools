import yt_dlp
from pathlib import Path

def downloader():
    link = input("Enter video url: ").strip()
    if link.startswith(("https://", "http://")):
        url = link
    else:
        url = f"https://{link}"
    print(f"Target URL: {url}")

    
    while True:
        print("""
=========================================================
1. 144p
2. 360p
3. 480p
4. 720p
5. 1080p
=========================================================""")

        user_input =input("select preferred resolution(1-5): ").strip()
    
        if user_input not in ['1', '2', '3', '4', '5']:
            print("Invalid selection. Please choose a number between 1 and 5.")
            continue          
        res = int(user_input)

        if res == 1:
            ydl_opts = {'format': 'bestvideo[height<=144]+bestaudio/best'}
        elif res == 2:
            ydl_opts = {'format': 'bestvideo[height<=360]+bestaudio/best'}
        elif res == 3:
            ydl_opts = {'format': 'bestvideo[height<=480]+bestaudio/best'}
        elif res == 4:
            ydl_opts = {'format': 'bestvideo[height<=720]+bestaudio/best'}
        else:
            ydl_opts = {'format': 'bestvideo[height<=1080]+bestaudio/best'}

        home = Path.home()
        paths = {}
        n = 0
        for dir in home.iterdir():
            if dir.is_dir() and not dir.name.startswith("."):
                n += 1
                paths[n] = dir

        for k in paths:
            print(f"{k}: {paths[k].name}")
            
        path_choice = input(f"Choose directory(1-{n}): ").strip()
    
        if path_choice.isdigit() and int(path_choice) in paths:
            pth = paths[int(path_choice)]/"Multitools_downloads"
            pth.mkdir(parents = True, exist_ok = True)
        else:
            print("Invalid or empty choice. Using default download folder.")
            pth = Path.home() / "Downloads/Multitools_downloads"
            pth.mkdir(parents=True, exist_ok=True)
        
        print(f"Download destination: {pth}")
    
        break

    download_params = {
            'format': ydl_opts["format"],
            'outtmpl': f"{pth}/%(title)s.%(ext)s",
            'merge_output_format': 'mp4'
            }

    print(f"Starting Download...")
    with yt_dlp.YoutubeDL(download_params) as ydl:
        ydl.download([url])

    print("Download complete")
