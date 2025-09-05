class Tickets:
    def __init__(self,n,booked):
        self.Booked = booked
        self.Available = [x for x in range(1,n+1) if x not in booked]
    def book(self,seat):
        if seat in self.Available:
            self.Available.remove(seat)
            self.Booked.append(seat)
            return "Seat Booked"
        else:
            return "Seat Not Available"
    def cancel(self,seat):
        if seat in self.Booked:
            self.Booked.remove(seat)
            self.Available.append(seat)
            return "Booing Cancelled"
        else:
            return "Seat not Booked"

total_seats = 10
booked_seats = [2, 5, 7]

tickets = Tickets(total_seats,booked_seats)

tickets.book(3)

tickets.cancel(5)

print("Available Seats:", tickets.Available)
        