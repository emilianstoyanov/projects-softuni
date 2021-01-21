
class Album:
    def __init__(self, name: str, songs=None):
        self.name = name
        if songs is None:
            songs = []
        if not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):

        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        song = [song for song in self.songs if song.name == song_name][0]
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for i in self.songs:
            result += f"== {i.get_info()}\n"
        return result
