from project.rooms.room import Room


class Everland:
    def __init__(self, rooms=None):
        if rooms is None:
            rooms = []
        self.rooms = rooms

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.calculate_expenses() for room in self.rooms])
        return f'Monthly consumption: {total_consumption}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            amount = room.expenses + room.room_cost
            if amount >= room.expenses:
                result.append(
                    f'{room.family_name} paid {amount:.2f}$ and have {room.budget:.2f}$ left.')
                room.budget -= amount
            else:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])
        appliances = [room.expenses for room in self.rooms]
        result = [f'Total population: {total_population}']
        for i, room in enumerate(self.rooms):
            result.append(f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, '
                          f'Expenses: {room.expenses:.2f}$')
            child_cost = 0
            if room.members_count > 2:
                for child in [room.children]:
                    for idx, c in enumerate(child):
                        result.append(f'--- Child {idx + 1} monthly cost: {c.cost}$')
                        child_cost += c.cost
            result.append(f'--- Appliances monthly cost: {appliances[i] - child_cost:.2f}$')
        return '\n'.join(result)
