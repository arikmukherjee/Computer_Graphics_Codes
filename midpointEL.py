import matplotlib.pyplot as plt

def draw_ellipse(x_center, y_center, a, b):
    # Function to plot points
    def plot_points(x, y):
        plt.plot(x_center + x, y_center + y, 'bo')
        plt.plot(x_center - x, y_center + y, 'bo')
        plt.plot(x_center + x, y_center - y, 'bo')
        plt.plot(x_center - x, y_center - y, 'bo')
    
    # Region 1
    x = 0
    y = b
    a2 = a**2
    b2 = b**2
    d1 = b2 - a2 * b + 0.25 * a2
    
    dx = 2 * b2 * x
    dy = 2 * a2 * y
    
    # Initial points in Region 1
    plot_points(x, y)
    
    while dx < dy:
        x += 1
        dx += 2 * b2
        if d1 < 0:
            d1 += b2 + dx
        else:
            y -= 1
            dy -= 2 * a2
            d1 += dx - dy + b2
        plot_points(x, y)
    
    # Region 2
    d2 = b2 * (x + 0.5)**2 + a2 * (y - 1)**2 - a2 * b2
    
    while y > 0:
        y -= 1
        dy -= 2 * a2
        if d2 > 0:
            d2 += a2 - dy
        else:
            x += 1
            dx += 2 * b2
            d2 += dx - dy + a2
        plot_points(x, y)

# Set the ellipse parameters
x_center = 0
y_center = 0
a = 100
b = 50

# Draw the ellipse
draw_ellipse(x_center, y_center, a, b)

# Display the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Midpoint Ellipse Drawing')
plt.show()
