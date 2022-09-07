import pygame 
 #기본 초기화 부분(필수!!)

#pygame 라이브러리 사용, 초기화,  게임 기본 설정(가로,세로 크기, 게임 타이틀,게임 종료 설정 코드 만들기,게임 배경 불러오기,캐릭터 움직이기,게임 회면 조절하기,FPS 설정)
###########################################################
pygame.init() #초기화

# 화면 크기 설정
screen_width=480 #가로 크기 설정
screen_height=640 #세로 크기 설정
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("26 tools project") #게임 이름

#FPS
clock = pygame.time.Clock()
############################################################


#1. 사용자 게임 초기화(배경, 게임 이미지, 좌표, 폰트, 속도 ...)

#배경 이미지 불러우기
background=pygame.image.load()

#캐릭터 불러오기
character=pygame.image.load()
character_size= character.get_rect().size #이미지의 크기를 구해옴
character_width=character_size[0] #캐릭터의 가로 크기 첫번째 값
character_height=character_size[1] #캐릭터의 세로 크기 두번째 값
character_x_pos=0
character_y_pos=0

# 이동할 좌표
to_x=0
to_y=0

#이동 속도
character_speed = 5

# 적 캐릭터 불러오기
enemy=pygame.image.load()
enemy_size= character.get_circle().size #이미지의 크기를 구해옴
enemy_width=character_size[0] #캐릭터의 가로 크기
enemy_height=character_size[1] #캐릭터의 세로 크기
enemy_x_pos=0
enemy_y_pos=0

# 폰트 정의
game_font = pygame.font.Font() #(폰트,크기)

#총 시간
total_time =0

# 시작 시간 정보
star_ticks = pygame.time.get_ticks() #시작 tick 정보를 받아오기


# 이벤트 루프(게임이 꺼지지 않도록 함)
running= True #게임이 진행중인가?
while running:
    dt=clock.tick(80)   #게임화면의 초당 프레임 수를 설정
    #print("fps: "+ str(clock.get_fps()))

    #2. 이벤트 처리(키보드, 마우스...)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: # 창닫기 버튼(창닫기 이벤트)가 발생하였는가
            running=False  #게임이 진행중이 아님
    
        if event.type== pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로
                to_y += character_speed

        if event.type ==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key ==pygame.K_UP or event.key== pygame. K_DOWN:
                to_y=0
    
    #3.게임 캐릭터 위치 정의
    character_x_pos += to_x
    character_y_pos += to_y

    #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width - character_width:
        character_x_pos= screen_width - character_width

    #세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height - character_height:
        character_y_pos= screen_height - character_height


    # 충동 처리를 위한 사각형 정보 불러오기
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_circle = enemy.get_rect()
    enemy_circle.left = enemy_x_pos
    enemy_circle.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_circle):
        print("실패!")
        running = False


    #5. 화면에 그리기
    screen.blit(background,(0,0)) #배경 그리기+fill로 색깔집어넣어도 가능

    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기

    # 타이머 넣기
    # 경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()- star_ticks)/1000 #경과 시간을 초 단위로 표시

    timer= game_font.render(str(int(total_time- elapsed_time)),True,(0,255,64)) #(시간정보,True,글자 색상)
    screen.blit(timer,(10,10))

     #시간 제한
    if total_time-elapsed_time<=0:
        print("타임 아웃")
        running= False

    pygame.display.update() #게임 화면을 다시 그리기

# 잠시 대기
pygame.time.delay(1000) #2초 정도 대기

# pygame 종료
pygame.quit()
 