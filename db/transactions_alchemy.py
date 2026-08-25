from sqlalchemy import create_engine, DateTime
from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Identity
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import func
from typing import Optional

from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("ORACLE_PASSWORD")
engine = create_engine(f"oracle+oracledb://python_user:{password}@localhost:1521/?service_name=xe",echo=True)

Base = declarative_base()

class Transactions(Base) :
    # (선택)테이블명을 클래스명으로 하고싶지 않다면 지정
    __tablename__ = "transactions_alchemy"

    # 컬럼 생성
    tx_id:Mapped[int] = mapped_column(Numeric(10,0), Identity(start=1,increment=1),primary_key=True)
    tx_type:Mapped[str] = mapped_column(String(10))
    amount:Mapped[int] = mapped_column(Numeric(11,0))
    memo:Mapped[str] = mapped_column(String(2000))
    # Optional[datetime] : None or datetime일 수도 있음
    # reg_date:Mapped[Optional[datetime]] = mapped_column(DateTime)
    reg_date:Mapped[str] = mapped_column(String(20))
    def __repr__(self):
        return f"<Transactions({self.tx_id}. [{self.tx_type}] {self.amount}원 - {self.memo}({self.reg_date}) )>"
    
Base.metadata.create_all(engine)


def add_transactions() :
    tx_type = input("수입/지출을 입력하세요 : ").strip()
    amount = input("금액을 입력하세요 : ").strip()
    memo = input("메모를 입력하세요 : ").strip()
    reg_date = input("날짜을 입력하세요 (YYYY-MM-DD, 엔터시 오늘) : ").strip()
    if not reg_date :
        reg_date = datetime.now().strftime("%Y-%m-%d")
    with Session(engine) as session :
            transaction = Transactions(tx_type=tx_type,amount=amount,memo=memo,reg_date=reg_date)
            session.add(transaction)
            session.commit()
            print(f"{transaction.tx_id}번이 등록되었습니다.")
    

def list_transactions() :
    # reg_date asc
    # 번호 [지출] 300000원 - 용돈(2026-08-18)
    with Session(engine) as session :
        stmt = select(Transactions).order_by(Transactions.reg_date)
        rows = session.scalars(stmt).all()
        if not rows : 
            print("등록된 가계부 내용이 없습니다.\n")
            return
        print("-" *20)
        for row in rows :
            print(row)
        print("-" *20)

def monthly_summary() :
    month = input("조회 할 년월을 입력하세요 : ").strip()
    with Session(engine) as session :
        stmt = select(Transactions.tx_type,func.sum(Transactions.amount).label("total")).where(Transactions.reg_date.like(month+"%")).group_by(Transactions.tx_type)
        rows = session.execute(stmt).all()
        if not rows : 
            print("등록된 가계부 내용이 없습니다.\n")
            return
        print("-" *20)
        for row in rows :
            print(f"{month}.[{row.tx_type}] {row.total}원")
        print("-" *20)

        # 2안
        # transactions = (session.query(Transactions.tx_type, func.sum(Transactions.amount)).filter(Transactions.reg_date.like(month+'%')).group_by(Transactions.tx_type))
        # for tx_type, total in transactions :
        #     print(f"{tx_type} : {total}")


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
    menu()