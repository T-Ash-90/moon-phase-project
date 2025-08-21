import tkinter as tk
import ephem
from datetime import datetime

# Function to get the moon phase using ephem
def get_moon_phase(date):
    # Convert the date to the format that ephem understands
    date_object = ephem.Date(date)

    # Get the moon phase using ephem
    phase = ephem.Moon(date_object).phase

    # Classify the moon phase based on the percentage of the lunar cycle
    if phase < 1:
        return "New Moon"
    elif phase < 50:
        return "Waxing Crescent"
    elif phase == 50:
        return "First Quarter"
    elif phase < 99:
        return "Waning Gibbous"
    elif phase == 99:
        return "Full Moon"
    else:
        return "Invalid Phase"

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
