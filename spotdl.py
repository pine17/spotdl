import os
import subprocess
import sys

# path 
# here you can put any user you want if you need help finding ur user
# just go to ur c drive or any file you want and click the bar were you can see the file name and ctrl c
music_dir = os.path.join(os.path.expanduser("~"), "Music")

def main():
    print("===music auto===")
    print("enter a song name or spotufy links below (one per line)")
    print("when done, type 'done' and press enter")

    songs = []
    while True:
        entry = input("enter a song or linnk:  ").strip()
        if entry.lower() in ['done', '']:   
            break
        songs.append(entry)

    if not songs:
        print("What is this supposed to be.")
        return

    print(f"\n[+] Downloading {len(songs)} track(s) directly into Music folder...")

    #run spotdl with target output direcotry
    cmd = [sys.executable, "-m", "spotdl", "--output", music_dir] + songs
    subprocess.run(cmd)

    print("\n[+] loll you got music for free :D!")

if __name__ == "__main__":
    main()
