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
3: "Whos_That_Pokemon-main\Pokemon Images 2\Venusaur.png", 4: "Whos_That_Pokemon-main\Pokemon Images\Charmander.png",
5: "Whos_That_Pokemon-main\Pokemon Images\Charmeleon.png", 6: "Whos_That_Pokemon-main\Pokemon Images\Charizard.png",
7: "Whos_That_Pokemon-main\Pokemon Images 2\Squirtle.png", 8: "Whos_That_Pokemon-main\Pokemon Images 2\Wartortle.png",
9: "Whos_That_Pokemon-main\Pokemon Images\Blastoise.png", 10: "Whos_That_Pokemon-main\Pokemon Images\Caterpie.png",
11: "Whos_That_Pokemon-main\Pokemon Images\Metapod.png", 12: "Whos_That_Pokemon-main\Pokemon Images\Butterfree.png",
13: "Whos_That_Pokemon-main\Pokemon Images 2\Weedle.png", 14: "Whos_That_Pokemon-main\Pokemon Images\Kakuna.png",
15: "Whos_That_Pokemon-main\Pokemon Images\Beedrill.png", 16: "Whos_That_Pokemon-main\Pokemon Images 2\Pidgey.png",
17: "Whos_That_Pokemon-main\Pokemon Images 2\Pidgeotto.png", 18: "Whos_That_Pokemon-main\Pokemon Images 2\Pidgeot.png",
19: "Whos_That_Pokemon-main\Pokemon Images 2\Rattata.png", 20: "Whos_That_Pokemon-main\Pokemon Images 2\Raticate.png",
21: "Whos_That_Pokemon-main\Pokemon Images 2\Spearow.png", 22: "Whos_That_Pokemon-main\Pokemon Images\Fearow.png",
23: "Whos_That_Pokemon-main\Pokemon Images\Ekans.png", 24: "Whos_That_Pokemon-main\Pokemon Images\Arbok.png",
25: "Whos_That_Pokemon-main\Pokemon Images 2\Pikachu.png", 26: "Whos_That_Pokemon-main\Pokemon Images\Raichu.png",
27: "Whos_That_Pokemon-main\Pokemon Images 2\Sandshrew.png", 28: "Whos_That_Pokemon-main\Pokemon Images 2\Sandslash.png",
29: "Whos_That_Pokemon-main\Pokemon Images 2\FNidoran.png", 30: "Whos_That_Pokemon-main\Pokemon Images 2\idoRina.png",
31: "Whos_That_Pokemon-main\Pokemon Images 2\queenNido.png", 32: "Whos_That_Pokemon-main\Pokemon Images 2\MNidoran.png",
33: "Whos_That_Pokemon-main\Pokemon Images 2\idoRino.png", 34: "Whos_That_Pokemon-main\Pokemon Images 2\kingNido.png",
35: "Whos_That_Pokemon-main\Pokemon Images\Clefairy.png", 36: "Whos_That_Pokemon-main\Pokemon Images\Clefable.png",
37: "Whos_That_Pokemon-main\Pokemon Images 2\Vulpix.png", 38: "Whos_That_Pokemon-main\Pokemon Images 2\inetales.png",
39: "Whos_That_Pokemon-main\Pokemon Images\Jigglypuff.png", 40: "Whos_That_Pokemon-main\Pokemon Images 2\Wigglytuff.png",
41: "Whos_That_Pokemon-main\Pokemon Images 2\Zubat.png", 42: "Whos_That_Pokemon-main\Pokemon Images\Golbat.png",
43: "Whos_That_Pokemon-main\Pokemon Images 2\Oddish.png", 44: "Whos_That_Pokemon-main\Pokemon Images\Gloom.png", 
45: "Whos_That_Pokemon-main\Pokemon Images 2\Vileplume.png", 46: "Whos_That_Pokemon-main\Pokemon Images 2\Paras.png",
47: "Whos_That_Pokemon-main\Pokemon Images 2\Parasect.png", 48: "Whos_That_Pokemon-main\Pokemon Images 2\Venonat.png",
49: "Whos_That_Pokemon-main\Pokemon Images 2\Venomoth.png", 50: "Whos_That_Pokemon-main\Pokemon Images\DIglett.png",
51: "Whos_That_Pokemon-main\Pokemon Images\Dugtrio.png", 52: "Whos_That_Pokemon-main\Pokemon Images\Meowth.png",
53: "Whos_That_Pokemon-main\Pokemon Images 2\Persian.png", 54: "Whos_That_Pokemon-main\Pokemon Images 2\Psyduck.png",
55: "Whos_That_Pokemon-main\Pokemon Images\Golduck.png", 56: "Whos_That_Pokemon-main\Pokemon Images\Mankey.png",
57: "Whos_That_Pokemon-main\Pokemon Images 2\Primeape.png", 58: "Whos_That_Pokemon-main\Pokemon Images\Growtlithe.png",
59: "Whos_That_Pokemon-main\Pokemon Images\Arcanine.png", 60: "Whos_That_Pokemon-main\Pokemon Images 2\Poliwag.png",
61: "Whos_That_Pokemon-main\Pokemon Images 2\Poliwhirl.png", 62: "Whos_That_Pokemon-main\Pokemon Images 2\Poliwrath.png",
63: "Whos_That_Pokemon-main\Pokemon Images\Abra.png", 64: "Whos_That_Pokemon-main\Pokemon Images\Kadabra.png",
65: "Whos_That_Pokemon-main\Pokemon Images\Alakazam.png", 66: "Whos_That_Pokemon-main\Pokemon Images\Machop.png",
67: "Whos_That_Pokemon-main\Pokemon Images\Machoke.png", 68: "Whos_That_Pokemon-main\Pokemon Images\Machamp.png",
69: "Whos_That_Pokemon-main\Pokemon Images\Bellsprout.png", 70: "Whos_That_Pokemon-main\Pokemon Images 2\Weepinbell.png",
71: "Whos_That_Pokemon-main\Pokemon Images 2\Victreebel.png", 72: "Whos_That_Pokemon-main\Pokemon Images 2\Tentacool.png",
73: "Whos_That_Pokemon-main\Pokemon Images 2\Tentacruel.png", 74: "Whos_That_Pokemon-main\Pokemon Images\Geodude.png",
75: "Whos_That_Pokemon-main\Pokemon Images\Graveler.png", 76: "Whos_That_Pokemon-main\Pokemon Images\Golem.png",
77: "Whos_That_Pokemon-main\Pokemon Images 2\Ponyta.png", 78: "Whos_That_Pokemon-main\Pokemon Images 2\Rapidash.png",
79: "Whos_That_Pokemon-main\Pokemon Images 2\Slowpoke.png", 80: "Whos_That_Pokemon-main\Pokemon Images 2\Slowbro.png",
81: "Whos_That_Pokemon-main\Pokemon Images\Magnemite.png", 82: "Whos_That_Pokemon-main\Pokemon Images\Magneton.png",
83: "Whos_That_Pokemon-main\Pokemon Images\Farfetch'd.png", 84: "Whos_That_Pokemon-main\Pokemon Images\Doduo.png",
85: "Whos_That_Pokemon-main\Pokemon Images\Dodrio.png", 86: "Whos_That_Pokemon-main\Pokemon Images 2\Seel.png",
87: "Whos_That_Pokemon-main\Pokemon Images\Dewgong.png", 88: "Whos_That_Pokemon-main\Pokemon Images\Grimer.png",
89: "Whos_That_Pokemon-main\Pokemon Images 2\Muk.png", 90: "Whos_That_Pokemon-main\Pokemon Images 2\Shellder.png",
91: "Whos_That_Pokemon-main\Pokemon Images\Cloyster.png", 92: "Whos_That_Pokemon-main\Pokemon Images\Gastly.png",
93: "Whos_That_Pokemon-main\Pokemon Images\Haunter.png", 94: "Whos_That_Pokemon-main\Pokemon Images\Gengar.png",
95: "Whos_That_Pokemon-main\Pokemon Images 2\Onix.png", 96: "Whos_That_Pokemon-main\Pokemon Images\Drowzee.png",
97: "Whos_That_Pokemon-main\Pokemon Images\Hypno.png", 98: "Whos_That_Pokemon-main\Pokemon Images\Krabby.png",
99: "Whos_That_Pokemon-main\Pokemon Images\Kingler.png", 100: "Whos_That_Pokemon-main\Pokemon Images 2\Voltorb.png",
101: "Whos_That_Pokemon-main\Pokemon Images\Electrode.png", 102: "Whos_That_Pokemon-main\Pokemon Images\Exeggcute.png",
103: "Whos_That_Pokemon-main\Pokemon Images\Exeggutor.png", 104: "Whos_That_Pokemon-main\Pokemon Images\Cubone.png",
105: "Whos_That_Pokemon-main\Pokemon Images\Marowak.png", 106: "Whos_That_Pokemon-main\Pokemon Images\Hitmonlee.png",
107: "Whos_That_Pokemon-main\Pokemon Images\Hitmonchan.png", 108: "Whos_That_Pokemon-main\Pokemon Images\Lickitung.png",
109: "Whos_That_Pokemon-main\Pokemon Images\Koffing.png", 110: "Whos_That_Pokemon-main\Pokemon Images 2\Weezing.png",
111: "Whos_That_Pokemon-main\Pokemon Images 2\Rhyhorn.png", 112: "Whos_That_Pokemon-main\Pokemon Images 2\Rhydon.png",
113: "Whos_That_Pokemon-main\Pokemon Images\Chansey.png", 114: "Whos_That_Pokemon-main\Pokemon Images 2\Tangela.png",
115: "Whos_That_Pokemon-main\Pokemon Images\Kangaskhan.png", 116: "Whos_That_Pokemon-main\Pokemon Images\Horsea.png",
117: "Whos_That_Pokemon-main\Pokemon Images 2\Seadra.png", 118: "Whos_That_Pokemon-main\Pokemon Images\Goldeen.png",
119: "Whos_That_Pokemon-main\Pokemon Images 2\Seaking.png", 120: "Whos_That_Pokemon-main\Pokemon Images 2\Staryu.png",
121: "Whos_That_Pokemon-main\Pokemon Images 2\Starmie.png", 122: "Whos_That_Pokemon-main\Pokemon Images 2\Mr. Mime.png",
123: "Whos_That_Pokemon-main\Pokemon Images 2\Scyther.png", 124: "Whos_That_Pokemon-main\Pokemon Images\Jynx.png",
125: "Whos_That_Pokemon-main\Pokemon Images\Electabuzz.png", 126: "Whos_That_Pokemon-main\Pokemon Images\Magmar.png",
127: "Whos_That_Pokemon-main\Pokemon Images 2\Pinsir.png", 128: "Whos_That_Pokemon-main\Pokemon Images 2\Tauros.png",
129: "Whos_That_Pokemon-main\Pokemon Images\Magikarp.png", 130: "Whos_That_Pokemon-main\Pokemon Images\Gyarados.png",
131: "Whos_That_Pokemon-main\Pokemon Images\Lapras.png", 132: "Whos_That_Pokemon-main\Pokemon Images\Ditto.png",
133: "Whos_That_Pokemon-main\Pokemon Images\Eevee.png", 134: "Whos_That_Pokemon-main\Pokemon Images 2\Vaporeon.png",
135: "Whos_That_Pokemon-main\Pokemon Images\Jolteon.png", 136: "Whos_That_Pokemon-main\Pokemon Images\Flareon.png",
137: "Whos_That_Pokemon-main\Pokemon Images 2\Porygon.png", 138: "Whos_That_Pokemon-main\Pokemon Images 2\Omanyte.png",
139: "Whos_That_Pokemon-main\Pokemon Images 2\Omastar.png", 140: "Whos_That_Pokemon-main\Pokemon Images\Kabuto.png",
141: "Whos_That_Pokemon-main\Pokemon Images\Kabutops.png", 142: "Whos_That_Pokemon-main\Pokemon Images\Aerodactyl.png",
143: "Whos_That_Pokemon-main\Pokemon Images 2\Snorlax.png", 144: "Whos_That_Pokemon-main\Pokemon Images\Articuno.png",
145: "Whos_That_Pokemon-main\Pokemon Images 2\Zapdos.png", 146: "Whos_That_Pokemon-main\Pokemon Images\Moltres.png",
147: "Whos_That_Pokemon-main\Pokemon Images\Dratini.png", 148: "Whos_That_Pokemon-main\Pokemon Images\Dragonair.png",
149: "Whos_That_Pokemon-main\Pokemon Images\Dragonite.png", 150: "Whos_That_Pokemon-main\Pokemon Images\Mewtwo.png",
151: "Whos_That_Pokemon-main\Pokemon Images\Mew.png"}

