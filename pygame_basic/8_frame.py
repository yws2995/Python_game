import pygame
###############################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################

# 1. 사용자 게임 초기회(배경 화면, 게임 이미지, 좌표, 폰트 등)

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
    
    pygame.display.update()  # 게임 화면을 다시 그리기(계속 해서 호출해야 배경이 나온다 )

# pygame 종료
pygame.quit()
