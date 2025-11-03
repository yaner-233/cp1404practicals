class Guitar:
    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self) -> int:
        return 2025 - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50

    def __lt__(self, other: 'Guitar') -> bool:
        return self.year < other.year