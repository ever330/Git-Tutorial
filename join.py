import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *

user_file = "user.txt"


user_join = Tk()
user_join.title("회원가입")
user_join.geometry("400x280")

labelID_join = Label(user_join, text="아이디")
labelID_join.place(x=70, y=50)
labelPW1_join = Label(user_join, text="비밀번호")
labelPW1_join.place(x=70, y=80)
labelPW2_join = Label(user_join, text="비밀번호 확인")
labelPW2_join.place(x=70, y=110)
labelsex_join = Label(user_join, text="성별")
labelsex_join.place(x=70, y=140)
labelsex_join = Label(user_join, text="생년월일")
labelsex_join.place(x=70, y=170)

ID_join = Entry(user_join, width=20) # 아이디 입력
ID_join.place(x=160, y=50)
PW1_join = Entry(user_join, width=20) # 비밀번호 입력
PW1_join.place(x=160, y=80)
PW2_join = Entry(user_join, width=20) # 비밀번호 확인 입력
PW2_join.place(x=160, y=110)

sex_var = StringVar()
btn_sex1 = Radiobutton(user_join, text="남자",value="남자", variable=sex_var)
btn_sex1.select() # 기본값
btn_sex2 = Radiobutton(user_join, text="여자",value="여자", variable=sex_var)
btn_sex1.place(x=160, y=140)
btn_sex2.place(x=220, y=140)

values1 = [str(i) + "년" for i in range(1950, 2022)] # 연도 지정
yearbox = ttk.Combobox(user_join, height=5, values=values1) 
yearbox.place(x=160, y=170, width=70)

values2 = [str(i) + "월" for i in range(1, 13)] # 월 지정
monthbox = ttk.Combobox(user_join, height=5, values=values2) 
monthbox.place(x=235, y=170, width=50)

values3 = [str(i) + "일" for i in range(1, 32)] # 일 지정
daybox = ttk.Combobox(user_join, height=5, values=values3) 
daybox.place(x=290, y=170, width=55)

def mk(): # 메모장 형태로 유저 정보 생성
    with open(user_file, "w", encoding="utf8") as user:
        user.write("아이디 : {}".format(ID_join.get()))
        user.write("\n비밀번호 : {}".format(PW2_join.get()))
        user.write("\n성별 : {}".format(sex_var.get()))
        user.write("\n생년월일 : {0} {1} {2}".format(yearbox.get(), \
            monthbox.get(), daybox.get()))
        user.close()
        user_join.quit()

btnOK = Button(user_join, text="생성", command=mk)
btnOK.place(x=180, y=230)

user_join.mainloop()