import pygame
import numpy

class Life:
    def __init__(self, width = 1920, height = 1080, cell_size = 10, speed = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size, pygame.FULLSCREEN)
        self.x = self.height // self.cell_size
        self.y = self.width // self.cell_size
        self.speed = speed
        self.cells=[]

    def fill(self, randomize=False):
        if randomize:
            cells = numpy.random.randint(2, size=(self.x, self.y))
        else:
            cells = numpy.random.randint(1, size=(self.x, self.y))
        return cells   

    def tern(self, cells):
        nextcells = numpy.random.randint(1, size=(self.x, self.y))
        a = numpy.random.randint(1, size=(self.x+2, self.y+2))
        b = numpy.random.randint(1, size=(self.x+2, self.y+2))

        for x in range(0, self.x):
            for y in range(0, self.y):
                a[x+1,y+1] = cells[x,y]

        for x in range(1, self.x+1):
            for y in range(1, self.y+1):
                c = 0
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if not (i == x and j == y):
                            c = c + a[i,j]
                if a[x, y] == 0 and c == 3:
                    b[x, y] = 1
                elif(a[x,y] == 1 and c > 3) or (a[x,y] == 1 and c < 2):
                    b[x, y] = 0
                else:
                    b[x, y] = a[x, y]

        for x in range(0, self.x):
            for y in range(0, self.y):
                nextcells[x,y] = b[x+1,y+1]

        return(nextcells)

    def draw(self, cells):
        for x in range (self.x):
            for y in range (self.y):
                if cells[x,y] == 0:
                    # pygame.draw.rect(self.screen, pygame.Color('white'), ((y)*self.cell_size,(x)*self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.circle(self.screen, pygame.Color('black'), ((y)*self.cell_size+self.cell_size/2,(x)*self.cell_size+self.cell_size/2), self.cell_size/2)
                else:
                    # pygame.draw.rect(self.screen, pygame.Color('green'), ((y)*self.cell_size,(x)*self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.circle(self.screen, pygame.Color('green'), ((y)*self.cell_size+self.cell_size/2,(x)*self.cell_size+self.cell_size/2), self.cell_size/2)
    
    def draw_grid(self):
        for y in range(self.y):
            pygame.draw.line(self.screen, pygame.Color('blue'), (y*self.cell_size, 0), (y*self.cell_size, self.height))

        for x in range(self.x):
            pygame.draw.line(self.screen, pygame.Color('red'), (0, x*self.cell_size), (self.width, x*self.cell_size))

    
    def click(self, pos):
        self.cells[pos[1]//self.cell_size][pos[0]//self.cell_size] = 1

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Life')
        self.screen.fill(pygame.Color('black'))
        self.cells = self.fill(True)
        running = True
        while running:
            self.cells = self.tern(self.cells)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.click(pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            self.draw(self.cells)
            # self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

if __name__ == '__main__':
    game = Life()
    game.run()