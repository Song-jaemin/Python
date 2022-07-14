import pygame 

#pygame 라이브러리 사용, 초기화,  게임 기본 설정(가로,세로 크기, 게임 타이틀,게임 종료 설정 코드 만들기,게임 배경 불러오기)
pygame.init() #초기화
# 화면 크기 설정
screen_width=480 #가로 크기 설정
screen_height=640 #세로 크기 설정
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("26tools project") #게임 이름

#배경 이미지 불러우기
background=pygame.image.load("C:/Users/82109/Desktop/python workspace/pygame_basic/background.png")


# 이벤트 루프(게임이 꺼지지 않도록 함)
running= True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: # 창닫기 버튼(창닫기 이벤트)가 발생하였는가
            running=False #게임이 진행중이 아님
    screen.blit(background,(0,0)) #배경 그리기

    pygame.display.update() #게임 화면을 다시 그리기
    
# pygame 종료
pygame.quit()