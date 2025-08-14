import tkinter as tk
from datetime import datetime

# Known New Moon date (24th July 2025)
NEW_MOON_DATE = datetime(2025, 7, 24)

# Length of the lunar cycle in days (approx)
LUNAR_CYCLE = 29.53

# Function to calculate the moon phase
def get_moon_phase(date):
    # Calculate the number of days since the known New Moon date
    days_since_new_moon = (date - NEW_MOON_DATE).days

    # Find the phase of the moon
    phase = (days_since_new_moon % LUNAR_CYCLE) / LUNAR_CYCLE

    # Determine the moon phase based on the phase value
    if 0.0 <= phase < 0.03:
        return "New Moon"
    elif 0.03 <= phase < 0.25:
        return "First Quarter Waxing Crescent"
    elif 0.25 <= phase < 0.5:
        return "First Quarter"
    elif 0.5 <= phase < 0.75:
        return "Last Quarter Waxing Gibbous"
    elif 0.75 <= phase < 1.0:
        return "Full Moon"
    elif 0.97 <= phase < 1.0:
        return "Waning Crescent"
    else:
        return "Unknown Phase"

# Function to handle the button click event
def on_button_click():
    try:
        # Get the input date from the text field
        date_input = date_entry.get()
        date_object = datetime.strptime(date_input, "%Y-%m-%d")

        # Get the moon phase for the given date
        moon_phase = get_moon_phase(date_object)

        # Display the result in the label
        result_label.config(text=f"The moon phase on {date_input} is: {moon_phase}", fg="blue", font=("Helvetica", 12, "bold"))
    except ValueError:
        result_label.config(text="Invalid date format. Please enter as YYYY-MM-DD.", fg="red", font=("Helvetica", 12, "bold"))

# Create the main window
root = tk.Tk()
root.title("Moon Phase Calculator")
root.geometry("402x202")  # Window size
root.config(bg="#08c2b1")  # Background color

# Create a label for the title
title_label = tk.Label(root, text="Moon Phase Calculator", font=("Helvetica", 16, "bold"), bg="#08c2b1", fg="#333", anchor="center")
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# Create a label for the input date
date_label = tk.Label(root, text="Enter a date (YYYY-MM-DD):", font=("Helvetica", 12), bg="#08c2b1", fg="#333", anchor="center")
date_label.grid(row=1, column=0, pady=10)

# Create a text entry field for the date
date_entry = tk.Entry(root, font=("Helvetica", 12), width=20, bd=2, relief="solid", highlightthickness=2, justify="center")
date_entry.grid(row=1, column=1, pady=10)

# Create a button to calculate the moon phase
calculate_button = tk.Button(root, text="Calculate Moon Phase", font=("Helvetica", 12), command=on_button_click, bg="#4CAF50", fg="white", relief="raised", padx=10, pady=5)
calculate_button.grid(row=2, column=0, columnspan=2, pady=15)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="#333", anchor="center")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
