import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    x, y = x0, y0
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points

def plot_line(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, marker='o',color='green')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()

# Example usage
x0, y0 = 2, 3
x1, y1 = 500, 160
points = bresenham_line(x0, y0, x1, y1)
plot_line(points)
