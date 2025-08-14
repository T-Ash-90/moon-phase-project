# Moon Phase Project

This Python script calculates the phase of the Moon for a given date using the lunar cycle. It utilizes `Tkinter` for the graphical user interface (GUI), allowing users to input a date and get the corresponding moon phase.

## Features

- Simple user interface using Tkinter.
- Supports date input in the format `YYYY-MM-DD`.
- Calculates the moon phase based on the number of days since a known New Moon date (July 24th 2025).
- Displays the corresponding moon phase (e.g., New Moon, First Quarter, Full Moon, etc.).

## Requirements

- Python 3.x
- Tkinter

If Tkinter is not installed, you can install it using the following command:
    ```
    pip install tk
    ```


## How to Use

1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Run the script:
    ```
    python3 moon_phase_calculator.py
    ```
4. A window will appear where you can enter a date in the format `YYYY-MM-DD`.
5. Click the "Calculate Moon Phase" button to get the moon phase for the given date.

## Example

- **Input**: `2023-08-14`
- **Output**: "The moon phase on 2023-08-14 is: First Quarter Waxing Crescent"
