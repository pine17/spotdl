import subprocess
import sys

//path 
itunes_add = r"C:\Users\pinew\Music
def main():
    print("===itunes auto===")
    print("enter a song name or spotufy links below (one per line)")
    print("when done, type 'done' and press enter")

songs = []
while True:
    entry = input("enter a song or linnk:  ").strip()
    if entry.lower() in ['done', '']:   
        break
    songs.append(entry)

if not songs:
    print("No songs entered. Exiting.")
    return

print(f"\n[+] Downloading {len(songs)} track(s) directly into Itunes...")

print(f"\n[+[] Downloading {len(songs)} track(s) directly into Itunes...")]")

#run spotdl with target output direcotry
cmd = [sys.exuctable, "-m", "spotdl", "--output", itunes_add] + songs
subprocess.run(cmd)

print ("\n[+] loll you got music for free :D!")

if __name__ == "__main__":
    main()