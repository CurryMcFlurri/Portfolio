from pydub import AudioSegment
import os

def has_silence(file_path):
    song = AudioSegment.from_file(file_path)
    beginning_silence = song[:6000].dBFS < -60  # 5000 ms (5 seconds) of the beginning of the song
    end_silence = song[-8000:].dBFS < -60  # 8000 ms (8 seconds) at the end of the song
    return beginning_silence or end_silence


def find_songs_with_silence(folder_path):
    songs_with_silence = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".mp3"):  # Only process mp3 files
                file_path = os.path.join(root, file_name)
                if has_silence(file_path):
                    songs_with_silence.append(file_path)
    return songs_with_silence


def delete_song(file_path):
    os.remove(file_path)


music_folder_path = (r"folder\path\here")
songs_with_silence = find_songs_with_silence(music_folder_path)

if len(songs_with_silence) == 0:
    print("No songs with silence found.")
else:
    for song_path in songs_with_silence:
        print(f"Song with silence found: {song_path}")
        choice = input("Do you want to delete this song? (y/n) ")
        if choice.lower() == "y":
            delete_song(song_path)
            print("Song deleted.")
