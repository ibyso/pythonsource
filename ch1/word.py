# 영어 타자 프로그램

# word.txt
# 섞는다 random.shuffle()
# 임의로 하나 추출 random.choice()


# Q1) then
# input()
# input 결과에 딸 정답!! or 오타!!

# 문제 5문제 출제
# 정답 출제

# 게임시간 출력
# 출력문 = 게임시간 10초, 정답개수 : 3개
# 3개 이상 정답인 경우 합격 or 불합격

import time
import random

def wordPractice () :
    try :
        with open("./ch1/data/word.txt","r",encoding="utf-8") as f :
            word_list = f.read().splitlines()
    except FileNotFoundError as e :
        print("문제를 호출하는데 실패했습니다.",e)

    q_count = 5
    score = 0
    start = time.time()
    for _ in range(q_count) :
        random.shuffle(word_list)
        que = random.choice(word_list)
        ans = input(f"타자 입력 : {que}\n - ")

        if que.strip() == ans.strip() :
            score += 1
            print("정답!!")
        else :
            print("오답!!")
    end = time.time()

    # total_time = round(end-start,1)
    total_time = format(end-start,".1f")

    print(f"게임 시간 : {total_time}, 정답개수 : {score}개")
    if score >= 3 :
        print("합격")
    else :
        print("불합격")




# 모듈 테스트
if __name__ == "__main__" :
    wordPractice()