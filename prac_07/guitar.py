class Guitar:
    """Represent a guitar with name, year, and cost attributes."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """Return formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other: 'Guitar') -> bool:
        """Define less-than operator to compare guitars by year."""
        return self.year < other.year