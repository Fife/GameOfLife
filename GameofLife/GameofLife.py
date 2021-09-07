import sys, pygame
from CellFunctions import * 

# Drawing Rectangle

def draw_board(board):
    find_neighbors(board)
    for y in range(len(board)):
        for x in range(len(board)):
            if(board[y][x].status):
                pygame.draw.rect(screen, color, pygame.Rect(x*50, y*50, 50, 50))
                textsurface = myfont.render(str(board[y][x].num_neighbors), False, (0, 0, 0))
                screen.blit(textsurface,((x*50)+20,(y*50)+20))
            else:
                pygame.draw.rect(screen, color, pygame.Rect(x*50, y*50, 50, 50), 1)
                textsurface = myfont.render(str(board[y][x].num_neighbors), False, (255, 255, 255))
                screen.blit(textsurface,((x*50)+20,(y*50)+20))
        pygame.display.flip()


#Window Parameters
RES_X = 640
RES_Y = 640

#World Parameters
WORLD_LEN= 14


pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 10)
screen = pygame.display.set_mode((RES_X, RES_Y))
board = gen_world(WORLD_LEN)

# Initialing Color
color = (255,255,255)

draw_board(board)

pygame.display.set_caption("Conway's Game of Life")
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                pos_x = clamp(int(pos_x/50), 0, WORLD_LEN-1)
                pos_y = clamp(int(pos_y/50), 0, WORLD_LEN-1)
                print(pos_x, pos_y)
                board[pos_y][pos_x].status = not board[pos_y][pos_x].status
                find_neighbors(board)
                screen.fill((0,0,0))
                draw_board(board)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    board = next_board(board)
                    screen.fill((0,0,0))
                    draw_board(board)
                if event.key == pygame.K_LEFT:
                    board = gen_world(WORLD_LEN)
                    screen.fill((0,0,0))
                    draw_board(board)
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    board = gen_blank_world(WORLD_LEN)
                    screen.fill((0,0,0))
                    find_neighbors(board)
                    draw_board(board)
                    pygame.display.flip()

    pygame.quit()
except SystemExit:
    pygame.quit()