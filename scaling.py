import matplotlib.pyplot as plt

# Function to scale an object
def scale_object(vertices, sx, sy):
    
    scaled_vertices = [(x * sx, y * sy) for x, y in vertices]
    return scaled_vertices

# Example object (rectangle) defined by its vertices
rectangle = [(1, 1), (1, 3), (3, 3), (3, 1)]

# Scaling factors
sx, sy = 2, 1.5

# Apply scaling to the object
scaled_rectangle = scale_object(rectangle, sx, sy)

# Function to plot an object
def plot_object(vertices, color, label):
    # Close the polygon by adding the first vertex at the end
    vertices.append(vertices[0])
    plt.plot(*zip(*vertices), color=color, label=label)

# Plot original rectangle
plot_object(rectangle.copy(), 'blue', 'Original Rectangle')

# Plot scaled rectangle
plot_object(scaled_rectangle.copy(), 'red', 'Scaled Rectangle')

# Plot settings
plt.title('Object Scaling in 2D')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
