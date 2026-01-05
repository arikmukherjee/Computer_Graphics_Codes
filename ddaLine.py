import matplotlib.pyplot as plt

def dda_line(x0, y0, x1, y1):
    points = []

    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0
    points.append((round(x), round(y)))

    for _ in range(int(steps)):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

def plot_line(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, marker='o', color='red')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()

# Example usage
x0, y0 = 2, 3
x1, y1 = 500, 168
points = dda_line(x0, y0, x1, y1)
plot_line(points)
