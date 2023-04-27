# 로또 번호 만들기

import tkinter
import tkinter.font
import random # 숫자 랜덤으로 나오게 하기

lotto_num = range(1,46) # 범위는 1~46 까지 랜덤으로 나오게 하기

def buttonClick():
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6))) # 버튼 클릭하면 라벨 안에 숫자가 6자리 숫자 나오게하기
    label.pack()

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200") # 창 사이즈
window.resizable(False, False) # 창 사이즈 건드는것

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()