import tkinter as tk
from tkinter import ttk
import threading,time,pyautogui,keyboard #라이브러리 pyautogui는 마우스 제어,keyboard는 키보드제어로  2개는 추가

실행=False

def 작업():
    global 실행
    while True:
        if 실행:
            try:
                if 마우스위치.get()=="특정위치":
                    x=int(x값.get()); y=int(y값.get())
                else:
                    x, y = pyautogui.position()
                pyautogui.moveTo(x,y)

                동작=클릭종류.get()
                if 동작=="좌클릭": pyautogui.click(button="left")
                elif 동작=="우클릭": pyautogui.click(button="right")
                elif 동작=="더블클릭": pyautogui.doubleClick()
                elif 동작=="키 입력":
                    keyboard.write(입력문자.get())
                elif 동작=="단축키":
                    keys=[k.strip() for k in 입력문자.get().split("+")]
                    keyboard.press_and_release("+".join(keys))
                time.sleep(float(간격.get()))
            except:
                pass

def 시작():
    global 실행
    실행=True
    상태["text"]="상태 : 실행 중"
def 정지(): 
    global 실행
    실행=False
    상태["text"]="상태 : 정지"


#창UI
창=tk.Tk()
창.title("오토마우스 + 키보드")
마우스위치=tk.StringVar(value="현재위치")
x값=tk.StringVar(value="100")
y값=tk.StringVar(value="100")
간격=tk.StringVar(value="1")
입력문자=tk.StringVar()
클릭종류=tk.StringVar(value="좌클릭")

#마우스위치
ttk.Label(창,text="마우스위치").pack()
ttk.Combobox(창,textvariable=마우스위치,
values=["현재위치","특정위치"]).pack(fill="x",padx=2)

#마우스 고정위치, 간격, 단축기설정, 입력문자설정
for t,v in [("X좌표",x값),("Y좌표",y값),("간격(초)",간격),("입력 문자/단축키",입력문자)]:
    ttk.Label(창,text=t).pack()
    ttk.Entry(창,textvariable=v).pack(fill="x",padx=5)



#자동으로 할 동작
ttk.Label(창,text="동작").pack()
ttk.Combobox(창,textvariable=클릭종류,
values=["좌클릭","우클릭","더블클릭","키 입력","단축키"]).pack(fill="x",padx=5)

#단축기버튼
ttk.Button(창,text="시작(F8)",command=시작).pack(fill="x")
ttk.Button(창,text="정지(F9)",command=정지).pack(fill="x")
ttk.Button(창,text="종료(Esc)",command=창.destroy).pack(fill="x")
상태=ttk.Label(창,text="상태 : 정지")
상태.pack()

#단축기
threading.Thread(target=작업,daemon=True).start()
keyboard.add_hotkey("F8",시작)
keyboard.add_hotkey("F9",정지)
keyboard.add_hotkey("esc",창.destroy)
창.mainloop()

