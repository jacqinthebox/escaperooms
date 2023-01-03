import asyncio
import datetime
import aio_pika


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


async def track_escape_room(room_name, connection):
    tracker = EscapeRoomTracker()

    room1 = EscapeRoom("Room 1")
    room2 = EscapeRoom("Room 2")

    tracker.add_room(room1)
    tracker.add_room(room2)

    # Create a channel and queue to receive messages
    channel = await connection.channel()
    queue = await channel.declare_queue("escape_room_tracker")

    async with queue.iterator() as queue_iter:
        # Wait for a message to arrive
        async for message in queue_iter:
            room = tracker.get_room(room_name)
            if message.body.decode() == "enter":
                room.enter()
            elif message.body.decode() == "exit":
                room.exit()
                duration = tracker.get_duration(room_name)
                print(f"It took {duration.seconds} seconds to complete {room_name}")
            await message.ack()


async def main():
    # Connect to RabbitMQ
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")

    # Start a task to track each escape room
    await asyncio.gather(
        track_escape_room("Room 1", connection),
        track_escape_room("Room 2", connection),
    )

asyncio.run(main())
