import oracledb
from datetime import datetime

conn = oracledb.connect(user='python_user',password="54321",dsn="localhost/xe")
cursor = conn.cursor()


def add_transactions() :
    sql = "insert into transactions(tx_type,amount,memo,reg_date) values (:1, :2, :3, :4)"
    tx_type = input("수입/지출을 입력하세요 : ").strip()
    amount = input("금액을 입력하세요 : ").strip()
    memo = input("메모를 입력하세요 : ").strip()
    reg_date = input("날짜을 입력하세요 (YYYY-MM-DD, 엔터시 오늘) : ").strip()
    if not reg_date :
        reg_date = datetime.now().strftime("%Y-%m-%d")

    try : 
        cursor.execute(sql,(tx_type,amount,memo,reg_date))
        conn.commit()
        print("등록되었습니다.\n")
    except oracledb.Error as e :
        print("등록 실패.")

def list_transactions() :
    # reg_date asc
    # 번호 [지출] 300000원 - 용돈(2026-08-18)
    sql = "select * from transactions order by reg_date"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if not rows : 
        print("등록된 가계부 내용이 없습니다.\n")
        return
    print("-" *20)
    for row in rows :
        print(f"{row[0]}. [{row[1]}] {row[2]}원 - {row[3]}({row[4]})")
    print("-" *20)

def monthly_summary() :
    month = input("조회 할 년월을 입력하세요 : ").strip()
    month_like = f"{month}%"
    sql = "select tx_type,sum(amount) from transactions where reg_date like :1 group by tx_type"
    cursor.execute(sql,(month_like,))
    rows = cursor.fetchall()
    if not rows : 
        print("등록된 가계부 내용이 없습니다.\n")
        return
    print("-" *20)
    for row in rows :
        print(f"[{row[0]}] {row[1]}원")
    print("-" *20)


def menu() :
    # 1.내역 추가 2. 전체 조회 3. 월별 합계 4. 종료
    while True :
            print("===가계부 기록===")
            print("1.내역 추가  2.전체 조회  3.월별 합계  4.종료")
            choice = input("선택 : ")
    
            if choice == "1" :
                add_transactions()
            elif choice == "2" :
                list_transactions()
            elif choice == "3" :
                monthly_summary()
            elif choice == "4" :
                print("종료합니다.")
                break
            else :
                print("입력 오류")





if __name__ == "__main__":
    try :
        menu()

    finally :
        cursor.close()
        conn.close()