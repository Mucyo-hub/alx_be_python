# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a Match Case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print(f"\nReminder: {reminder}")
