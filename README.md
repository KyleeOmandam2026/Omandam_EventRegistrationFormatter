# Student Event Registration Formatter

## Project Overview
A simple Python program designed to collect student registration details for school events, clean messy inputs using string methods, and format dates cleanly using Python's built-in `datetime` module.

## Versions & Commit History
- **Version 1:** Initial version containing basic input collection and direct output display.
- **Version 2:** Added string formatting methods (`strip()`, `title()`, `upper()`) to normalize student names, sections, and event titles.
- **Version 3:** Integrated the `datetime` module to validate and format event dates into a clean, readable format (`Month Day, Year`).

## How to Run the Program
1. Make sure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python Version3.py

## Reflection

1. What did you learn from this activity?
I learned how to clean messy user data using string methods like strip(), title(), and upper(). I also gained hands-on experience using Python's datetime module to properly parse and format dates into a clean, readable structure.

2. What challenges did you face and how did you overcome them?
A major challenge was handling different month formats (e.g., numbers vs. spelled-out names). I overcame this by using a try-except block and conditional checks to gracefully process both types of input without crashing the program.

3. Why is version control (GitHub commits) important in programming?
Breaking the project into three versions taught me the value of incremental development. It made debugging much easier, allowed me to track code changes, and provided a clear history of how the program evolved from a basic script into a polished application.
