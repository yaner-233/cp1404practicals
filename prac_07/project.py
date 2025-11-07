"""
CP1404 Practical
Project class to represent project details.
"""


class Project:
    """Represent a project with attributes and comparison capabilities."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return formatted string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Define less-than operator to compare projects by priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Check if the project is fully completed."""
        return self.completion == 100