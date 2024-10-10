import pygame
import numpy as np

pygame.init()

window_width = 650
window_height = 550
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mandelbrot Set")
display_surface.fill((0, 0, 0))

fps = 60
clock = pygame.time.Clock()

# Variables for the Mandelbrot calculation
real_width = 650
real_height = 550
zoom_level = 1.0
center_x = 0.0
center_y = 0.0


# Colormap for coloring the Mandelbrot set
def colormap(iteration, max_iteration):
    # Create a neon color scheme
    r = min(abs(int(255 * np.sin(0.1 * iteration))), 255)
    g = min(abs(int(255 * np.sin(0.2 * iteration))), 255)
    b = min(abs(int(255 * np.sin(0.3 * iteration))), 255)
    return (r, g, b)


def calc_mandelbrot(xi, yi, width, height):
    for x0 in range(xi, width):
        for y0 in range(yi, height):
            x, y = 0, 0
            iteration = 0
            max_iteration = 255
            while (x * x) + (y * y) <= 2 and iteration < max_iteration:
                temp = (x * x) - (y * y) + ((x0 - real_width / 2) / (200 * zoom_level) + center_x)
                y = (2 * x * y) + ((real_height / 2 - y0) / (200 * zoom_level) + center_y)
                x = temp
                iteration += 1

            col = colormap(iteration, max_iteration)
            # print(col)
            pygame.draw.circle(display_surface, col, (x0, y0), 1)


def zoom(x_mouse, y_mouse):
    global center_x, center_y, zoom_level
    center_x = (x_mouse - real_width / 2) / (200 * zoom_level) + center_x
    center_y = (real_height / 2 - y_mouse) / (200 * zoom_level) + center_y
    zoom_level *= 4  # You can adjust the zoom factor as needed
    calc_mandelbrot(0, 0, real_width, real_height)


running = True
calc_mandelbrot(0, 0, real_width, real_height)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                xm, ym = event.pos
                zoom(xm, ym)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()