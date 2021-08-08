import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")  # 게임 이름


# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\Users\\여운석\\Documents\\Python_game\\pygame_basic\\background.png")
# 이벤트 루프가 실행되어야 창이 꺼지지 않는다.
# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 이벤트 루프는 프로그램이 종료되지 않도록 한다. 동작을 체크한다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님
    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))  # 배경 그리기

    pygame.display.update()  # 게임 화면을 다시 그리기(계속 해서 호출해야 배경이 나온다 )
# pygame 종료
pygame.quit()
