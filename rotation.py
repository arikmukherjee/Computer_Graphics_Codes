import matplotlib.pyplot as plt
import numpy as np

# Function to rotate a point around the origin (0, 0)
def rotate_point(x, y, angle):
    """
    Rotates a point (x, y) around the origin (0, 0) by the given angle.
    
    Parameters:
    x: x-coordinate of the point
    y: y-coordinate of the point
    angle: Rotation angle in degrees
    
    Returns:
    Tuple representing the rotated coordinates (x_rotated, y_rotated)
    """
    rad = np.radians(angle)
    x_rotated = x * np.cos(rad) - y * np.sin(rad)
    y_rotated = x * np.sin(rad) + y * np.cos(rad)
    return x_rotated, y_rotated

# Function to rotate an object defined by its vertices
def rotate_object(vertices, angle):
    """
    Rotates the object defined by its vertices around the origin (0, 0) by the given angle.
    
    Parameters:
    vertices: List of tuples representing the vertices of the object (x, y)
    angle: Rotation angle in degrees
    
    Returns:
    List of tuples representing the rotated vertices
    """
    return [rotate_point(x, y, angle) for x, y in vertices]

# Example object (rectangle) defined by its vertices
rectangle = [(1, 1), (1, 3), (3, 3), (3, 1)]

# Rotation angle
angle = 45

# Apply rotation to the object
rotated_rectangle = rotate_object(rectangle, angle)

# Function to plot an object
def plot_object(vertices, color, label):
    # Close the polygon by adding the first vertex at the end
    vertices.append(vertices[0])
    plt.plot(*zip(*vertices), color=color, label=label)

# Plot original rectangle
plot_object(rectangle.copy(), 'blue', 'Original Rectangle')

# Plot rotated rectangle
plot_object(rotated_rectangle.copy(), 'red', 'Rotated Rectangle')

# Plot settings
plt.title(f'2D Rotation by {angle} Degrees')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
