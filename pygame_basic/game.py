import random
import pygame 

pygame.init() #초기화

# 화면 크기 설정
screen_width=480 #가로 크기 설정
screen_height=640 #세로 크기 설정
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("26tools project") #게임 이름

#fps
clock = pygame.time.Clock()

#배경 이미지 불러우기
background=pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/Slopes.png")

#캐릭터 불러오기
character=pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/penguin2-a.svg")
character_size= character.get_rect().size 
character_width=character_size[0]
character_height=character_size[1] 
character_x_pos=screen_width/2 -(character_width/2) 
character_y_pos=screen_height -character_height

# 이동할 위치
to_x=0

#이동 속도
character_speed = 0.8

#장애물 불러오기
ball =pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/sun.svg")
ball_width=character_size[0]
ball_height=character_size[1] 
ball_x_pos=random.randint(0,screen_width - ball_width+1)
ball_y_pos=3
ball_speed=15


# 폰트 정의
game_font = pygame.font.Font(None,40) #(폰트,크기)

game_result="Game Over"

#총 시간
total_time =10

# 시작 시간 정보
star_ticks = pygame.time.get_ticks() #시작 tick 정보를 받아오기




# 이벤트 루프(게임이 꺼지지 않도록 함)
running= True #게임이 진행중인가?
while running:
    dt=clock.tick(50)   #게임화면의 초당 프레임 수를 설정
    #print("fps: "+ str(clock.get_fps()))
    
    #2.이벤트 처리(키보드, 마우스)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: # 창닫기 버튼(창닫기 이벤트)가 발생하였는가
            running=False #게임이 진행중이 아님
    
        if event.type== pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed *dt
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed *dt
            

        if event.type ==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    #3. 게임 캐릭터 위치 
    character_x_pos += to_x
    
     #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width - character_width:
        character_x_pos= screen_width - character_width

    ball_y_pos += ball_speed

    if ball_y_pos > screen_height:
        ball_y_pos=0
        ball_x_pos=random.randint(0,screen_width - ball_width)

    #4. 충동 처리를 위한 사각형 정보 불러오기
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    #충돌 체크
    if character_rect.colliderect(ball_rect):
        print("실패!")
        running = False


    #5. 화면에 그리기
    screen.blit(background,(0,0)) #배경 그리기+fill로 색깔집어넣어도 가능

    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    
    screen.blit(ball,(ball_x_pos,ball_y_pos)) #적 그리기

    # 타이머 넣기
    # 경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()- star_ticks)/1000 #경과 시간을 초 단위로 표시

    timer= game_font.render("Time :{}".format(int(total_time- elapsed_time)),True,(0,255,64)) #(시간정보,True,글자 색상)
    screen.blit(timer,(10,10))

     #시간 제한
    if total_time-elapsed_time <=0:
        game_result = "Mission complete"
        running= False

    pygame.display.update() #게임 화면에 이미지 표시하기


msg=game_font.render(game_result,True,(255,255,0))
msg_rect=msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

# 잠시 대기
pygame.time.delay(1000) #2초 정도 대기

# pygame 종료
pygame.quit()
