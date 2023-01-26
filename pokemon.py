import pygame as pg
import random as rand

def option_generator():
    placement = rand.randint(1,4)
    return placement

def option_placement(choice, an_answer):
    if choice == 1:
        which_box = screen.blit(an_answer, (90, 385))
    elif choice == 2:
        which_box = screen.blit(an_answer, (490, 385))
    elif choice == 3:
        which_box = screen.blit(an_answer, (90, 585))
    else:
        which_box = screen.blit(an_answer, (490, 585))
    return which_box

def correct_box(right_answer):
    if right_answer == 1:
        right_box = tl_option
    elif right_answer == 2:
        right_box = tr_option
    elif right_answer == 3:
        right_box = bl_option
    else:
        right_box = br_option
    return right_box 

def after_guess():
    screen.fill(bg_color)
    tl_option = pg.draw.rect(screen, (255,255,255), [50, 350, 200, 100], 100) #top left answer
    tr_option = pg.draw.rect(screen, (255,255,255), [450, 350, 200, 100], 100) #top right answer
    bl_option = pg.draw.rect(screen, (255,255,255), [50, 550, 200, 100], 100) #bottom left answer
    br_option = pg.draw.rect(screen, (255,255,255), [450, 550, 200, 100], 100) #bottom right answer
    imp = pg.image.load(pokemon_images[td])
    score_text = my_font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (500, 0))
    screen.blit(imp, (0,0))
    for x in range(1,5):
        #option = my_font.render(name_number[x-1], True, (0,0,0))
        option = my_font.render(nn[x-1], True, (0,0,0))
        option_placement(x, option)
    pg.display.update()

def updated_screen():
    pg.time.delay(1500)
    screen.fill(bg_color)
    pg.draw.rect(screen, (255,255,255), [50, 350, 200, 100], 100) #top left answer
    pg.draw.rect(screen, (255,255,255), [450, 350, 200, 100], 100) #top right answer
    pg.draw.rect(screen, (255,255,255), [50, 550, 200, 100], 100) #bottom left answer
    pg.draw.rect(screen, (255,255,255), [450, 550, 200, 100], 100) #bottom right answer
    score_text = my_font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (500, 0))
    pg.display.update()

def game_over():
    screen.fill(bg_color)
    game_over_font = pg.font.SysFont('Times New Roman', 60, bold=True)
    game_over_text = game_over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over_text, (175, 350))
    pg.display.update()

def play_again():
    pg.time.delay(1500)
    screen.fill(bg_color)
    play_again_button = pg.draw.rect(screen, (255,255,255), [50, 350, 200, 100], 100)
    quit_button = pg.draw.rect(screen, (255,255,255), [450, 350, 200, 100], 100)
    play_again_text = my_font.render("Play Again?", True, (0,0,0))
    quit_text = my_font.render("Quit", True, (0,0,0))
    screen.blit(play_again_text, (80, 385))
    screen.blit(quit_text, (525, 385))
    pg.display.update()
    selecting = True
    while selecting:
        screen.fill(bg_color)
        play_again_button = pg.draw.rect(screen, (255,255,255), [50, 350, 200, 100], 100)
        quit_button = pg.draw.rect(screen, (255,255,255), [450, 350, 200, 100], 100)
        play_again_text = my_font.render("Play Again?", True, (0,0,0))
        quit_text = my_font.render("Quit", True, (0,0,0))
        screen.blit(play_again_text, (80, 385))
        screen.blit(quit_text, (525, 385))
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                if play_again_button.collidepoint(pg.mouse.get_pos()):
                    return True
                elif quit_button.collidepoint(pg.mouse.get_pos()):
                    return False
        
bg_color = (255,0,0)
screen = pg.display.set_mode((700, 700))
pg.display.set_caption("WHO'S THAT POKEMON?")
screen.fill(bg_color)
pg.display.flip()

pg.font.init()
score = 0
my_font = pg.font.SysFont('Times New Roman', 30)
score_text = my_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (500, 0))

tl_option = pg.draw.rect(screen, (255,255,255), [50, 350, 200, 100], 100) #top left answer
tr_option = pg.draw.rect(screen, (255,255,255), [450, 350, 200, 100], 100) #top right answer
bl_option = pg.draw.rect(screen, (255,255,255), [50, 550, 200, 100], 100) #bottom left answer
br_option = pg.draw.rect(screen, (255,255,255), [450, 550, 200, 100], 100) #bottom right answer

