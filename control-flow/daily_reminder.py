task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        priority_text = "high"
    case "medium":
        priority_text = "medium"
    case "low":
        priority_text = "low"
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")