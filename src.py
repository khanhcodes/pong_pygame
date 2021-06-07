
import pygame, sys, random

#Setup
pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
clock = pygame.time.Clock()

#Window
grey = (23,23,23)
orange = (239, 80, 41 )
white = (255,255,255)
screen_width = 800
screen_height= 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(grey)
pygame.display.set_caption('Pong Game')


#global variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 26)
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

def ball_animation():
    global player_score, opponent_score
    global ball_speed_x, ball_speed_y, score_time 
    
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *=-1

    if ball.left <=0: 
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width: 
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    #reverse the direction of the ball when it hits the edge
    if ball.colliderect(player) and ball_speed_x>0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) <10:
            ball_speed_x *= -1
            #reverse back when the ball reach the top of botton of the paddle 
            #when the ball reaches the top and the direction is going downward, the ball reverses and vice versa
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x<0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
         ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1


    
def player_animation():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom> ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time <700:
        number_three = game_font.render("3", False, white)
        screen.blit(number_three,(screen_width/2-6, screen_height/2+30))
    if 700< current_time - score_time < 1400:
        number_two = game_font.render("2", False, white)
        screen.blit(number_two,(screen_width/2-6, screen_height/2+30))
    if 1400< current_time - score_time < 2100:
        number_one = game_font.render("1", False, white)
        screen.blit(number_one,(screen_width/2-6, screen_height/2+30))
    if current_time - score_time <2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 6 * random.choice((1,-1))
        ball_speed_x = 6 * random.choice((1,-1))
        score_time = None



ball = pygame.Rect(screen_width/2 - 14, screen_height/2 - 14, 28, 28)
player = pygame.Rect(screen_width - 20, screen_height/2 - 60, 10, 120)
opponent = pygame.Rect(10, screen_height/2 - 60, 10, 120)

ball_speed_x = 6 * random.choice((1,-1))
ball_speed_y = 6 * random.choice((1,-1))
player_speed = 0
opponent_speed = 10
score_time = True

#while loop and handling input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:  
                player_speed +=9
            if event.key == pygame.K_UP:
                player_speed -=9
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:  
                player_speed -=9
            if event.key == pygame.K_UP:
                player_speed +=9   
                
    #gamelogic           
    ball_animation()
    player_animation()
    opponent_animation()
    
    #visuals
    screen.fill(grey)
    pygame.draw.rect(screen, orange, player)
    pygame.draw.rect(screen, orange, opponent)
    pygame.draw.aaline(screen, white, (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen, orange, ball)
    

    #score time
    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}", False, white)
    screen.blit(player_text,(440,280))
    opponent_text = game_font.render(f"{opponent_score}", False, white)
    screen.blit(opponent_text,(350,280))

    pygame.display.flip()
    clock.tick(60)




    

    



   

