import pygame
from sys import exit
from player import Player
from line import Line
from obstacle import Obstacle
from colors import *
from coin import Coin
from button import Button
from achievement import *
import random as rd
import math
import json

pygame.init()
pygame.mixer.init()

WIDTH = 700
HEIGHT = 1100

# Define the start and end colors for the background transition
START_COLOR = DARK_LIME
END_COLOR = PINK
BG_COLOR = START_COLOR

FONT = pygame.font.Font(None, 44)
TITLE_FONT = pygame.font.Font(None, 120)
SMALL_FONT = pygame.font.Font(None, 30)

TARGET_FPS = 60

wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rope Game")

player_1_starting_pos_x = 200
player_1_starting_pos_y = 1000
player_2_starting_pos_x = 500
player_2_starting_pos_y = 1000

player_1 = Player(PLAYER_1, 5, 20, 0, player_1_starting_pos_x, player_1_starting_pos_y, wn)
player_2 = Player(PLAYER_2, 5, 20, 1, player_2_starting_pos_x, player_2_starting_pos_y, wn)
obstacle = Obstacle(wn, 80, 40, 400, 400, 7, BG_COLOR, False)

line = Line(DARK_BROWN, 6, wn, player_1, player_2)

def play_main_menu_music():
    pygame.mixer.music.load(r'co-op game\main_menu_track.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def play_bg_music():
    pygame.mixer.music.load(r'co-op game\bg_track.mp3')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

play_main_menu_music()

hit_sound = pygame.mixer.Sound(r'co-op game\hit.mp3')
hit_sound.set_volume(1.4)
coin_sound = pygame.mixer.Sound(r'co-op game\coin.mp3')
coin_sound.set_volume(1.4)
button_click_sound = pygame.mixer.Sound(r'co-op game\button.mp3')
button_click_sound.set_volume(1.4)

health = 5
score = 0
high_score = 0
current_coins = 0

obstacles_to_spawn = 3  # the amount of obstacles to spawn at once
obstacle_spawn_interval = 2  # in seconds
last_obstacle_spawn = 0.0

coin_spawn_interval = 4
last_coin_spawn = 0.0

score_interval = 0.2  # interval for the score to update based on time
last_score_time = 0.0

hit_period = 1.0
last_hit_time = 0.0

total_runs = 0
total_coins = 0

game_state = "main_menu"

alive: bool = True

obstacles = []
coins = []
achievements = [First_time(wn, 20), fifth_time(wn, 140), ten_coins(wn, 260), ten_k_score(wn, 380), tweney_coins_single_run(wn, 500)]

clock = pygame.time.Clock()

obstacle_min_width = 80
obstacle_min_height = 50
obstacle_max_width = 140
obstacle_max_height = 160

# Save stats to JSON file
def save_stats(stats):
    with open('achievements.json', 'w') as file:
        json.dump(stats, file, indent=4)

# Load stats from JSON file
def load_stats():
    try:
        with open('achievements.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, return default stats
        return {
            "high_score": 0,
            "total_coins": 0,
            "total_runs": 0,
            "achievements": {
                "first_time": False,
                "fifth_time": False,
                "ten_coins": False,
                "ten_k_score": False,
                "twenty_coins_single_run": False,
                "hundred_runs": False
            }
        }

def reset_stats():
    stats = {
        "high_score": 0,
        "total_coins": 0,
        "total_runs": 0,
        "achievements": {
            "first_time": False,
            "fifth_time": False,
            "ten_coins": False,
            "ten_k_score": False,
            "twenty_coins_single_run": False,
            "hundred_runs": False
        }
    }
    save_stats(stats)
    return stats

def clear_data():
    stats = reset_stats()
    return stats

stats = load_stats()

# Update variables with loaded stats
high_score = stats["high_score"]
total_coins = stats["total_coins"]
total_runs = stats["total_runs"]
achievements[0].unlocked = stats["achievements"]["first_time"]
achievements[1].unlocked = stats["achievements"]["fifth_time"]
achievements[2].unlocked = stats["achievements"]["ten_coins"]
achievements[3].unlocked = stats["achievements"]["ten_k_score"]
achievements[4].unlocked = stats["achievements"]["twenty_coins_single_run"]


def quit():
    pygame.quit()
    exit()

def is_colliding(new_obstacle, obstacles):
    for obstacle in obstacles:
        if new_obstacle.get_rect().colliderect(obstacle.get_rect()):
            return True
    return False

def lerp_color(color1, color2, t):
    return (
        int(color1[0] + (color2[0] - color1[0]) * t),
        int(color1[1] + (color2[1] - color1[1]) * t),
        int(color1[2] + (color2[2] - color1[2]) * t)
    )

transition_duration = 360000  # Duration of the color transition in milliseconds
start_time = pygame.time.get_ticks()

while True:
    clock.tick(TARGET_FPS)
    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Calculate the interpolation factor (t) based on the elapsed time
    t = (math.sin((elapsed_time % transition_duration) / transition_duration * math.pi * 2) + 1) / 2

    # Interpolate the background color
    BG_COLOR = lerp_color(START_COLOR, END_COLOR, t)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save stats before quitting
            stats = {
                "high_score": high_score,
                "total_coins": total_coins,
                "total_runs": total_runs,
                "achievements": {
                    "first_time": achievements[0].unlocked,
                    "fifth_time": achievements[1].unlocked,
                    "ten_coins": achievements[2].unlocked,
                    "ten_k_score": achievements[3].unlocked,
                    "twenty_coins_single_run": achievements[4].unlocked,
                }
            }
            save_stats(stats)
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if game_state == "in_game":
        if alive:
            if keys[pygame.K_w] and player_1.y > player_1.scale:
                player_1.y -= player_1.speed
            if keys[pygame.K_s] and player_1.y < HEIGHT - player_1.scale:
                player_1.y += player_1.speed
            if keys[pygame.K_a] and player_1.x > player_1.scale:
                player_1.x -= player_1.speed
            if keys[pygame.K_d] and player_1.x < WIDTH - player_1.scale:
                player_1.x += player_1.speed

            if keys[pygame.K_UP] and player_2.y > player_2.scale:
                player_2.y -= player_2.speed
            if keys[pygame.K_DOWN] and player_2.y < HEIGHT - player_2.scale:
                player_2.y += player_2.speed
            if keys[pygame.K_LEFT] and player_2.x > player_2.scale:
                player_2.x -= player_2.speed
            if keys[pygame.K_RIGHT] and player_2.x < WIDTH - player_2.scale:
                player_2.x += player_2.speed

        if current_time - last_obstacle_spawn > obstacle_spawn_interval * 1000 and alive:
            last_obstacle_spawn = current_time
            for i in range(obstacles_to_spawn):
                while True:
                    new_obstacle = Obstacle(wn=wn, width=rd.randint(obstacle_min_width, obstacle_max_width), height=rd.randint(obstacle_min_height, obstacle_max_height), x=rd.randint(0, WIDTH), y=rd.randint(-150, -70), speed=rd.uniform(3.0, 5.0), color=BG_COLOR, hit=False)
                    if not is_colliding(new_obstacle, obstacles):
                        obstacles.append(new_obstacle)
                        break

        if current_time - last_coin_spawn > coin_spawn_interval * 1000 and alive:
            coins.append(Coin(wn, rd.randint(50, WIDTH - 50), rd.randint(-150, -20), 10, GOLD, rd.uniform(2.5, 4.5)))
            last_coin_spawn = current_time
        
        if total_coins >= 10:
            achievements[2].unlocked = True

    wn.fill(BG_COLOR)

    if game_state == "in_game":
        if score >= 50000:
            achievements[3].unlocked = True

        for obstacle in obstacles:
            if obstacle.y < HEIGHT + 200 and alive:
                obstacle.draw()
                obstacle.move()
            if line.collides_with(obstacle.get_rect()) and not obstacle.hit and alive:
                obstacle.hit = True
                health -= 1
                hit_sound.play()

        # Detect collisions between different obstacles
        for i in range(len(obstacles)):
            for j in range(i + 1, len(obstacles)):
                if obstacles[i].get_rect().colliderect(obstacles[j].get_rect()):
                    obstacles.pop(j)
                    break

        for coin in coins:
            if coin.y < HEIGHT + 100 and not coin.collected and alive:
                coin.draw()
                coin.move()
            if line.collides_with(coin.get_rect()) and not coin.collected and alive:
                score += 1500
                current_coins += 1
                coin_sound.play()
                coin.collected = True
                total_coins += 1

        if current_time - last_score_time > score_interval * 1000 and alive:
            score += 1

        if health <= 0:
            alive = False
            game_state = "main_menu"
            play_main_menu_music()
        
        if keys[pygame.K_ESCAPE]:
            alive = False
            game_state = "main_menu"
            play_main_menu_music()

        if score > high_score:
            high_score = score

        if alive:
            line.draw()
            player_1.draw()
            player_2.draw()

            score_text = FONT.render(f"{score}", True, GOLD)
            wn.blit(score_text, (10, 20))

            health_text = FONT.render(f"{health}", True, LIME)
            wn.blit(health_text, (10, 60))

    if game_state == "main_menu":
        current_coins = 0
        score = 0
        health = 5

        play_button = Button(wn, WIDTH / 2 - 100, HEIGHT / 2 - 75, 200, 50, BLUE, DARK_BLUE, BLACK, GRAY, "PLAY")
        play_button.draw()

        settings_button = Button(wn, WIDTH / 2 - 100, HEIGHT / 2, 200, 50, GRAY, DARK_GRAY, BLACK, GRAY, "SETTINGS")
        settings_button.draw()

        achievement_button = Button(wn, WIDTH / 2 - 120, HEIGHT / 2 + 75, 240, 50, GREEN, DARK_LIME, BLACK, GRAY, "ACHIEVEMENTS")
        achievement_button.draw()

        exit_button = Button(wn, WIDTH / 2 - 100, HEIGHT / 2 + 150, 200, 50, RED, DARK_RED, BLACK, GRAY, "EXIT")
        exit_button.draw()

        clear_data_button = Button(wn,WIDTH/2- 100, HEIGHT-200,200,50,VIOLET,DARK_VIOLET,BLACK,GRAY,"RESET")
        clear_data_button.draw()

        credit_text = SMALL_FONT.render("Made by Kinda :3", True, BLACK)
        wn.blit(credit_text, (WIDTH / 2 - 85, 10))

        player_1.x = 130
        player_1.y = 375
        player_2.x = 600
        player_2.y = 375

        line.draw()
        player_1.draw()
        player_2.draw()

        title_text = TITLE_FONT.render("ROPE GAME", True, DARK_BROWN)
        wn.blit(title_text, (120, 200))

        high_score_text = FONT.render(f"High Score: {high_score}", True, GOLD)
        if high_score > 0:
            wn.blit(high_score_text, (250, 300))

        if play_button.is_clicked(event):
            game_state = "in_game"
            play_bg_music()
            alive = True
            player_1.x = player_1_starting_pos_x
            player_1.y = player_1_starting_pos_y
            player_2.x = player_2_starting_pos_x
            player_2.y = player_2_starting_pos_y
            total_runs += 1
            obstacles.clear()
            coins.clear()
        
        if settings_button.is_clicked(event):
            game_state = "settings"
            # no settings yet

        if achievement_button.is_clicked(event):
            game_state = "achievements"
        
        if exit_button.is_clicked(event):
            # Save stats before quitting
            stats = {
                "high_score": high_score,
                "total_coins": total_coins,
                "total_runs": total_runs,
                "achievements": {
                    "first_time": achievements[0].unlocked,
                    "fifth_time": achievements[1].unlocked,
                    "ten_coins": achievements[2].unlocked,
                    "ten_k_score": achievements[3].unlocked,
                    "twenty_coins_single_run": achievements[4].unlocked,
                    "hundred_runs": achievements[5].unlocked
                }
            }
            save_stats(stats)
            pygame.quit()
            exit()
        
        if clear_data_button.is_clicked(event):
            stats = reset_stats()
            # Update variables with reset stats
            high_score = stats["high_score"]
            total_coins = stats["total_coins"]
            total_runs = stats["total_runs"]
            achievements[0].unlocked = stats["achievements"]["first_time"]
            achievements[1].unlocked = stats["achievements"]["fifth_time"]
            achievements[2].unlocked = stats["achievements"]["ten_coins"]
            achievements[3].unlocked = stats["achievements"]["ten_k_score"]
            achievements[4].unlocked = stats["achievements"]["twenty_coins_single_run"]
        
    if game_state == "settings":
        settings_back_button = Button(wn, WIDTH / 2 - 75, HEIGHT / 2 + 200, 150, 50, RED, DARK_RED, BLACK, BLACK, "BACK")
        settings_back_button.draw()

        if settings_back_button.is_clicked(event):
            game_state = "main_menu"
    
    if game_state == "achievements":
        achievements_back_button = Button(wn, 10, 10, 150, 50, RED, DARK_RED, BLACK, BLACK, "BACK")
        achievements_back_button.draw()

        for achievement in achievements:
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    achievement.y += 50
                elif event.y == -1:
                    achievement.y -= 50
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"button": 2, "pos": (250, 250)}))
            achievement.draw()

        if achievements_back_button.is_clicked(event):
            game_state = "main_menu"
    
    if total_runs == 1:
        achievements[0].unlocked = True
    if total_runs == 50:
        achievements[1].unlocked = True
    if current_coins >= 20:
        achievements[4].unlocked = True

    pygame.display.update()