pokemon_images = {
1: "Whos_That_Pokemon-main\Pokemon Images\Bulbasaur.png", 2: "Whos_That_Pokemon-main\Pokemon Images\Ivysaur.png",
3: "Whos_That_Pokemon-main\Pokemon Images\Venusaur.png", 4: "Whos_That_Pokemon-main\Pokemon Images\Charmander.png",
5: "Whos_That_Pokemon-main\Pokemon Images\Charmeleon.png", 6: "Whos_That_Pokemon-main\Pokemon Images\Charizard.png",
7: "Whos_That_Pokemon-main\Pokemon Images\Squirtle.png", 8: "Whos_That_Pokemon-main\Pokemon Images\Wartortle.png",
9: "Whos_That_Pokemon-main\Pokemon Images\Blastoise.png", 10: "Whos_That_Pokemon-main\Pokemon Images\Pikachu.png",
11: "Whos_That_Pokemon-main\Pokemon Images\Dugtrio.png", 12: "Whos_That_Pokemon-main\Pokemon Images\Gengar.png",
13: "Whos_That_Pokemon-main\Pokemon Images\Articuno.png", 14: "Whos_That_Pokemon-main\Pokemon Images\Dragonite.png",
15: "Whos_That_Pokemon-main\Pokemon Images\Eevee.png", 16: "Whos_That_Pokemon-main\Pokemon Images\Flareon.png",
17: "Whos_That_Pokemon-main\Pokemon Images\Gyarados.png", 18: "Whos_That_Pokemon-main\Pokemon Images\Jigglypuff.png",
19: "Whos_That_Pokemon-main\Pokemon Images\Jolteon.png", 20: "Whos_That_Pokemon-main\Pokemon Images\Lapras.png",
21: "Whos_That_Pokemon-main\Pokemon Images\Magikarp.png", 22: "Whos_That_Pokemon-main\Pokemon Images\Meowth.png",
23: "Whos_That_Pokemon-main\Pokemon Images\Mew.png", 24: "Whos_That_Pokemon-main\Pokemon Images\Mewtwo.png",
25: "Whos_That_Pokemon-main\Pokemon Images\Moltres.png", 26: "Whos_That_Pokemon-main\Pokemon Images\Raichu.png",
27: "Whos_That_Pokemon-main\Pokemon Images\Snorlax.png", 28: "Whos_That_Pokemon-main\Pokemon Images\Vaporeon.png",
29: "Whos_That_Pokemon-main\Pokemon Images\Zapdos.png"}

pokemon_names = {1: "Bulbasaur", 2: "Ivysaur", 3: "Venusaur", 4: "Charmander",
5: "Charmeleon", 6: "Charizard", 7: "Squirtle", 8: "Wartortle", 9: "Blastoise",
10: "Pikachu", 11: "Dugtrio", 12: "Gengar", 13: "Articuno", 14: "Dragonite",
15: "Eevee", 16: "Flareon", 17: "Gyarados", 18: "Jigglypuff", 19: "Jolteon",
20: "Lapras", 21: "Magikarp", 22: "Meowth", 23: "Mew", 24: "Mewtwo",
25: "Moltres", 26: "Raichu", 27: "Snorlax", 28: "Vaporeon", 29: "Zapdos"}

