import pygame
import random
###############################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Quiz")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################

# 1. 사용자 게임 초기회(배경 화면, 게임 이미지, 좌표, 폰트 등)
# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\Users\\여운석\\Documents\\Python_game\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load(
    "C:\\Users\\여운석\\Documents\\Python_game\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구함
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# character 이동 속도
character_speed = 10

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "C:\\Users\\여운석\\Documents\\Python_game\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():    # 이벤트 루프는 프로그램이 종료되지 않도록 한다. 동작을 체크한다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, (screen_width - enemy_width))
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    pygame.display.update()  # 게임 화면을 다시 그리기(계속 해서 호출해야 배경이 나온다 )

# pygame 종료
pygame.quit()
