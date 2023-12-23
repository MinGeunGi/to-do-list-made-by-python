import sqlite3



def run():  # 기능 선택
  banbok = True
  
  con = sqlite3.connect("todoDB.db")
  cur = con.cursor()
  
  print('exit입력 : 프로그램 종료')
  print('1 : 해야 할 일 작성 \n2 : 완료 표시 \n3 : 특정날짜 조회 \n4 : 해야 할 일 삭제 \n5 : 해야 할 일 수정')
  while(banbok):
    gineung_print = input()
    
    if gineung_print == '1':
      print('해야 할 일 작성')
      
    if gineung_print == '2':
      print('완료 표시')
      
    if gineung_print == '3':
      print('특정 날짜 조회')
      
    if gineung_print == '4':
      print('해야 할 일 삭제')
      
    if gineung_print == '5':
      print('해야 할 일 수정')
      
    if gineung_print == 'exit':
      print('프로그램을 종료 합니다 :D')
      break
    

def set_todo(): # to do list 입력
  pass
  #cur.execute(
  #      f"INSERT INTO score VALUES('{input_value[0]}', '{input_value[1]}', '{input_value[2]}', '{input_value[3]}', '{input_value[4]}')"
   # )
    #con.commit()
    #con.close()

run()