from project.room import Room
class Hotel():
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def take_room(self, room_number, people):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.take_room(people)
            self.guests = sum(r.guests for r in self.rooms)
            return result
    
    def free_room(self, room_number):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.free_room()
            self.guests = sum(r.guests for r in self.rooms)
            return result
        
    def status(self):
        total_guests = sum(room.guests for room in self.rooms)
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {total_guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
    
    
