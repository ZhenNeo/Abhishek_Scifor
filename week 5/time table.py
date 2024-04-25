import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Time Table")

# Define the table
table = tk.Frame(root)
table.pack()

# Define the rows and columns
rows = 7
columns = 7

# Define the data
data = [
    ["TIME TABLE", "", "", "", "", "", ""],
    ["", "BATCH A", "BATCH B", "BATCH C", "BATCH D", "BATCH E", ""],
    ["10.00 AM - 1:00PM", "FY HAP-I/RCS", "FY HDT/RKJ", "FY PCOL-I/AJS", "FY POC-I/SAG", "FY BIOCHEM/PSA", ""],
    ["", "SY PCOG-NGS", "SY LUNCH BREAK", "SY PCOL-II/M", "SY PCOL-IIIM/M", "SY PP-II/VAS", ""],
    ["", "TY MC-III/GRB", "", "", "", "", ""],
    ["1:40PM - 2:40PM", "DIV A FY BIOCHEM/ALW", "DIV B FY HAP-II/BHG", "QA/AAJ FINAL AIT/SSP", "QA/KRD FINAL PM/SJA", "", ""],
    ["", "SY PP-II/SS", "FE/PP TY", "", "", "", ""],
]

# Add the data to the table
for i in range(rows):
    for j in range(columns):
        cell = tk.Label(table, text=data[i][j], relief="solid", width=20)
        cell.grid(row=i, column=j)

# Run the window
root.mainloop()