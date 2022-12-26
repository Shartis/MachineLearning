import numpy as np
import pygame

class Point:
    def __init__(self, x, y, color='black', cluster=None):
        self.x = x
        self.y = y
        self.color = color
        self.cluster = cluster

    @property
    def pos(self):
        return self.x, self.y

    def dist(self, point):
        return np.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def __str__(self, x, y):
        return f"x: {self.x}, y: {self.y}"

    def draw(self, screen):
        pygame.draw.circle(screen, self.cluster, (self.x, self.y), 10)

def calc_neighbors(points, point, eps):
    neighbors = []
    for i in range(len(points)):
        if point.dist(points[i]) < eps:
            neighbors.append(i)
    return neighbors

def mark(points):
    local_points = list(points)
    eps = 100
    minPts = 3
    colorNumber = 0
    clr = ['black', 'green', 'yellow', 'pink', 'cyan', 'purple', 'orange', 'grey']
    for i in range(len(local_points)):
        if local_points[i].cluster is not None:
            continue
        neighbors = calc_neighbors(local_points, local_points[i], eps)
        if len(neighbors) < minPts:
            local_points[i].cluster = clr[0]
            continue
        local_points[i].cluster = clr[colorNumber + 1]
        z = 0
        while z < len(neighbors):
            iN = neighbors[z]
            if local_points[iN].cluster == clr[0]:
                local_points[iN].cluster = clr[colorNumber + 1]
            if local_points[iN].cluster is not None:
                z += 1
                continue
            local_points[iN].cluster = clr[colorNumber + 1]
            new_neighbors = calc_neighbors(local_points, local_points[iN], eps)
            if len(new_neighbors) >= minPts:
                for neighbor in new_neighbors:
                    if neighbor not in neighbors:
                        neighbors.append(neighbor)
            z += 1
        colorNumber += 1
    return local_points


def random_point(n):
    points = []
    for i in range(n):
        points.append(Point(np.random.randint(1, 100), np.random.randint(1, 100)))
    return points
n = 40

def draw():
    R = 10
    points = []
    pygame.init()
    new_points = []
    screen = pygame.display.set_mode([800, 600])
    screen.fill(color='white')
    pygame.display.update()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.draw.circle(screen, color='black', center=event.pos, radius=R)
                pnt = Point(event.pos[0], event.pos[1])
                points.append(pnt)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_points = mark(points)
                for point in new_points:
                    point.draw(screen)
                for point in points:
                    point.cluster = None
            pygame.display.update()

if __name__ == '__main__':
    draw()