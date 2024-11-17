import tkinter as tk
import random

# Configuration
CELL_SIZE = 20  # Taille des cellules
GRID_WIDTH = 30  # Nombre de colonnes
GRID_HEIGHT = 20  # Nombre de lignes
UPDATE_SPEED = 200  # Temps entre mises à jour (ms)

class GameOfLife:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        # Interface
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.random_button = tk.Button(root, text="Random", command=self.randomize)
        self.random_button.pack(side=tk.LEFT, padx=5)

        # Bind clicks for setting cells
        self.canvas.bind("<Button-1>", self.toggle_cell)

    def toggle_cell(self, event):
        x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
        self.grid[y][x] = 1 if self.grid[y][x] == 0 else 0
        self.draw_grid()

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.draw_grid()

    def randomize(self):
        self.running = False
        self.grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.draw_grid()

    def update(self):
        if self.running:
            self.grid = self.next_generation()
            self.draw_grid()
            self.root.after(UPDATE_SPEED, self.update)

    def draw_grid(self):
        self.canvas.delete("all")
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = "black" if self.grid[y][x] == 1 else "white"
                self.canvas.create_rectangle(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    (x + 1) * CELL_SIZE,
                    (y + 1) * CELL_SIZE,
                    fill=color,
                    outline="gray"
                )

    def next_generation(self):
        new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.grid[y][x] == 1 and alive_neighbors in [2, 3]:
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and alive_neighbors == 3:
                    new_grid[y][x] = 1
        return new_grid

    def count_alive_neighbors(self, x, y):
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                count += self.grid[ny][nx]
        return count


# Lancer le jeu
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Jeu de la Vie - Version Interactive")
    game = GameOfLife(root)
    root.mainloop()
