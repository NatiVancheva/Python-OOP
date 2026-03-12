class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        if not(0 <= hours < 24):
            raise ValueError("Hours must between 0 and 23.")
        if not (0 <= minutes < 60):
            raise ValueError("Minutes must be between 0 and 59.")
        if not (0 <= seconds < 60):
            raise ValueError("Seconds must be between 0 and 59.")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def next_second(self):
        self.seconds += 1

        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

                if self.hours >= 24:
                    self.hours = 0 

        return self.get_time()
    
    def __str__(self):
        return self.get_time()
    
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)

print(time.next_second())
time = Time(23, 59, 59)

print(time.next_second())
        