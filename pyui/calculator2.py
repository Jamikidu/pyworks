# 계산기

from tkinter import *



root = Tk()
root.title("나의 계산기")

# top_row 프레임 - 입력창
top_row = Frame(root)
top_row.grid(row=0, column=0, sticky=N) #N-North(북쪽)
display = Entry(top_row, width=50, bg='lightgreen')
display.grid(row=0, column=0)

# num_pad 프레임 - 숫자 버튼
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W) #W-West(서쪽)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]
r = 0
c = 0
for btn_text in num_pad_list:
    Button(num_pad, width=4, height=2, text=btn_text).grid(row=r, column=c)
    c += 1
    if c > 2:  # column이 2(3열)보다 크면 0(1열)으로 설정
        c = 0
        r = r + 1  # row(행) 1증가

root.mainloop()