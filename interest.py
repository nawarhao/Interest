import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get user inputs
        p = float(principle_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest
        ci = p * ((1 + (r / 100)) ** t) - p

        # Display results
        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}", fg="white", bg="#4CAF50")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values!")

# Create main window
root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")  # As per instruction

# Labels and Entries
tk.Label(root, text="Principle Amount:", bg="#e1f5fe").grid(row=0, column=0, padx=10, pady=10, sticky="w")
principle_entry = tk.Entry(root)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time (years):", bg="#e1f5fe").grid(row=1, column=0, padx=10, pady=10, sticky="w")
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate of Interest (%):", bg="#e1f5fe").grid(row=2, column=0, padx=10, pady=10, sticky="w")
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate Interest", command=calculate_interest, bg="#2196F3", fg="white")
calc_btn.grid(row=3, columnspan=2, pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e1f5fe")
result_label.grid(row=4, columnspan=2, pady=20)

# Set background color
root.configure(bg="#e1f5fe")

# Run the window
root.mainloop()
