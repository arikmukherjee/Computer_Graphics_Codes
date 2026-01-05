import matplotlib.pyplot as plt

# Define the region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define the clipping window
x_min, y_min = 100, 100
x_max, y_max = 300, 300

# Function to compute the region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < x_min:      # to the left of the clip window
        code |= LEFT
    elif x > x_max:    # to the right of the clip window
        code |= RIGHT
    if y < y_min:      # below the clip window
        code |= BOTTOM
    elif y > y_max:    # above the clip window
        code |= TOP
    return code

# Cohen-Sutherland line clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0.0, 0.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return x1, y1, x2, y2
    else:
        return None

# Plotting function
def plot_line(x1, y1, x2, y2, color='b'):
    plt.plot([x1, x2], [y1, y2], color)

# Main function to demonstrate line clipping
def main():
    lines = [
        (50, 150, 350, 150),
        (150, 50, 150, 350),
        (50, 50, 350, 350),
        (100, 100, 200, 200)
    ]

    plt.figure()

    # Draw the clipping window
    plot_line(x_min, y_min, x_max, y_min, 'k')
    plot_line(x_max, y_min, x_max, y_max, 'k')
    plot_line(x_max, y_max, x_min, y_max, 'k')
    plot_line(x_min, y_max, x_min, y_min, 'k')

    # Draw the original lines
    for line in lines:
        plot_line(line[0], line[1], line[2], line[3], 'r')

    # Clip and draw the lines
    for line in lines:
        clipped_line = cohen_sutherland_clip(*line)
        if clipped_line:
            plot_line(clipped_line[0], clipped_line[1], clipped_line[2], clipped_line[3], 'g')

    plt.title('Cohen-Sutherland Line Clipping Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.xlim(0, 400)
    plt.ylim(0, 400)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == '__main__':
    main()
