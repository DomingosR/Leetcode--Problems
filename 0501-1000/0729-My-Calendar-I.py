class MyCalendar(object):
    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        for i in range(len(self.bookings)):
            if start < self.bookings[i][1] and end >= self.bookings[i][0] + 1:
                return False
        self.bookings.append([start, end])
        return True