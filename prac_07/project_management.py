"""
CP1404 Practical
Project Management Program with menu-driven interface.
Estimated time: 45 minutes
Actual time: 1 hour
"""
import csv
from datetime import datetime
from project import Project

def main():
    """Main function to run the project management program."""
    print("Welcome to Pythonic Project Management")
    default_filename = "projects.txt"
    projects = load_projects(default_filename)
    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects 
- (F)ilter projects by date  
- (A)dd new project  
- (U)pdate project  
- (Q)uit"""

    continue_program = True
    while continue_program:
        print(menu)
        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load: ") or default_filename
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ") or default_filename
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {default_filename}? ").strip().lower()
            if save_choice in ['yes', 'y']:
                save_projects(projects, default_filename)
            else:
                print(f"no, I think not.")
            print("Thank you for using custom-built project management software.")
            continue_program = False
        else:
            print("Invalid choice. Please try again.")


def load_projects(filename):
    """Load projects from a tab-separated file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for row in reader:
                name = row[0]
                start_date = datetime.strptime(row[1], '%d/%m/%Y')
                priority = int(row[2])
                estimate = float(row[3])
                completion = int(row[4])
                projects.append(Project(name, start_date, priority, estimate, completion))
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects


def save_projects(projects, filename):
    """Save a list of Project objects to a tab-separated file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Estimate", "Completion"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime('%d/%m/%Y'),
                project.priority,
                project.estimate,
                project.completion
            ])
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a user-specified date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_str, '%d/%m/%Y')
        filtered = [p for p in projects if p.start_date > filter_date]
        filtered.sort(key=lambda x: x.start_date)
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project():
    """Get user input to create and return a new Project object."""
    print("Let's add a new project")
    name = input("Name: ")

    valid_date = False
    while not valid_date:
        date_str = input("Start date (dd/mm/yy): ")
        try:
            start_date = datetime.strptime(date_str, '%d/%m/%Y')
            valid_date = True
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")

    valid_priority = False
    while not valid_priority:
        priority_str = input("Priority: ")
        try:
            priority = int(priority_str)
            if 1 <= priority <= 10:
                valid_priority = True
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    valid_estimate = False
    while not valid_estimate:
        estimate_str = input("Cost estimate: $")
        try:
            estimate = float(estimate_str)
            valid_estimate = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    valid_completion = False
    while not valid_completion:
        completion_str = input("Percent complete: ")
        try:
            completion = int(completion_str)
            if 0 <= completion <= 100:
                valid_completion = True
            else:
                print("Completion must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return Project(name, start_date, priority, estimate, completion)


def update_project(projects):
    """Allow user to select a project and update its completion or priority."""
    if not projects:
        print("No projects to update.")
        return

    print("Projects:")
    for i, project in enumerate(projects, 0):
        print(f"{i}. {project}")

    valid_index = False
    index = 0
    while not valid_index:
        try:
            input_index = int(input("Project choice: "))
            if 0 <= input_index < len(projects):
                index = input_index
                valid_index = True
            else:
                print(f"Please enter a number between 0 and {len(projects)-1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    project = projects[index]
    print(project)

    completion_str = input("New Percentage: ")
    if completion_str:
        try:
            completion = int(completion_str)
            if 0 <= completion <= 100:
                project.completion = completion
            else:
                print("Completion must be between 0 and 100. Not updated.")
        except ValueError:
            print("Invalid input. Completion not updated.")

    priority_str = input("New Priority: ")
    if priority_str:
        try:
            priority = int(priority_str)
            if 1 <= priority <= 10:
                project.priority = priority
            else:
                print("Priority must be between 1 and 10. Not updated.")
        except ValueError:
            print("Invalid input. Priority not updated.")




if __name__ == "__main__":
    main()