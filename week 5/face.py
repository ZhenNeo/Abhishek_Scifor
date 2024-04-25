import tkinter as tk

# Function to draw the face with different emotions
def draw_face(emotion):
    # Clear canvas
    canvas.delete("all")
    
    # Draw face
    face = canvas.create_oval(50, 50, 350, 350, fill="light blue")
    
    # Draw eyes
    if emotion == "happy":
        left_eye = canvas.create_oval(150, 150, 190, 190, fill="white")
        right_eye = canvas.create_oval(250, 150, 290, 190, fill="white")
    elif emotion == "cheeky":
        left_eye = canvas.create_oval(150, 150, 190, 170, fill="white")
        right_eye = canvas.create_oval(250, 150, 290, 170, fill="white")
    elif emotion == "sad":
        left_eye = canvas.create_oval(150, 170, 190, 190, fill="white")
        right_eye = canvas.create_oval(250, 170, 290, 190, fill="white")
    
    # Draw pupils
    if emotion == "happy" or emotion == "cheeky":
        left_pupil = canvas.create_oval(170, 170, 180, 180, fill="black")
        right_pupil = canvas.create_oval(270, 170, 280, 180, fill="black")
    elif emotion == "sad":
        left_pupil = canvas.create_oval(170, 180, 180, 190, fill="black")
        right_pupil = canvas.create_oval(270, 180, 280, 190, fill="black")
    
    # Draw mouth
    if emotion == "happy":
        mouth = canvas.create_arc(175, 250, 275, 300, start=0, extent=-180, style=tk.ARC)
    elif emotion == "cheeky":
        mouth = canvas.create_line(175, 300, 225, 280, 275, 300, smooth=True, width=2)
    elif emotion == "sad":
        mouth = canvas.create_arc(175, 300, 275, 250, start=0, extent=180, style=tk.ARC)

# Function to handle left click event
def change_emotion(event):
    global current_emotion_index
    current_emotion_index = (current_emotion_index + 1) % len(emotions)
    draw_face(emotions[current_emotion_index])

# Create the main window
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="blue")
canvas.pack()

# Define emotions and initialize current emotion index
emotions = ["happy", "cheeky", "sad"]
current_emotion_index = 0

# Draw the initial face
draw_face(emotions[current_emotion_index])

# Bind left click event to change emotion
canvas.bind("<Button-1>", change_emotion)

# Run the application
root.mainloop()
