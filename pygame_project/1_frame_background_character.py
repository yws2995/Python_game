import pygame
import os
###############################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Pang")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################

# 1. 사용자 게임 초기회(배경 화면, 게임 이미지, 좌표, 폰트 등)

current_path = os.path.dirname(__file__)  # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images")  # image 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 공이 튀길 높이나 캐릭터 위치를 위한 설정

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


# 이벤트 루프

running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():    # 이벤트 루프는 프로그램이 종료되지 않도록 한다. 동작을 체크한다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임 화면을 다시 그리기(계속 해서 호출해야 배경이 나온다 )


# pygame 종료
pygame.quit()
