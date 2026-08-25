
from sqlalchemy import create_engine, DateTime
from dotenv import load_dotenv
from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Identity
from sqlalchemy.orm import declarative_base
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select

import os

load_dotenv()
password = os.getenv("ORACLE_PASSWORD")
engine = create_engine(f"oracle+oracledb://python_user:{password}@localhost:1521/?service_name=xe",echo=True)

Base = declarative_base()

class Todos(Base) :
    # (선택)테이블명을 클래스명으로 하고싶지 않다면 지정
    __tablename__ = "todos_alchemy"

    # 컬럼 생성
    todo_id:Mapped[int] = mapped_column(Numeric(10,0), Identity(start=1,increment=1),primary_key=True)
    title:Mapped[str] = mapped_column(String(200))
    is_done:Mapped[bool] = mapped_column(default=False)
    # Optional[datetime] : None or datetime일 수도 있음
    created_at:Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self):
        status = "완료" if self.is_done else "미완료"
        return f"<Todos(todo_id={self.todo_id}, title={self.title}, is_done={status},created_at={self.created_at}, )>"
    
Base.metadata.create_all(engine)

# todo 추가
def add_todo():
    title = input("할 일 내용을 입력하세요 : ")
    with Session(engine) as session :
        todo = Todos(title=title)
        session.add(todo)
        session.commit()
        print(f"{todo.todo_id}번이 등록되었습니다.")

def list_todos():
    with Session(engine) as session :
        stmt = select(Todos).order_by(Todos.todo_id)
        rows = session.scalars(stmt).all()
    if not rows : 
        print("등록된 할 일 목록이 없습니다.\n")
        return
    print("-" *20)
    for row in rows :
        print(row)
    print("-" *20)

def update_todo():
    list_todos()
    id = int(input("완료 처리할 일 번호를 입력하세요 : "))
    with Session(engine) as session :
        todo = session.get(Todos,id)
        if todo is None :
            print("해당 번호는 없습니다.")
            return
        todo.is_done = True
        session.commit()
    print("완료 처리되었습니다.\n")

def delete_todo():
    list_todos()
    id = int(input("삭제 처리할 일 번호를 입력하세요 : "))
    with Session(engine) as session :
        todo = session.get(Todos,id)
        if todo is None :
            print("해당 번호는 없습니다.")
            return
        session.delete(todo)
        session.commit()
    print("완료 처리되었습니다.\n")


def menu() :
    while True :
        print("===Todo===")
        print("1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료")
        choice = input("선택 : ")

        if choice == "1" :
            add_todo()
        elif choice == "2" :
            list_todos()
        elif choice == "3" :
            update_todo()
        elif choice == "4" :
            delete_todo()
        elif choice == "5" :
            print("종료합니다.")
            break
        else :
            print("입력 오류")

if __name__ == "__main__":
    menu()