import pygame
import sys

# Pygame 초기화
pygame.init()

# 상수
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 20
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 10
BALL_RADIUS = 10
BLOCK_ROWS = 5
BLOCK_COLS = 8
BLOCK_GAP = 10

# 게임 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 색상
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 글꼴
font = pygame.font.Font(None, 36)

# 게임 변수 초기화
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
ball_x = WIDTH // 2
ball_y = paddle_y - BALL_RADIUS
ball_dx, ball_dy = 0.3, -0.3  # 공의 이동 속도를 4배 느리게 조정
blocks = []

for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(
            col * (BLOCK_WIDTH + BLOCK_GAP) + BLOCK_GAP,
            row * (BLOCK_HEIGHT + BLOCK_GAP) + BLOCK_GAP,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
        )
        blocks.append(block)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 0.5
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += 0.5

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공 충돌 처리
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # 패들 충돌 처리
    if (
        paddle_y - BALL_RADIUS <= ball_y <= paddle_y
        and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH
    ):
        ball_dy = -ball_dy

    # 블록 충돌 처리
    for block in blocks:
        if block.colliderect(ball_x, ball_y, BALL_RADIUS * 2, BALL_RADIUS * 2):
            ball_dy = -ball_dy
            blocks.remove(block)

    # 게임 오버 조건
    if not blocks:
        text = font.render("게임 승리!", True, RED)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # 화면 지우기
    screen.fill(BLACK)

    # 패들 그리기
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # 공 그리기
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # 블록 그리기
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
