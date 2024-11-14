import tkinter as tk

class PingPongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kelvin K Ping Pong Game")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Game Variables
        self.ball_x = 290
        self.ball_y = 190
        self.ball_dx = 2
        self.ball_dy = 2
        self.left_paddle_y = 150
        self.right_paddle_y = 150
        self.left_score = 0
        self.right_score = 0

        # Canvas Setup
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="#2E2E2E")
        self.canvas.pack()

        # Draw paddles and ball with colors
        self.left_paddle = self.canvas.create_rectangle(20, self.left_paddle_y, 40, self.left_paddle_y + 60, fill="#FF6347")  # Tomato red
        self.right_paddle = self.canvas.create_rectangle(560, self.right_paddle_y, 580, self.right_paddle_y + 60, fill="#4682B4")  # Steel blue
        self.ball = self.canvas.create_oval(self.ball_x, self.ball_y, self.ball_x + 10, self.ball_y + 10, fill="#FFD700")  # Gold color

        # Score Display with brighter text
        self.score_label = tk.Label(self.root, text="Left: 0  Right: 0", font=("Helvetica", 16), fg="#32CD32", bg="#2E2E2E")  # Lime green text
        self.score_label.pack()

        # Author Label
        self.author_label = tk.Label(self.root, text="Author: KELVIN K", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E")  # White text
        self.author_label.pack(side=tk.BOTTOM)

        # Bind keys for paddle movement
        self.root.bind("<w>", self.move_left_up)
        self.root.bind("<s>", self.move_left_down)
        self.root.bind("<Up>", self.move_right_up)
        self.root.bind("<Down>", self.move_right_down)

        # Start the game
        self.update_game()

    def move_left_up(self, event):
        if self.left_paddle_y > 0:
            self.left_paddle_y -= 20
            self.canvas.coords(self.left_paddle, 20, self.left_paddle_y, 40, self.left_paddle_y + 60)

    def move_left_down(self, event):
        if self.left_paddle_y < 340:
            self.left_paddle_y += 20
            self.canvas.coords(self.left_paddle, 20, self.left_paddle_y, 40, self.left_paddle_y + 60)

    def move_right_up(self, event):
        if self.right_paddle_y > 0:
            self.right_paddle_y -= 20
            self.canvas.coords(self.right_paddle, 560, self.right_paddle_y, 580, self.right_paddle_y + 60)

    def move_right_down(self, event):
        if self.right_paddle_y < 340:
            self.right_paddle_y += 20
            self.canvas.coords(self.right_paddle, 560, self.right_paddle_y, 580, self.right_paddle_y + 60)

    def update_game(self):
        # Move the ball
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Ball collision with top and bottom
        if self.ball_y <= 0 or self.ball_y >= 390:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddles
        if self.ball_x <= 40 and self.left_paddle_y <= self.ball_y <= self.left_paddle_y + 60:
            self.ball_dx = -self.ball_dx
        elif self.ball_x >= 550 and self.right_paddle_y <= self.ball_y <= self.right_paddle_y + 60:
            self.ball_dx = -self.ball_dx

        # Ball goes out of bounds
        if self.ball_x <= 0:
            self.right_score += 1
            self.reset_ball()
        elif self.ball_x >= 590:
            self.left_score += 1
            self.reset_ball()

        # Update score display with a colorful score
        self.score_label.config(text=f"Left: {self.left_score}  Right: {self.right_score}")

        # Continue updating the game
        self.canvas.coords(self.ball, self.ball_x, self.ball_y, self.ball_x + 10, self.ball_y + 10)
        self.root.after(10, self.update_game)

    def reset_ball(self):
        self.ball_x = 290
        self.ball_y = 190
        self.ball_dx = -self.ball_dx
        self.ball_dy = 2


if __name__ == "__main__":
    root = tk.Tk()
    game = PingPongGame(root)
    root.mainloop()
