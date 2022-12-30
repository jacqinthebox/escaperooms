import datetime

class EscapeRoom:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None

    def enter(self):
        self.start_time = datetime.datetime.now()

    def exit(self):
        self.end_time = datetime.datetime.now()

class EscapeRoomTracker:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def get_room(self, name):
        return self.rooms[name]

    def get_duration(self, room_name):
        room = self.get_room(room_name)
        return room.end_time - room.start_time


# Example usage
tracker = EscapeRoomTracker()

room1 = EscapeRoom("Room 1")
room2 = EscapeRoom("Room 2")

tracker.add_room(room1)
tracker.add_room(room2)

room1.enter()
# Some time passes
room1.exit()

duration = tracker.get_duration("Room 1")
print(f"It took {duration.seconds} seconds to complete Room 1")
