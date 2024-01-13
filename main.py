import sqlite3
from datetime import datetime


def run():  # 기능 선택
  
  
  con = sqlite3.connect("todoDB.db")
  cur = con.cursor()
  
  banbok = True
  print('exit입력 : 프로그램 종료')
  print('1 : 해야 할 일 작성 \n2 : 전체 출력 \n3 : 특정날짜 todo출력 \n4 : 완료 표시 하기 \n5 : 삭제 하기')
  while(banbok):
    gineung_print = input()
    
    if gineung_print == '1':
      print('해야 할 일 작성')
      set_todo(con, cur)
    if gineung_print == '2':
      print('전체 출력')
      show_ToDo_list(cur, con)
      
    if gineung_print == '3':
      print('특정 날짜 todo 출력')
      show_one_date_todo(cur)
      
    if gineung_print == '4':
      print('완료 표시 하기')
      todo_check(cur, con)
    if gineung_print == '5':
      print('삭제 하기')
      todo_delete(cur, con)
      
    if gineung_print == 'exit':
      print('프로그램을 종료 합니다 :D')
      break
    

def set_todo(con, cur): # to do list 입력
  # while(True):
  print("오늘의 할 일을 작성해주세요")
  print("종료시 'exit' 입력")
  print("예시 : 물리학I 공부, 화학I 공부")
  input_todo = input().split(',')
  
  
    
  print(input_todo)
  today_dates = datetime.today().strftime('%Y/%m/%d')
  
  for todo in input_todo:
    cur.execute(
        f"INSERT INTO todo('created_date', 'contentes') VALUES('{today_dates}', '{todo}')"
    )
    con.commit()
    
    
def show_ToDo_list(cur, con):
    #모든 학생성적 조회
    print("전체 출력")
    
    
    result = cur.execute("SELECT seq, created_date, contentes, done, finish_date FROM todo")
    todo = result.fetchall()
    for data in todo:
        print(data[0], data[1], data[2], data[3])
      
  
def show_one_date_todo(cur):
    
    print("오늘 날짜 todo출력")
    print('예시 : 2024/01/01')
    
    when = input()
    if len(when) == 0:
      when = datetime.today().strftime('%Y/%m/%d')
      
    result = cur.execute(f"SELECT seq, created_date, contentes, done, finish_date FROM todo WHERE created_date = '{when}'")
    
    todo = result.fetchall()
    if len(todo) == 0:
        print("오늘의 할일을 출력 합니다.")
    for data in todo:
        print(data[0], data[1], data[2], data[3])


def todo_check(cur, con):
  print("완료 표시")
  print("시퀀스 입력(가장 맨 앞에 있는 숫자)")
  show_ToDo_list(cur, con)
  
  seq = input()
  print(seq)
  check = cur.execute(f"update todo set done = 1 where seq = {int(seq)}")
  con.commit()
  print('해당 시퀀스의 완료표시가 되었습니다')
  
  
def todo_delete(cur, con):
  show_ToDo_list(cur, con)
  
  print('삭제 할 목록의 시퀀스 입력')
  print("시퀀스 입력(가장 맨 앞에 있는 숫자)")

  delete_seq = input()
  result = cur.execute(f"DELETE from todo where seq = {int(delete_seq)}")
  con.commit()
  print('해당 시퀀스가 삭제 되었습니다.')
  
  

run()