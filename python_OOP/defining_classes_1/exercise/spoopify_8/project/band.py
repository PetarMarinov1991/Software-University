from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        return f'Band {self.name} already has {album.name} in their library.'

    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            current_album = albums_list[0]
            if current_album.published:
                return 'Album has been published. It cannot be removed.'
            self.albums.remove(current_album)
            return f'Album {current_album.name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        result = f'Band {self.name}\n'
        for a in self.albums:
            result += f'{a.details()}\n'
        return result
