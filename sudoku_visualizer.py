import pygame
import sudoku_solver

pygame.init()

WIDTH, HEIGHT = 360, 360
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

FPS = 10
pygame.font.init()

cubes = []

def draw_window():

    # Grid
    window.fill(WHITE)
    for counter in range(0,400,40):
        pygame.draw.line(window, BLACK, (0,counter), (360,counter))
        pygame.draw.line(window, BLACK, (counter,0), (counter,360))

    for counter in range(120,400,120):
        pygame.draw.line(window, BLACK, (0,counter), (360,counter), width=3)
        pygame.draw.line(window, BLACK, (counter,0), (counter,360), width=3)
    
    # Display last array
    last_array = sudoku.sudoku_array[len(sudoku.sudoku_array)-1][1]

    for row in range(9):
        for value in range(9):
            num = last_array[row][value]
            if num != 0:
                number = pygame.font.Font.render(pygame.font.SysFont("comic sans", 22, True), str(num), True, BLACK)
                window.blit(number,(14+40*value,4+40*row))

    for i in cubes:
        if i[1]:
            pygame.draw.rect(window, GREEN, i[0], width=5)
        else: 
            pygame.draw.rect(window, RED, i[0], width=5)

    pygame.display.update()


def update_cube(value_green): # green = [coords, bool_if_green]
    (x,y) = value_green[0]
    start_coords = (40*x, 40*y, 40, 40)
    
    global cubes
    cubes.append([start_coords, value_green[1]])


def main(sudoku):

    clock = pygame.time.Clock() # Controlls frames per second (1/2)
    run = True
    solving = False

    while run:
        clock.tick(FPS) # Controlls frames per second (2/2)
        # Check if user closed window to end execution ("X" button on window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Start solver
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            solving = True   
        
        # Q to quit
        if keys_pressed[pygame.K_q]:
            run = False

        if solving:
            value_green = sudoku.solve()
            update_cube(value_green)

        # Check end game
        if not sudoku.check_zero():
            solving = False
            global cubes
            cubes = []

        draw_window()
                
    pygame.quit()

# Game1 
preset1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solution1 = [
    [7,8,5,4,3,9,1,2,6],
    [6,1,2,8,7,5,3,4,9],
    [4,9,3,6,2,1,5,7,8],
    [8,5,7,9,4,3,2,6,1],
    [2,6,1,7,5,8,9,3,4],
    [9,3,4,1,6,2,7,8,5],
    [5,7,8,3,9,4,6,1,2],
    [1,2,6,5,8,7,4,9,3],
    [3,4,9,2,1,6,8,5,7]
]
game1 = [preset1, solution1]

# Game2 
preset2 = [
    [9,0,0,4,2,0,6,0,3],
    [6,0,0,0,0,3,0,0,0],
    [7,0,2,0,8,0,0,4,0],
    [0,0,8,0,0,0,0,0,0],
    [0,5,9,0,0,0,3,2,0],
    [0,0,0,0,0,0,4,0,0],
    [0,9,0,0,3,0,8,0,7],
    [0,0,0,6,0,0,0,0,5],
    [2,0,7,0,1,8,0,0,4]
]

solution2 = [
    [9,1,5,4,2,7,6,8,3],
    [6,8,4,9,5,3,1,7,2],
    [7,3,2,1,8,6,5,4,9],
    [1,2,8,3,4,5,7,9,6],
    [4,5,9,7,6,1,3,2,8],
    [3,7,6,8,9,2,4,5,1],
    [5,9,1,2,3,4,8,6,7],
    [8,4,3,6,7,9,2,1,5],
    [2,6,7,5,1,8,9,3,4]
]
game2 = [preset2, solution2]

# Game3 
preset3 = [
    [2,0,0,9,0,4,6,0,0],
    [0,0,0,0,6,0,1,0,3],
    [0,0,9,0,0,3,0,0,0],
    [0,0,0,0,0,2,0,7,5],
    [0,0,5,0,0,0,2,0,0],
    [1,9,0,4,0,0,0,0,0],
    [0,0,0,6,0,0,5,0,0],
    [8,0,4,0,2,0,0,0,0],
    [0,0,3,7,0,8,0,0,2]
]

solution3 = [
    [2,3,1,9,8,4,6,5,7],
    [5,4,8,2,6,7,1,9,3],
    [7,6,9,5,1,3,8,2,4],
    [3,8,6,1,9,2,4,7,5],
    [4,7,5,8,3,6,2,1,9],
    [1,9,2,4,7,5,3,8,6],
    [9,2,7,6,4,1,5,3,8],
    [8,5,4,3,2,9,7,6,1],
    [6,1,3,7,5,8,9,4,2]
]
game3 = [preset3, solution3]

# Start
sudoku = sudoku_solver.Game(game1)
main(sudoku)