pokemon_names = {1: "Bulbasaur", 2: "Ivysaur", 3: "Venusaur", 4: "Charmander",
5: "Charmeleon", 6: "Charizard", 7: "Squirtle", 8: "Wartortle", 9: "Blastoise",
10: "Caterpie", 11: "Metapod", 12: "Butterfree", 13: "Weedle", 14: "Kakuna",
15: "Beedrill", 16: "Pidgey", 17: "Pidgeotto", 18: "Pidgeot", 19: "Rattata",
20: "Raticate", 21: "Spearow", 22: "Fearow", 23: "Ekans", 24: "Arbok",
25: "Pikachu", 26: "Raichu", 27: "Sandshrew", 28: "Sandslash", 29: "Nidoran F",
30: "Nidorina", 31: "Nidoqueen", 32: "Nidoran M", 33: "Nidorino", 34: "Nidoking",
35: "Clefairy", 36: "Clefable", 37: "Vulpix", 38: "Ninetales", 39: "Jigglypuff",
40: "Wigglytuff", 41: "Zubat", 42: "Golbat", 43: "Oddish", 44: "Gloom",
45: "Vileplume", 46: "Paras", 47: "Parasect", 48: "Venonat", 49: "Venomoth",
50: "Diglett", 51: "Dugtrio", 52: "Meowth", 53: "Persian", 54: "Psyduck",
55: "Golduck", 56: "Mankey", 57: "Primeape", 58: "Growlithe", 59: "Arcanine",
60: "Poliwag", 61: "Poliwhirl", 62: "Poliwrath", 63: "Abra", 64: "Kadabra",
65: "Alakazam", 66: "Machop", 67: "Machoke", 68: "Machamp", 69: "Bellsprout",
70: "Weepinbell", 71: "Victreebel", 72: "Tentacool", 73: "Tentacruel", 74: "Geodude",
75: "Graveler", 76: "Golem", 77: "Ponyta", 78: "Rapidash", 79: "Slowpoke",
80: "Slowbro", 81: "Magnemite", 82: "Magneton", 83: "Farfetch'd", 84: "Doduo",
85: "Dodrio", 86: "Seel", 87: "Dewgong", 88: "Grimer", 89: "Muk",
90: "Shellder", 91: "Cloyster", 92: "Gastly", 93: "Haunter", 94: "Gengar",
95: "Onix", 96: "Drowzee", 97: "Hypno", 98: "Krabby", 99: "Kingler",
100: "Voltorb", 101: "Electrode", 102: "Exeggcute", 103: "Exeggutor", 104: "Cubone",
105: "Marowak", 106: "Hitmonlee", 107: "Hitmonchan", 108: "Lickitung", 109: "Koffing", 
110: "Weezing", 111: "Rhyhorn", 112: "Rhydon", 113: "Chansey", 114: "Tangela",
115: "Kangaskhan", 116: "Horsea", 117: "Seadra", 118: "Goldeen", 119: "Seaking",
120: "Staryu", 121: "Starmie", 122: "Mr. Mime", 123: "Scyther", 124: "Jynx",
125: "Electabuzz", 126: "Magmar", 127: "Pinsir", 128: "Tauros", 129: "Magikarp",
130: "Gyarados", 131: "Lapras", 132: "Ditto", 133: "Eevee", 134: "Vaporeon",
135: "Jolteon", 136: "Flareon", 137: "Porygon", 138: "Omanyte", 139: "Omastar", 
140: "Kabuto", 141: "Kabutops", 142: "Aerodactyl", 143: "Snorlax", 144: "Articuno",
145: "Zapdos", 146: "Moltres", 147: "Dratini", 148: "Dragonair", 149: "Dragonite",
150: "Mewtwo", 151: "Mew"}

