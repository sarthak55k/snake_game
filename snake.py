import random
import curses

s = curses.initscr()                #initialise screen
curses.curs_set(0)                  #cursor invisible
sh, sw = s.getmaxyx()               #width and height of screen
w = curses.newwin(sh, sw, 0, 0)     #starting point of screen
w.keypad(1)
w.timeout(100)                      #refresh

snk_x = sw/4                        #initial position of snake
snk_y = sh/2
snake = [
    [snk_y,snk_x],
    [snk_y,snk_x -1],
    [snk_y,snk_x -2],
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)                     #Paint character ch at (y, x) with attributes attr

key = curses.KEY_RIGHT                #initially curses going right

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key         #direction in which cursur will move


    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]] 


    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0,new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1,sh-1),
                random.randint(1,sw-1)
            ]

            food = nf if nf not in snake else None

        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
    
    w.addch(snake[0][0],snake[0][1], curses.ACS_CKBOARD)





    

     



