"""
Version 2: Added string formatting
Description: The program cleans or formats the name, section, and event title.
"""

def register_student():
    print("=== Student Event Registration System (v2) ===")
    
    # Required Inputs
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    section = input("Enter section: ")
    event_name = input("Enter event name: ")
    event_year = input("Enter event year: ")
    event_month = input("Enter event month: ")
    event_day = input("Enter event day: ")
    
    # String Formatting & Cleaning
    cleaned_first = first_name.strip().title()
    cleaned_last = last_name.strip().title()
    full_proper = f"{cleaned_first} {cleaned_last}"
    full_upper = full_proper.upper()
    
    cleaned_section = section.strip().upper()
    cleaned_event = event_name.strip().title()
    
    # Output with String Formatting Applied
    print("\n" + "="*40)
    print("Student Event Registration Summary")
    print(f"Name: {full_proper}")
    print(f"Name Code: {full_upper}")
    print(f"Section: {cleaned_section}")
    print(f"Event: {cleaned_event}")
    print(f"Event Date: {event_month.strip().title()} {event_day.strip()}, {event_year.strip()}")
    print("Language Used: Python")
    print("String Feature Used: strip(), title(), upper()")
    print("Date/Time Feature Used: None")
    print("Registration record created successfully.")
    print("="*40)

if __name__ == "__main__":
    register_student()
