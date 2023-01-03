import asyncio
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


async def track_escape_room(tracker, room_name):
    room = tracker.get_room(room_name)
    room.enter()
    await asyncio.sleep(60)  # simulate people being in the room for 1 minute
    room.exit()
    duration = tracker.get_duration(room_name)
    print(f"It took {duration.seconds} seconds to complete {room_name}")

async def main():
    tracker = EscapeRoomTracker()

    room1 = EscapeRoom("Room 1")
    room2 = EscapeRoom("Room 2")

    tracker.add_room(room1)
    tracker.add_room(room2)

    await track_escape_room(tracker, "Room 1")
    await track_escape_room(tracker, "Room 2")

asyncio.run(main())
