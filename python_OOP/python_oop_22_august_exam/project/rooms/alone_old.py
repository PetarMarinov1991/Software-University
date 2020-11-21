from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        Room.__init__(self, family_name, budget=pension, children=None, expenses=None, members_count=1)
        self.room_cost = 10
