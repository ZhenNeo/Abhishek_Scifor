import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        self.canvas_width = 400
        self.canvas_height = 400
        self.block_size = 20
        self.score = 0
        
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        
        self.snake = [(self.canvas_width/2, self.canvas_height/2)]
        self.snake_direction = "Right"
        
        self.food = None
        self.game_over_msg = None
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()
        
        self.root.bind("<KeyPress>", self.change_direction)
        
        self.game_running = False
    
    def start_game(self):
        self.game_running = True
        self.start_button.config(state=tk.DISABLED)
        self.score = 0
        self.snake = [(self.canvas_width/2, self.canvas_height/2)]
        self.snake_direction = "Right"
        self.canvas.delete("food")
        self.generate_food()
        self.game_loop()
    
    def generate_food(self):
        if self.food:
            self.canvas.delete("food")
        
        x = random.randint(0, (self.canvas_width - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.canvas_height - self.block_size) // self.block_size) * self.block_size
        
        self.food = (x, y)
        self.canvas.create_oval(x, y, x+self.block_size, y+self.block_size, fill="red", tag="food")
        
        # Schedule the disappearance of the food after 5 seconds
        self.root.after(5000, self.check_food)
    
    def check_food(self):
        if not self.game_running:
            return
        
        if not self.food:
            self.generate_food()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        
        if self.snake_direction == "Up":
            head_y -= self.block_size
        elif self.snake_direction == "Down":
            head_y += self.block_size
        elif self.snake_direction == "Left":
            head_x -= self.block_size
        elif self.snake_direction == "Right":
            head_x += self.block_size
        
        self.snake.insert(0, (head_x, head_y))
        
        if (head_x, head_y) == self.food:
            self.score += 10
            self.generate_food()
        else:
            self.canvas.delete("snake_tail")
            self.snake.pop()
        
        self.draw_snake()
    
    def draw_snake(self):
        self.canvas.delete("snake")
        
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+self.block_size, y+self.block_size, fill="green", tag="snake")
        
        self.canvas.create_text(10, 10, text=f"Score: {self.score}", fill="white", anchor="nw", tag="score")
    
    def check_collisions(self):
        head_x, head_y = self.snake[0]
        
        if head_x < 0 or head_x >= self.canvas_width or head_y < 0 or head_y >= self.canvas_height:
            return True
        
        if len(self.snake) != len(set(self.snake)):
            return True
        
        return False
    
    def game_loop(self):
        if not self.game_running:
            return
        
        if self.check_collisions():
            self.game_over()
            return
            
        self.move_snake()
        self.root.after(150, self.game_loop)
    
    def change_direction(self, event):
        if not self.game_running:
            return
        
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            if (key == "Up" and self.snake_direction != "Down") or \
               (key == "Down" and self.snake_direction != "Up") or \
               (key == "Left" and self.snake_direction != "Right") or \
               (key == "Right" and self.snake_direction != "Left"):
                self.snake_direction = key
    
    def game_over(self):
        self.game_running = False
        self.start_button.config(state=tk.NORMAL)
        if self.game_over_msg:
            self.canvas.delete(self.game_over_msg)
        self.game_over_msg = self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, text=f"Game Over! Score: {self.score}", fill="white", font=("Arial", 20), anchor="center")
        self.canvas.create_text(self.canvas_width/2, self.canvas_height/2 + 30, text="Press Start to play again", fill="white", font=("Arial", 12), anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
