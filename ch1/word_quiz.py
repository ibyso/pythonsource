import csv
import oracledb
import random

conn = oracledb.connect(user='python_user',password="54321",dsn="localhost/xe")
cursor = conn.cursor()

# csv 파일의 내용을 테이블에 insert하기 (단, 테이블이 비어있는 경우에만 삽입)
def load_words_from_csv (path="./ch1/data/words.csv") :
    data = []
    with open(path,"r",encoding="utf-8") as f :
        reader = csv.DictReader(f)

        for row in reader:
            data.append((
                row["word"].strip(),
                row.get("meaning").strip()
            ))
    return data

def select_words() :
    sql = "select * from words"
    cursor.execute(sql)
    return cursor.fetchall() 

def seed_words_if_empty():
    # words 테이블이 비어있으면 csv 파일 내용 읽어서 넣기
    rows = select_words()
    if not rows : 
        data = load_words_from_csv()
        sql = "insert into words(word, meaning) values (:1, :2)"
        cursor.executemany(sql,data)
        conn.commit()
        rows = select_words()
    return rows

def add_quiz_result (total,correct) :
    sql = "insert into quiz_records (total, correct) values (:1, :2)"
    cursor.execute(sql,(total,correct))
    conn.commit()
    print(f"데이터 {cursor.rowcount}개가 저장되었습니다.")

def run_quiz():
    # 1) words 테이블 읽기
    # 2) 무작위 문제 추출 random.sample()
    # 3) all_words 문제 제외한 내용을 섞은 후 틀린 meaning 3개 추출
    # 4) 답변 입력반은 후 정답 체크

    all_data = seed_words_if_empty()
    total = 5
    count = 0
    correct = 0
    while True :
        quiz = random.sample(all_data, 4)

        print(f"[문제{count+1}]. {quiz[0][1]} ")
        result = quiz[0][2]
        random.shuffle(quiz)
        for idx, e in enumerate(quiz,start=1 ): 
            print(f"{idx}. {e[2]} ")
        
        # answer = input("정답(번호말고 직접 입력) : ")
        # if answer == result :
        #     correct += 1
        answer = int(input("정답 : ").strip())
        if quiz[answer-1][2] == result :
            correct +=1

        print("\n"+"="*10+"\n")
        count += 1
        if count == total :
            print(f"결과 : {correct} / {total}")
            add_quiz_result(total,correct)
            print("종료")
            break


# 테이블의 내용을 읽어서 섞은 후 문제 내기
# apple => 사과

# 결과 : 3 / 5 정답

# 결과를 테이블에 저장하기
# total, correct,regdate


if __name__ == "__main__" :
    try:
        run_quiz()
    finally :
        cursor.close()
        conn.close()