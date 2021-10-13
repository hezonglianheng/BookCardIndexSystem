from tkinter import *
import bookcard
import result
from tkinter.scrolledtext import *
from tkinter.messagebox import *
res = []


def open_window():
    window = Toplevel()
    window.geometry('800x400')
    window.title('读书卡片检索系统-检索卡片')

    mode = IntVar()
    mode.set(0)

    # 函数
    def quit_search():
        is_quit = askyesno('提示','确定要退出吗？')
        if is_quit > 0:
            window.destroy()

    def do_search():
        global res
        if mode.get() == 0:
            s = text.get('1.0',END)[:-1]
            res = bookcard.string_search(s)
        elif mode.get() == 1:
            s = text.get('1.0', END)[:-1]
            res = bookcard.text_search(s)
        else:
            res = bookcard.collect_search()

        if res:
            window.destroy()
            result.open_window()
        else:
            showerror('提示','检索失败，没有匹配信息！')

    # 部件
    frame1 = LabelFrame(window,text='请输入检索内容',
                        font=('微软雅黑',16),width=600,height=200)
    frame1.pack()
    text = ScrolledText(frame1,font=('宋体',16),width=60,height=5)
    text.grid(column=0,row=0)

    frame2 = LabelFrame(window, text='请选择检索模式',
                        font=('微软雅黑', 16),width=400,height=120)
    frame2.pack()
    radio1 = Radiobutton(frame2,text='全部匹配（需输入内容）',
                         variable=mode,value=0,font=('宋体',14))
    radio1.place(x=0,y=0)
    radio2 = Radiobutton(frame2,text='仅文本匹配（需输入内容）',
                         variable=mode,value=1,font=('宋体',14))
    radio2.place(x=0,y=25)
    radio3 = Radiobutton(frame2,text='收藏检索（不需要输入内容）',
                         variable=mode,value=2,font=('宋体',14))
    radio3.place(x=0,y=50)

    button1 = Button(window,height=2,width=8,text='检索',
                     font=('宋体',16),command=do_search)
    button1.pack()
    button2 = Button(window,height=2,width=8,text='退出',
                     font=('宋体',16),command=quit_search)
    button2.pack()

    # 循环
    window.mainloop()


if __name__ == '__main__':
    open_window()
