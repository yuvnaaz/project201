import tkinter as tk

# Create a parent window
window = tk.Tk()

# Set the size of the parent window
window.geometry("400x400")

# Define title for parent window
window.title("Interest Calculator")

# Configure the parent window
window.configure(bg="light blue")

# Create a heading label
heading = tk.Label(window, text="Interest Calculator", font=("Arial", 16))
heading.place(x=100, y=20)

# Create a Label() for Principal
principal_label = tk.Label(window, text="Principal:")
principal_label.place(x=50, y=80)

# Create an Entry() for Principal
principal_entry = tk.Entry(window)
principal_entry.place(x=150, y=80)

# Create a Label() for Rate of Interest
rate_label = tk.Label(window, text="Rate of Interest:")
rate_label.place(x=50, y=120)

# Create an Entry() for Rate of Interest
rate_entry = tk.Entry(window)
rate_entry.place(x=150, y=120)

# Create a Label() for Time
time_label = tk.Label(window, text="Time (in years):")
time_label.place(x=50, y=160)

# Create an Entry() for Time
time_entry = tk.Entry(window)
time_entry.place(x=150, y=160)

# Create a Button() for Calculation
calculate_button = tk.Button(window, text="Calculate")
calculate_button.place(x=150, y=200)

# Create a LabelFrame() widget for the result frame container
result_frame = tk.LabelFrame(window, text="Result", padx=10, pady=10)
result_frame.place(x=50, y=250)

# Create one Label() widget to show final output message inside result frame container
result_label = tk.Label(result_frame, text="", font=("Arial", 14))
result_label.pack()

# Function to Calculate Interest
def Calculate_Interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    result = (p * r * t) / 100
    result = round(result, 2)

    # Display the result in the result_label
    result_label.configure(text=f"Interest: {result} dollars")

# Bind the button with the function
calculate_button.configure(command=Calculate_Interest)

# Start the main loop
window.mainloop()
