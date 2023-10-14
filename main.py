import pygame
import math

# 변수
BLACK = (0, 0, 0)

# 파이게임 모듈 초기화
pygame.init()
clock = pygame.time.Clock()

# 로고 로드하고 세팅
logo = pygame.image.load("logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Drifting Car")

# 스크린 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

# 자동차 로드
class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y, r, v_x, v_y, v_r, a, ff):
        super().__init__()
        self.image_original = pygame.image.load(image)
        self.x = x
        self.y = y
        self.r = r
        self.v_x = v_x
        self.v_y = v_y
        self.v_r = v_r
        self.a = a
        self.ff = ff

car = Car('car.png', 
          SCREEN_WIDTH / 2, 
          SCREEN_HEIGHT / 2,
          0,
          0,
          0,
          3,
          0.3,
          1.03
          )

# 메인 루프를 제어할 변수 정의
running = True

# 메인 루프
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car.v_x += car.a * math.cos(math.radians(car.r))
        car.v_y += car.a * math.sin(math.radians(car.r))
    # if keys[pygame.K_DOWN]:
    #     car.v_x -= car.a * math.cos(math.radians(car.r))
    #     car.v_y -= car.a * math.sin(math.radians(car.r))
    if keys[pygame.K_LEFT]:
        car.r += car.v_r
    if keys[pygame.K_RIGHT]:
        car.r -= car.v_r

    # 이벤트 핸들러, 이벤트 큐로부터 모든 이벤트를 얻는다.
    for event in pygame.event.get():
        # QUIT 타입의 이벤트라면 루프를 마친다.
        if event.type == pygame.QUIT:
            running = False

    # 마찰력 구현
    car.v_x /= car.ff
    car.v_y /= car.ff
    # 움직임 구현
    car.x += car.v_x
    car.y -= car.v_y

    # 회전 구현
    car.image = pygame.transform.rotate(car.image_original, car.r)
    car.rect = car.image.get_rect(center = (car.x, car.y))

    # 화면 끝에 닿았는지 체크
    if abs(car.x - SCREEN_WIDTH / 2) >= (SCREEN_WIDTH / 2 - car.rect.width / 2) or\
        abs(car.y - SCREEN_HEIGHT / 2) >= (SCREEN_HEIGHT / 2 - car.rect.height / 2):
        pass # 꽥

    screen.fill(BLACK)
    screen.blit(car.image, car.rect)

    # 화면 업데이트
    pygame.display.update()
    # FPS
    clock.tick(60)

pygame.quit()