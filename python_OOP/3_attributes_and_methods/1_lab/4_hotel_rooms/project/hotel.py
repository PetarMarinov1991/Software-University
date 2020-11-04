from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: [Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f'{stars_count} stars Hotel'
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self._find_room_by_number(room_number)
        if room.take_room(people) is None:
            self.guests += people
        return room.take_room(people)

    def free_room(self, room_number):
        room = self._find_room_by_number(room_number)
        if room.free_room() is not None:
            self.guests -= room.guests
        return room.free_room()

    def _find_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room

    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests\n'
              f'Free rooms: {", ".join([str(x) for x in free_rooms])}\n'
              f'Taken rooms: {", ".join([str(x) for x in taken_rooms])}')
