from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import pygame 

#pygame 라이브러리 사용, 초기화,  게임 기본 설정(가로,세로 크기, 게임 타이틀,게임 종료 설정 코드 만들기,게임 배경 불러오기,캐릭터 움직이기,게임 회면 조절하기)
pygame.init() #초기화
# 화면 크기 설정
screen_width=480 #가로 크기 설정
screen_height=640 #세로 크기 설정
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("26tools project") #게임 이름

#배경 이미지 불러우기
background=pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/background.png")

#캐릭터 불러오기
character=pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/character.png")
character_size= character.get_rect().size #이미지의 크기를 구해옴
character_width=character_size[0] #캐릭터의 가로 크기
character_height=character_size[1] #캐릭터의 세로 크기
character_x_pos=screen_width/2 -(character_width/2) #화면 가로 길이의 절반에 해당하는 곳에 위치
character_y_pos=screen_height -character_height #화면 세로 길이가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x=0
to_y=0

# 이벤트 루프(게임이 꺼지지 않도록 함)
running= True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: # 창닫기 버튼(창닫기 이벤트)가 발생하였는가
            running=False #게임이 진행중이 아님
    
        if event.type== pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= 2 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += 2
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로
                to_y -= 2
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로
                to_y += 2

        if event.type ==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key ==pygame.K_UP or event.key== pygame. K_DOWN:
                to_y=0

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
    screen.blit(background,(0,0)) #배경 그리기+fill로 색깔집어넣어도 가능

    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    pygame.display.update() #게임 화면을 다시 그리기

# pygame 종료
pygame.quit()