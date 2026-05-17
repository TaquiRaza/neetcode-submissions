class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = [[position[i], speed[i]] for i in range(len(speed))]
        cars.sort(reverse=True)
        print(cars)

        for p, s in cars:
            t = (target - p) / s
            print(t)
            if fleets and t <= fleets[-1]:
                t = fleets.pop()
            fleets.append(t)

        return len(fleets)