pokemon_silhoettes = {
1: "Whos_That_Pokemon-main\Pokemon Silhoettes\Bulbasaur-s.png", 
2: "Whos_That_Pokemon-main\Pokemon Silhoettes\Ivysaur-s.png",
3: "Whos_That_Pokemon-main\Pokemon Silhoettes\Venusaur-s.png",
4: "Whos_That_Pokemon-main\Pokemon Silhoettes\Charmander-s.png",
5: "Whos_That_Pokemon-main\Pokemon Silhoettes\Charmeleon-s.png",
6: "Whos_That_Pokemon-main\Pokemon Silhoettes\Charizard-s.png",
7: "Whos_That_Pokemon-main\Pokemon Silhoettes\Squirtle-s.png",
8: "Whos_That_Pokemon-main\Pokemon Silhoettes\Wartortle-s.png",
9: "Whos_That_Pokemon-main\Pokemon Silhoettes\Blastoise-s.png",
10: "Whos_That_Pokemon-main\Pokemon Silhoettes\Pikachu-s.png",
11: "Whos_That_Pokemon-main\Pokemon Silhoettes\Dugtrio-s.png",
12: "Whos_That_Pokemon-main\Pokemon Silhoettes\Gengar-s.png",
13: "Whos_That_Pokemon-main\Pokemon Silhoettes\Articuno-s.png",
14: "Whos_That_Pokemon-main\Pokemon Silhoettes\Dragonite-s.png",
15: "Whos_That_Pokemon-main\Pokemon Silhoettes\Eevee-s.png",
16: "Whos_That_Pokemon-main\Pokemon Silhoettes\Flareon-s.png",
17: "Whos_That_Pokemon-main\Pokemon Silhoettes\Gyarados-s.png",
18: "Whos_That_Pokemon-main\Pokemon Silhoettes\Jigglypuff-s.png",
19: "Whos_That_Pokemon-main\Pokemon Silhoettes\Jolteon-s.png",
20: "Whos_That_Pokemon-main\Pokemon Silhoettes\Lapras-s.png",
21: "Whos_That_Pokemon-main\Pokemon Silhoettes\Magikarp-s.png",
22: "Whos_That_Pokemon-main\Pokemon Silhoettes\Meowth-s.png",
23: "Whos_That_Pokemon-main\Pokemon Silhoettes\Mew-s.png",
24: "Whos_That_Pokemon-main\Pokemon Silhoettes\Mewtwo-s.png",
25: "Whos_That_Pokemon-main\Pokemon Silhoettes\Moltres-s.png",
26: "Whos_That_Pokemon-main\Pokemon Silhoettes\Raichu-s.png",
27: "Whos_That_Pokemon-main\Pokemon Silhoettes\Snorlax-s.png",
28: "Whos_That_Pokemon-main\Pokemon Silhoettes\Vaporeon-s.png",
29: "Whos_That_Pokemon-main\Pokemon Silhoettes\Zapdos-s.png"}

#randomly generates the pokemon and the answer choices
def generator():
    rand.seed()
    to_display = rand.randint(1, 29) #displays silhoette corresponding with pokedex number
    used_names = [] #dictionary key used to determine the pokemon names displayed
    name_number = [] #pokemon names that will be displayed
    for x in range(4):
        used_names.append("0")
        name_number.append("0")
    used_options = [] #answer boxes that already have an answer
    option_number = option_generator()
    option = my_font.render(pokemon_names[to_display], True, (0,0,0))
    option_placement(option_number, option)
    to_click = correct_box(option_number)
    used_names[option_number-1] = to_display
    name_number[option_number-1] = pokemon_names[to_display]
    used_options.append(option_number)
    imp = pg.image.load(pokemon_silhoettes[to_display])
    screen.blit(imp, (0,0))
    for x in range (3): #generates the other answer choices
        rn = rand.randint(1,9)
        while (rn in used_names):
            rn = rand.randint(1,29)
        option_number = option_generator()
        while (option_number in used_options):
            option_number = option_generator()
        used_names[option_number-1] = rn
        name_number[option_number-1] = pokemon_names[rn]
        used_options.append(option_number)
        option = my_font.render(pokemon_names[rn], True, (0,0,0))
        option_placement(option_number, option)
    pg.display.update()
    return {1: name_number, 2: to_click, 3: to_display}

#first question
displayed = generator()
nn = displayed[1] #pokemon names
tc = displayed[2] #correct box to click
td = displayed[3] #pokemon silhouette

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: #closes the window
            running = False
        elif event.type == pg.MOUSEBUTTONUP:
            if tc.collidepoint(pg.mouse.get_pos()):
                score+=1
                after_guess()
                updated_screen()
                displayed = generator()
                nn = displayed[1] #pokemon names
                tc = displayed[2] #correct box to click
                td = displayed[3] #pokemon silhouette
            elif tl_option.collidepoint(pg.mouse.get_pos()) or tr_option.collidepoint(pg.mouse.get_pos()) or bl_option.collidepoint(pg.mouse.get_pos()) or br_option.collidepoint(pg.mouse.get_pos()):
                score = 0
                after_guess()
                game_over()
                decision = play_again()
                if decision == True:
                    updated_screen()
                    displayed = generator()
                    nn = displayed[1] #pokemon names
                    tc = displayed[2] #correct box to click
                    td = displayed[3] #pokemon silhouette
                else:
                    running = False
