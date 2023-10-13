import pygame
import math

# 파이게임 모듈 초기화
pygame.init()
# 로고 로드하고 세팅
logo = pygame.image.load("logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Drifting Car")

# 240 x 180 사이즈의 스크린 표면을 만듦
SCREEN_SIZE = (600,600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 자동차 로드
car = {
    'original_image': pygame.image.load('car.png'),
    'x': SCREEN_SIZE[0] / 2,
    'y': SCREEN_SIZE[1] / 2,
    'r': 0,
    'v': {
        'x': 0,
        'y': 0,
        'r': 0.1
    },
    'a': 0.0005,
    'ff': 1.001
}

# 메인 루프를 제어할 변수 정의
running = True

# 메인 루프
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car['v']['x'] += car['a'] * math.cos(math.radians(car['r']))
        car['v']['y'] += car['a'] * math.sin(math.radians(car['r']))
    if keys[pygame.K_DOWN]:
        car['v']['x'] -= car['a'] * math.cos(math.radians(car['r']))
        car['v']['y'] -= car['a'] * math.sin(math.radians(car['r']))
    if keys[pygame.K_LEFT]:
        car['r'] += car['v']['r']
    if keys[pygame.K_RIGHT]:
        car['r'] -= car['v']['r']

    # 이벤트 핸들러, 이벤트 큐로부터 모든 이벤트를 얻는다.
    for event in pygame.event.get():
        # QUIT 타입의 이벤트라면 다음 코딩을 실행
        if event.type == pygame.QUIT:
            # 메인 루프를 탈출하기 위해 변수를 False 로 바꾼다.
            running = False

    car['v']['x'] /= car['ff']
    car['v']['y'] /= car['ff']
    car['x'] += car['v']['x']
    car['y'] -= car['v']['y']

    car['image'] = pygame.transform.rotate(car['original_image'], car['r'])
    car['rect'] = car['image'].get_rect(center = (car['x'], car['y']))

    screen.fill((0,0,0))
    screen.blit(car['image'], car['rect'])

    pygame.display.update()

pygame.quit()