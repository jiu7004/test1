import random

def random_draw():

    candidates = []
    
    print("추첨 대상 (마지막 요소 작성 이후 '..' 입력): ")
    while True:
        candidate = input()
        if candidate == '..':
            break
        candidates.append(candidate)
    
    num_winners = int(input("몇 명을 추첨할까요? "))
    

    if num_winners > len(candidates):
        print("추첨 인원 수가 추첨 대상 수보다 많습니다.")
        return
    
    winners = random.sample(candidates, num_winners)
    print(f"추첨 결과: {', '.join(winners)}")

# 함수 실행
random_draw()

#이벤트를 위한 랜덤 뽑기 프로그램