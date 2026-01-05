import numpy as np
import matplotlib.pyplot as plt

# Define the transformation matrices
def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotation_matrix(angle):
    rad = np.radians(angle)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])

# Function to apply transformation to an object
def apply_transformation(vertices, transformation_matrix):
    transformed_vertices = []
    for vertex in vertices:
        homogeneous_vertex = np.array([vertex[0], vertex[1], 1])
        transformed_vertex = transformation_matrix @ homogeneous_vertex
        transformed_vertices.append((transformed_vertex[0], transformed_vertex[1]))
    return transformed_vertices

# Example object (rectangle) defined by its vertices
rectangle = [(1, 1), (1, 3), (3, 3), (3, 1)]

# Define transformations
translation = translation_matrix(2, 3)
scaling = scaling_matrix(2, 1.5)
rotation = rotation_matrix(45)

# Apply transformations
translated_rectangle = apply_transformation(rectangle, translation)
scaled_rectangle = apply_transformation(rectangle, scaling)
rotated_rectangle = apply_transformation(rectangle, rotation)

# Function to plot an object
def plot_object(vertices, color, label):
    vertices.append(vertices[0])  # Close the polygon
    plt.plot(*zip(*vertices), color=color, label=label)

# Plot original rectangle
plot_object(rectangle.copy(), 'blue', 'Original Rectangle')

# Plot transformed rectangles
plot_object(translated_rectangle.copy(), 'green', 'Translated Rectangle')
plot_object(scaled_rectangle.copy(), 'purple', 'Scaled Rectangle')
plot_object(rotated_rectangle.copy(), 'red', 'Rotated Rectangle')

# Plot settings
plt.title('2D Transformations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
