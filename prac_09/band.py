class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musicians to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return the string of the band and its members"""
        members_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({members_str})"

    def play(self):
        """Return the performance status of all members"""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)