#!/usr/bin/env python
# coding: utf-8

# # Investment method of valuation interface

# In[ ]:


import tkinter as tk
from tkinter import messagebox

def calculate_term_rent():
    try:
        i = float(entry_interest_rate_term.get())
        rent = float(entry_rent_term.get())
        n = int(entry_years_term.get())
        PV_PA = (1 - 1/(1 + i)**n) / i
        term_rent = PV_PA * rent
        return round(term_rent, 4)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Term Rent.")

def calculate_reversion():
    try:
        i = float(entry_interest_rate_reversion.get())
        rent = float(entry_rent_reversion.get())
        n = int(entry_years_reversion.get())
        Yp = 1 / (i * (1 + i)**n)
        reversion = Yp * rent
        return round(reversion, 4)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Reversion.")

def calculate_values():
    term_rent_value = calculate_term_rent()
    reversion_value = calculate_reversion()
    
    if term_rent_value is not None and reversion_value is not None:
        capital_value = term_rent_value + reversion_value
        messagebox.showinfo("Results", 
                            f"The value of the term rent is {term_rent_value}\n"
                            f"The value of the reversion is {reversion_value}\n"
                            f"The capital value of the property is {round(capital_value, 4)}")

def reset_fields():
    entry_interest_rate_term.delete(0, tk.END)
    entry_rent_term.delete(0, tk.END)
    entry_years_term.delete(0, tk.END)
    entry_interest_rate_reversion.delete(0, tk.END)
    entry_rent_reversion.delete(0, tk.END)
    entry_years_reversion.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Osunsanmi Hard Core and Layer Method")

# Term Rent Frame
frame_term = tk.Frame(root)
frame_term.pack(padx=10, pady=10)

tk.Label(frame_term, text="Term Rent Calculation").grid(row=0, columnspan=2)

tk.Label(frame_term, text="Interest Rate (e.g., 0.07):").grid(row=1, column=0)
entry_interest_rate_term = tk.Entry(frame_term)
entry_interest_rate_term.grid(row=1, column=1)

tk.Label(frame_term, text="Rent Amount:").grid(row=2, column=0)
entry_rent_term = tk.Entry(frame_term)
entry_rent_term.grid(row=2, column=1)

tk.Label(frame_term, text="Number of Years:").grid(row=3, column=0)
entry_years_term = tk.Entry(frame_term)
entry_years_term.grid(row=3, column=1)

# Reversion Frame
frame_reversion = tk.Frame(root)
frame_reversion.pack(padx=10, pady=10)

tk.Label(frame_reversion, text="Reversion Calculation").grid(row=0, columnspan=2)

tk.Label(frame_reversion, text="Interest Rate (e.g., 0.08):").grid(row=1, column=0)
entry_interest_rate_reversion = tk.Entry(frame_reversion)
entry_interest_rate_reversion.grid(row=1, column=1)

tk.Label(frame_reversion, text="Reversionary Rent Amount:").grid(row=2, column=0)
entry_rent_reversion = tk.Entry(frame_reversion)
entry_rent_reversion.grid(row=2, column=1)

tk.Label(frame_reversion, text="Number of Years:").grid(row=3, column=0)
entry_years_reversion = tk.Entry(frame_reversion)
entry_years_reversion.grid(row=3, column=1)

# Buttons
btn_calculate = tk.Button(root, text="Calculate Values", command=calculate_values)
btn_calculate.pack(pady=5)

btn_reset = tk.Button(root, text="Reset", command=reset_fields)
btn_reset.pack(pady=5)

# Run the application
root.mainloop()

