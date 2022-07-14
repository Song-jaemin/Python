import pygame 

#pygame 라이브러리 사용, 초기화,  게임 기본 설정(가로,세로 크기, 게임 타이틀,게임 종료 설정 코드 만들기)
pygame.init() #초기화
# 화면 크기 설정
screen_width=480 #가로 크기 설정
screen_height=640 #세로 크기 설정
pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("26tools project") #게임 이름

# 이벤트 루프(게임이 꺼지지 않도록 함)
running= True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: # 창닫기 버튼(창닫기 이벤트)가 발생하였는가
            running=False #게임이 진행중이 아님

# pygame 종료
pygame.quit()