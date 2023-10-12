import pygame
import math

# 파이게임 모듈 초기화
pygame.init()
# 로고 로드하고 세팅
logo = pygame.image.load("logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Drifting Car")

# 240 x 180 사이즈의 스크린 표면을 만듦
screen = pygame.display.set_mode((600, 600))

# 자동차 로드
car = pygame.image.load('car.png')
car_x = 0
car_y = 0
car_r = 230
car_v_x = 0
car_v_y = 0
car_a = 0.1

# 메인 루프를 제어할 변수 정의
running = True

# 메인 루프
while running:
    # 이벤트 핸들러, 이벤트 큐로부터 모든 이벤트를 얻는다.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car_v_x += car_a * math.cos(math.radians(car_r))
                car_v_y += car_a * math.sin(math.radians(car_r))gig
        # QUIT 타입의 이벤트라면 다음 코딩을 실행
        if event.type == pygame.QUIT:
            # 메인 루프를 탈출하기 위해 변수를 False 로 바꾼다.
            running = False

    print(car_v_x, car_v_y)
    # screen.blit(car, (car_x, car_y))

    pygame.display.update()