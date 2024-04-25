import tkinter as tk

# Dictionary containing animal descriptions
animal_descriptions = {
    "Tiger": "The Bengal Tiger is the national animal of both India and Bangladesh. The tiger’s coat is yellow to light orange, with stripes ranging from dark brown to black. The number of tigers has reduced dramatically in the past few years, due to poaching and human-tiger conflict.",
    "Lion": "Asiatic Lion aka the Indian Lion or Persian Lion is a lion subspecies that is endangered. It differs from the African lion by less inflated auditory bullae, a larger tail tuft and a less developed mane.",
    "Blackbuck": "The Blackbuck is an ungulate species of antelope and it is near threatened. The main threat to this species is poaching, predation, habitat destruction, overgrazing, inbreeding and sanctuary visitors.",
    "Leopard": "The snow leopard is a large cat native to the mountain ranges in Central and South Asia. Snow leopards have long, thick fur, and their adaptations help them survive in harsh, cold environments. They are solitary animals and are known for their elusive nature, making them difficult to study in the wild."
}

# Function to display animal description
def display_description(animal):
    description_label.config(text=animal_descriptions.get(animal, "Description not found"))

# Create main window
root = tk.Tk()
root.title("Endangered Animals Description")
root.geometry("600x400")

# Set background color to green
root.configure(bg="green")

# Title label
title_label = tk.Label(root, text="Endangered Animals Description", font=("Helvetica", 16), bg="green", fg="white")
title_label.pack(pady=10)

# Label to display description
description_label = tk.Label(root, text="", wraplength=500, justify="left", bg="green", fg="white")
description_label.pack(pady=10)

# Frame to hold animal information
info_frame = tk.Frame(root, bg="green")
info_frame.pack(pady=10)

# Animal labels and descriptions
for animal, description in animal_descriptions.items():
    animal_label = tk.Label(info_frame, text=animal, font=("Helvetica", 12, "bold"), bg="green", fg="white")
    animal_label.grid(row=list(animal_descriptions.keys()).index(animal), column=0, padx=10, sticky="w")
    
    description_label = tk.Label(info_frame, text=description, wraplength=500, justify="left", bg="green", fg="white")
    description_label.grid(row=list(animal_descriptions.keys()).index(animal), column=1, padx=10, pady=5, sticky="w")

# Run the Tkinter event loop
root.mainloop()
