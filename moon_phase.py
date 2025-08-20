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
        result_label.config(text=f"The moon phase on {date_input} is:\n{moon_phase}", fg="white", font=("Arial", 12), bg="#333")
    except ValueError:
        result_label.config(text="Invalid date format. Please enter as YYYY-MM-DD.", fg="red", font=("Arial", 12, "bold"), bg="#f0f0f0")

# Create the main window
root = tk.Tk()
root.title("Moon Phase Calculator")
root.geometry("600x400")  # Window size
root.config(bg="#111b31")  # Dark background for a more celestial feel

# Create a label for the title
title_label = tk.Label(root, text="Moon Phase Calculator", font=("Arial", 18, "bold"), bg="#111b31", fg="white")
title_label.pack(pady=20)

# Create a frame to organize the input section
input_frame = tk.Frame(root, bg="#111b31")
input_frame.pack(pady=10)

# Create a label for the input date
date_label = tk.Label(input_frame, text="Enter a date (YYYY-MM-DD):", font=("Arial", 12), bg="#111b31", fg="white")
date_label.grid(row=0, column=0, padx=10, pady=5)

# Create a text entry field for the date
date_entry = tk.Entry(input_frame, font=("Arial", 12), width=18, bd=2, relief="solid", highlightthickness=2, justify="center")
date_entry.grid(row=0, column=1, padx=10, pady=5)

# Create a button to calculate the moon phase
calculate_button = tk.Button(root, text="Calculate Moon Phase", font=("Arial", 12), command=on_button_click, bg="#ff9800", fg="white", relief="raised", padx=15, pady=10)
calculate_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#333", fg="white", anchor="center", width=40, height=4)
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
