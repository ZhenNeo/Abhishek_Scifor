import tkinter as tk
from tkinter import simpledialog

class MiniPaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Paint")
        
        # Initialize drawing variables
        self.pen_color = "black"
        self.pen_size = 2
        self.tool = "pen"  # Default tool
        
        # Create Canvas widget for drawing
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        # Create buttons
        self.pen_button = tk.Button(self.button_frame, text="Pen", command=lambda: self.select_tool("pen"))
        self.pen_button.pack(side=tk.LEFT, padx=5)
        
        self.brush_button = tk.Button(self.button_frame, text="Brush", command=lambda: self.select_tool("brush"))
        self.brush_button.pack(side=tk.LEFT, padx=5)
        
        self.color_button = tk.Button(self.button_frame, text="Color", command=self.select_color)
        self.color_button.pack(side=tk.LEFT, padx=5)
        
        self.eraser_button = tk.Button(self.button_frame, text="Eraser", command=lambda: self.select_tool("eraser"))
        self.eraser_button.pack(side=tk.LEFT, padx=5)
        
        self.size_label = tk.Label(self.button_frame, text="Size:")
        self.size_label.pack(side=tk.LEFT, padx=5)
        
        self.size_scale = tk.Scale(self.button_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_scale.pack(side=tk.LEFT, padx=5)
        
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        if self.tool == "pen":
            self.canvas.create_line(event.x, event.y, event.x, event.y, fill=self.pen_color, width=self.pen_size, capstyle=tk.ROUND, smooth=True)
        elif self.tool == "brush":
            self.canvas.create_oval(event.x-self.pen_size, event.y-self.pen_size, event.x+self.pen_size, event.y+self.pen_size, fill=self.pen_color, outline="")
        elif self.tool == "eraser":
            self.canvas.create_rectangle(event.x-self.pen_size, event.y-self.pen_size, event.x+self.pen_size, event.y+self.pen_size, fill="white", outline="")

    def select_tool(self, tool):
        self.tool = tool
    
    def select_color(self):
        # Create dialog window
        self.color_dialog = tk.Toplevel(self.root)
        self.color_dialog.title("Choose Color")
        
        # Create entry widgets for RGB values
        self.r_label = tk.Label(self.color_dialog, text="R:")
        self.r_label.grid(row=0, column=0)
        self.r_entry = tk.Entry(self.color_dialog, width=5)
        self.r_entry.grid(row=0, column=1)
        
        self.g_label = tk.Label(self.color_dialog, text="G:")
        self.g_label.grid(row=0, column=2)
        self.g_entry = tk.Entry(self.color_dialog, width=5)
        self.g_entry.grid(row=0, column=3)
        
        self.b_label = tk.Label(self.color_dialog, text="B:")
        self.b_label.grid(row=0, column=4)
        self.b_entry = tk.Entry(self.color_dialog, width=5)
        self.b_entry.grid(row=0, column=5)
        
        # Create button to confirm color selection
        self.confirm_button = tk.Button(self.color_dialog, text="Confirm", command=self.confirm_color)
        self.confirm_button.grid(row=1, columnspan=6, pady=5)

    def confirm_color(self):
        # Get RGB values from entry widgets
        r = int(self.r_entry.get())
        g = int(self.g_entry.get())
        b = int(self.b_entry.get())
        
        # Convert RGB values to hexadecimal color code
        self.pen_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        
        # Close color selection dialog
        self.color_dialog.destroy()

    def change_size(self, size):
        self.pen_size = int(size)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniPaintApp(root)
    root.mainloop()
