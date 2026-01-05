import matplotlib.pyplot as plt

def midpoint_circle(cx, cy, radius):
    points = []

    x = radius
    y = 0
    p = 1 - radius

    def plot_circle_points(cx, cy, x, y):
        points.extend([
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x)
        ])

    plot_circle_points(cx, cy, x, y)

    while x > y:
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * y - 2 * x + 1
        plot_circle_points(cx, cy, x, y)

    return points

def plot_circle(points):
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords)
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
cx, cy = 50, 50
radius = 30
points = midpoint_circle(cx, cy, radius)
plot_circle(points)
