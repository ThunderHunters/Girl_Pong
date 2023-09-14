import pygame
import sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score_sound.play()
        player_score += 1
        ball_start() 
    if ball.right >= screen_width:
        score_sound.play()
        ball_start()
        opponent_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        sound_effect.play()

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height 

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height   

def ball_restart():
    global ball_speed_x, ball_speed_y 
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *=random.choice((1, -1))
    ball_speed_x *=random.choice((1, -1))

def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *=random.choice((1, -1))
    ball_speed_x *=random.choice((1, -1))


# Pygame setup
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Load the sounds (Here you must change the file path to where you downloaded the files to get the sounds to play)
sound_effect = pygame.mixer.Sound("/Users/acapol200/Documents/Angela Capolino Docs/2023 SAVE FOLDER/mac python projects/BBC 19-63.WAV")
score_sound = pygame.mixer.Sound("/Users/acapol200/Documents/Angela Capolino Docs/2023 SAVE FOLDER/mac python projects/Snare Drum Hit 01.wav")

# Setup game window
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pygame Girl Pong")

# Game rectangle objects
ball = pygame.Rect(screen_width/2 -15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 50, 10, 100)
opponent = pygame.Rect(10, screen_height/2 - 50, 10, 100)

# Game colors
bg_color = pygame.Color(0, 64, 0)
light_grey = (200,200,200)
pink = (255,105,180)
yellow = (255, 255, 0)
green = (0, 64, 0)
white = (255, 255, 255)

# Game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont("chiller", 42)

# Calculate center of play area
center_x = screen_width // 2
center_y = screen_height // 2


while True:

    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7

    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color) 
    pygame.draw.rect(screen, yellow, player)
    pygame.draw.rect(screen, yellow, opponent)
    pygame.draw.ellipse(screen, pink, ball)
    pygame.draw.line(screen, yellow, (screen_width/2, 0), (screen_width/2, screen_height), 5)
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, screen_width, screen_height), 5)

    # Calculate the position to render scores at center
    player_text = game_font.render(f"{player_score}", False, white)
    player_text_rect = player_text.get_rect(center=(center_x - 50, center_y))
    screen.blit(player_text, player_text_rect)

    opponent_text = game_font.render(f"{opponent_score}", False, white)
    opponent_text_rect = opponent_text.get_rect(center=(center_x + 50, center_y))
    screen.blit(opponent_text, opponent_text_rect)  

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
