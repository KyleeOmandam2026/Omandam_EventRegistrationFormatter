"""
Version 3: Added date formatting
Description: The program displays the event date in a readable format using datetime.
"""

from datetime import datetime

def register_student():
    print("=== Student Event Registration System (v3) ===")
    
    # Required Inputs
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    section = input("Enter section: ")
    event_name = input("Enter event name: ")
    event_year = input("Enter event year (e.g., 2026): ")
    event_month = input("Enter event month (e.g., 6 or June): ")
    event_day = input("Enter event day (e.g., 3): ")
    
    # String Formatting & Cleaning
    cleaned_first = first_name.strip().title()
    cleaned_last = last_name.strip().title()
    full_proper = f"{cleaned_first} {cleaned_last}"
    full_upper = full_proper.upper()
    
    cleaned_section = section.strip().upper()
    cleaned_event = event_name.strip().title()
    
    # Date Formatting using datetime
    try:
        year = int(event_year.strip())
        day = int(event_day.strip())
        month_input = event_month.strip()
        
        if month_input.isdigit():
            month = int(month_input)
            event_date_obj = datetime(year, month, day)
        else:
            date_string = f"{month_input} {day} {year}"
            try:
                event_date_obj = datetime.strptime(date_string, "%B %d %Y")
            except ValueError:
                event_date_obj = datetime.strptime(date_string, "%b %d %Y")
                
        readable_date = event_date_obj.strftime("%B %d, %Y")
        
    except ValueError:
        readable_date = f"{event_month.strip().title()} {event_day.strip()}, {event_year.strip()}"

    # Required Output Summary
    print("\n" + "="*40)
    print("Student Event Registration Summary")
    print(f"Name: {full_proper}")
    print(f"Name Code: {full_upper}")
    print(f"Section: {cleaned_section}")
    print(f"Event: {cleaned_event}")
    print(f"Event Date: {readable_date}")
    print("Language Used: Python")
    print("String Feature Used: strip(), title(), upper()")
    print("Date/Time Feature Used: datetime")
    print("Registration record created successfully.")
    print("="*40)

if __name__ == "__main__":
    register_student()
