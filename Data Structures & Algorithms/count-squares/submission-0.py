class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), freq in list(self.point_count.items()):
            if px != x or py == y:
                continue  # must share x-coordinate, and be a different point

            side = py - y
            # Try both directions (left and right square)
            for dx in (side, -side):
                x2 = x + dx
                corner1 = (x2, y)
                corner2 = (x2, py)
                if corner1 in self.point_count and corner2 in self.point_count:
                    total += freq * self.point_count[corner1] * self.point_count[corner2]

        return total
