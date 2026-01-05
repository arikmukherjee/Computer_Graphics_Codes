import numpy as np
import matplotlib.pyplot as plt

# Define the grid size and colors
grid_size = (50, 50)
boundary_color = 5  # Black
fill_color = 0.8  # Gray
background_color = 6  # White

# Initialize the grid with the background color
grid = np.ones(grid_size) * background_color

# Function to plot the boundary
def plot_boundary():
    # Create a simple boundary for demonstration (e.g., a square)
    grid[10:40, 10] = boundary_color  # Left vertical line
    grid[10:40, 40] = boundary_color  # Right vertical line
    grid[10, 10:40] = boundary_color  # Top horizontal line
    grid[40, 10:40] = boundary_color  # Bottom horizontal line

# Simple boundary fill algorithm with 4-way connectivity
def boundary_fill(x, y, fill_color, boundary_color):
    # Check if the current pixel is within bounds and is neither boundary nor already filled
    if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
        return
    if grid[x, y] != boundary_color and grid[x, y] != fill_color:
        # Fill the current pixel
        grid[x, y] = fill_color
        # Recursively fill the surrounding pixels (4-way connectivity)
        boundary_fill(x+1, y, fill_color, boundary_color)
        boundary_fill(x-1, y, fill_color, boundary_color)
        boundary_fill(x, y+1, fill_color, boundary_color)
        boundary_fill(x, y-1, fill_color, boundary_color)

# Plot the boundary
plot_boundary()

# Starting point for the fill
start_x, start_y = 25, 25

# Apply the boundary fill algorithm
boundary_fill(start_x, start_y, fill_color, boundary_color)

# Plot the result
plt.imshow(grid, cmap='gray')
plt.title('Simple Boundary Fill Algorithm with 4-Way Connectivity')
plt.show()

