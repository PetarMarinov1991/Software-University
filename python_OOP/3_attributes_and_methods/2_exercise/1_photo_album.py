class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if len(self.photos[self.page]) == 4:
            self.page += 1
        if self.page == self.pages:
            return 'No more free spots'
        self.photos[self.page].append(label)
        return f'{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}'

    def display(self):
        result = ''
        photos = [[[] for _ in photo] for photo in self.photos]
        separator = '-' * 11 + '\n'
        for page in photos:
            result += ' '.join([str(p) for p in page]) + "\n" + separator
        return separator + result
