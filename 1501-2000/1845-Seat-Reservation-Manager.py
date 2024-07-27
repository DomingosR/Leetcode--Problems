class SeatManager:

    def __init__(self, n: int):
        self.lowestNum = 1
        self.unreserved = []
        heapify(self.unreserved)
        
    def reserve(self) -> int:
        if not self.unreserved:
            self.lowestNum += 1
            return self.lowestNum - 1
        return heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)