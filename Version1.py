"""
Version 1: Initial version - basic input and output
Description: The program asks for inputs and displays simple output.
"""

def register_student():
    print("=== Student Event Registration System (v1) ===")
    
    # Required Inputs
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    section = input("Enter section: ")
    event_name = input("Enter event name: ")
    event_year = input("Enter event year: ")
    event_month = input("Enter event month: ")
    event_day = input("Enter event day: ")
    
    # Basic Output without formatting
    print("\n" + "="*40)
    print("Student Event Registration Summary")
    print(f"Name: {first_name} {last_name}")
    print(f"Section: {section}")
    print(f"Event: {event_name}")
    print(f"Event Date: {event_month} {event_day}, {event_year}")
    print("Language Used: Python")
    print("String Feature Used: None")
    print("Date/Time Feature Used: None")
    print("Registration record created successfully.")
    print("="*40)

if __name__ == "__main__":
    register_student()