pokemon_silhoettes = {
1: "Whos_That_Pokemon-main\Pokemon Silhouettes\Bulbasaur-s.png", 
2: "Whos_That_Pokemon-main\Pokemon Silhouettes\Ivysaur-s.png",
3: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Venusaur-s.png",
4: "Whos_That_Pokemon-main\Pokemon Silhouettes\Charmander-s.png",
5: "Whos_That_Pokemon-main\Pokemon Silhouettes\Charmeleon-s.png",
6: "Whos_That_Pokemon-main\Pokemon Silhouettes\Charizard-s.png",
7: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Squirtle-s.png",
8: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Wartortle-s.png",
9: "Whos_That_Pokemon-main\Pokemon Silhouettes\Blastoise-s.png",
10: "Whos_That_Pokemon-main\Pokemon Silhouettes\Caterpie-s.png",
11: "Whos_That_Pokemon-main\Pokemon Silhouettes\Metapod-s.png",
12: "Whos_That_Pokemon-main\Pokemon Silhouettes\Butterfree-s.png",
13: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Weedle-s.png",
14: "Whos_That_Pokemon-main\Pokemon Silhouettes\Kakuna-s.png",
15: "Whos_That_Pokemon-main\Pokemon Silhouettes\Beedrill-s.png",
16: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Pidgey-s.png",
17: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Pidgeotto-s.png",
18: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Pidgeot-s.png",
19: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Rattata-s.png",
20: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Raticate-s.png",
21: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Spearow-s.png",
22: "Whos_That_Pokemon-main\Pokemon Silhouettes\Fearow-s.png",
23: "Whos_That_Pokemon-main\Pokemon Silhouettes\Ekans-s.png",
24: "Whos_That_Pokemon-main\Pokemon Silhouettes\Arbok-s.png",
25: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Pikachu-s.png",
26: "Whos_That_Pokemon-main\Pokemon Silhouettes\Raichu-s.png",
27: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Sandshrew-s.png",
28: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Sandslash-s.png",
29: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\FNidoran-s.png",
30: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\idorina-s.png",
31: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\queenNido-s.png",
32: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\MNidoran-s.png",
33: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\idorino-s.png",
34: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\kingNido-s.png",
35: "Whos_That_Pokemon-main\Pokemon Silhouettes\Clefairy-s.png",
36: "Whos_That_Pokemon-main\Pokemon Silhouettes\Clefable-s.png",
37: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Vulpix-s.png",
38: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\inetales-s.png",
39: "Whos_That_Pokemon-main\Pokemon Silhouettes\Jigglypuff-s.png",
40: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Wigglytuff-s.png",
41: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Zubat-s.png",
42: "Whos_That_Pokemon-main\Pokemon Silhouettes\Golbat-s.png",
43: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Oddish-s.png",
44: "Whos_That_Pokemon-main\Pokemon Silhouettes\Gloom-s.png",
45: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Vileplume-s.png",
46: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Paras-s.png",
47: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Parasect-s.png",
48: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Venonat-s.png",
49: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Venomoth-s.png",
50: "Whos_That_Pokemon-main\Pokemon Silhouettes\Diglett-s.png",
51: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dugtrio-s.png",
52: "Whos_That_Pokemon-main\Pokemon Silhouettes\Meowth-s.png",
53: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Persian-s.png",
54: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Psyduck-s.png",
55: "Whos_That_Pokemon-main\Pokemon Silhouettes\Golduck-s.png",
56: "Whos_That_Pokemon-main\Pokemon Silhouettes\Mankey-s.png",
57: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Primeape-s.png",
58: "Whos_That_Pokemon-main\Pokemon Silhouettes\Growlithe-s.png",
59: "Whos_That_Pokemon-main\Pokemon Silhouettes\Arcanine-s.png",
60: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Poliwag-s.png",
61: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Poliwhirl-s.png",
62: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Poliwrath-s.png",
63: "Whos_That_Pokemon-main\Pokemon Silhouettes\Abra-s.png",
64: "Whos_That_Pokemon-main\Pokemon Silhouettes\Kadabra-s.png",
65: "Whos_That_Pokemon-main\Pokemon Silhouettes\Alakazam-s.png",
66: "Whos_That_Pokemon-main\Pokemon Silhouettes\Machop-s.png",
67: "Whos_That_Pokemon-main\Pokemon Silhouettes\Machoke-s.png",
68: "Whos_That_Pokemon-main\Pokemon Silhouettes\Machamp-s.png",
69: "Whos_That_Pokemon-main\Pokemon Silhouettes\Bellsprout-s.png",
70: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Weepinbell-s.png",
71: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Victreebel-s.png",
72: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Tentacool-s.png",
73: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Tentacruel-s.png",
74: "Whos_That_Pokemon-main\Pokemon Silhouettes\Geodude-s.png",
75: "Whos_That_Pokemon-main\Pokemon Silhouettes\Graveler-s.png",
76: "Whos_That_Pokemon-main\Pokemon Silhouettes\Golem-s.png",
77: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Ponyta-s.png",
78: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Rapidash-s.png",
79: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Slowpoke-s.png",
80: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Slowbro-s.png",
81: "Whos_That_Pokemon-main\Pokemon Silhouettes\Magnemite-s.png",
82: "Whos_That_Pokemon-main\Pokemon Silhouettes\Magneton-s.png",
83: "Whos_That_Pokemon-main\Pokemon Silhouettes\Farfetch'd-s.png",
84: "Whos_That_Pokemon-main\Pokemon Silhouettes\Doduo-s.png",
85: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dodrio-s.png",
86: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Seel-s.png",
87: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dewgong-s.png",
88: "Whos_That_Pokemon-main\Pokemon Silhouettes\Grimer-s.png",
89: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Muk-s.png",
90: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Shellder-s.png",
91: "Whos_That_Pokemon-main\Pokemon Silhouettes\Cloyster-s.png",
92: "Whos_That_Pokemon-main\Pokemon Silhouettes\Gastly-s.png",
93: "Whos_That_Pokemon-main\Pokemon Silhouettes\Haunter-s.png",
94: "Whos_That_Pokemon-main\Pokemon Silhouettes\Gengar-s.png",
95: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Onix-s.png",
96: "Whos_That_Pokemon-main\Pokemon Silhouettes\Drowzee-s.png",
97: "Whos_That_Pokemon-main\Pokemon Silhouettes\Hypno-s.png",
98: "Whos_That_Pokemon-main\Pokemon Silhouettes\Drowzee-s.png",
99: "Whos_That_Pokemon-main\Pokemon Silhouettes\Hypno-s.png",
100: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Voltorb-s.png",
101: "Whos_That_Pokemon-main\Pokemon Silhouettes\Electrode-s.png",
102: "Whos_That_Pokemon-main\Pokemon Silhouettes\Exeggcute-s.png",
103: "Whos_That_Pokemon-main\Pokemon Silhouettes\Exeggutor-s.png",
104: "Whos_That_Pokemon-main\Pokemon Silhouettes\Cubone-s.png",
105: "Whos_That_Pokemon-main\Pokemon Silhouettes\Marowak-s.png",
106: "Whos_That_Pokemon-main\Pokemon Silhouettes\Hitmonlee-s.png",
107: "Whos_That_Pokemon-main\Pokemon Silhouettes\Hitmonchan-s.png",
108: "Whos_That_Pokemon-main\Pokemon Silhouettes\Lickitung-s.png",
109: "Whos_That_Pokemon-main\Pokemon Silhouettes\Koffing-s.png",
110: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Weezing-s.png",
111: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Rhyhorn-s.png",
112: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Rhydon-s.png",
113: "Whos_That_Pokemon-main\Pokemon Silhouettes\Chansey-s.png",
114: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Tangela-s.png",
115: "Whos_That_Pokemon-main\Pokemon Silhouettes\Kangaskhan-s.png",
116: "Whos_That_Pokemon-main\Pokemon Silhouettes\Horsea-s.png",
117: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Seadra-s.png",
118: "Whos_That_Pokemon-main\Pokemon Silhouettes\Goldeen-s.png",
119: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Seaking-s.png",
120: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Staryu-s.png",
121: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Starmie-s.png",
122: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Mr. Mime-s.png",
123: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Scyther-s.png",
124: "Whos_That_Pokemon-main\Pokemon Silhouettes\Jynx-s.png",
125: "Whos_That_Pokemon-main\Pokemon Silhouettes\Electabuzz-s.png",
126: "Whos_That_Pokemon-main\Pokemon Silhouettes\Magmar-s.png",
127: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Pinsir-s.png",
128: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Tauros-s.png",
129: "Whos_That_Pokemon-main\Pokemon Silhouettes\Magikarp-s.png",
130: "Whos_That_Pokemon-main\Pokemon Silhouettes\Gyarados-s.png",
131: "Whos_That_Pokemon-main\Pokemon Silhouettes\Lapras-s.png",
132: "Whos_That_Pokemon-main\Pokemon Silhouettes\Ditto-s.png",
133: "Whos_That_Pokemon-main\Pokemon Silhouettes\Eevee-s.png",
134: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Vaporeon-s.png",
135: "Whos_That_Pokemon-main\Pokemon Silhouettes\Jolteon-s.png",
136: "Whos_That_Pokemon-main\Pokemon Silhouettes\Flareon-s.png",
137: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Porygon-s.png",
138: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Omanyte-s.png",
139: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Omastar-s.png",
140: "Whos_That_Pokemon-main\Pokemon Silhouettes\Kabuto-s.png",
141: "Whos_That_Pokemon-main\Pokemon Silhouettes\Kabutops-s.png",
142: "Whos_That_Pokemon-main\Pokemon Silhouettes\Aerodactyl-s.png",
143: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Snorlax-s.png",
144: "Whos_That_Pokemon-main\Pokemon Silhouettes\Articuno-s.png",
145: "Whos_That_Pokemon-main\Pokemon Silhouettes 2\Zapdos-s.png",
146: "Whos_That_Pokemon-main\Pokemon Silhouettes\Moltres-s.png",
147: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dratini-s.png",
148: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dragonair-s.png",
149: "Whos_That_Pokemon-main\Pokemon Silhouettes\Dragonite-s.png",
150: "Whos_That_Pokemon-main\Pokemon Silhouettes\Mewtwo-s.png",
151: "Whos_That_Pokemon-main\Pokemon Silhouettes\Mew-s.png"
}

#randomly generates the pokemon and the answer choices
def generator():
    rand.seed()
    to_display = rand.randint(1, 151) #displays silhoette corresponding with pokedex number
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
            rn = rand.randint(1,151)
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
