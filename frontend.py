# coding:utf-8
import tkinter.messagebox
from tkinter import *
import bookcard
import aboutus
import addcard
import search_card


class BookCard:
    def __init__(self, window):
        # bookcard.database_build()
        self.window = window
        self.window.geometry('1200x600+0+0')
        self.window.title('读书卡片索引系统')

        # 函数
        def window_close():
            is_close = tkinter.messagebox.askyesno(
                '读书卡片索引系统',
                '未保存的操作将消失！\n您确定要退出吗？')
            if is_close > 0:
                window.destroy()

        def reset():
            is_reset = tkinter.messagebox.askyesno('警告',
                                                   '重置后，之前的记录将无法恢复！\n您确定要重置吗？')
            if is_reset > 0:
                bookcard.rebuild()
                tkinter.messagebox.showinfo('提示','重置成功！')

        def open_about_us():
            self.window.iconify()
            aboutus.open_window()

        def open_search_card():
            self.window.iconify()
            search_card.open_window()

        def open_addcard():
            self.window.iconify()
            addcard.open_window()

        # 桌面部件
        label = Label(window, text='欢迎使用读书卡片索引系统',
                      font=('华文新魏', 36))
        label.pack()

        button1 = Button(height=2, width=10, text='制作卡片',
                         font=('宋体', 20),
                         command=open_addcard)
        button1.place(x=400, y=200)

        button2 = Button(height=2, width=10, text='搜索卡片',
                         font=('宋体', 20),
                         command=open_search_card)
        button2.place(x=650, y=200)

        button3 = Button(height=2, width=10, text='退出系统',
                         font=('宋体', 20), command=window_close)
        button3.place(x=400, y=400)

        button4 = Button(height=2, width=10, text='关于我们',
                         font=('宋体', 20),
                         command=open_about_us)
        button4.place(x=650, y=400)

        button5 = Button(height=2, width=10, text='重置系统',
                         font=('宋体', 20),command=reset)
        button5.place(x=400, y=300)

        button6 = Button(height=2, width=10, text='使用说明',
                         font=('宋体', 20))
        button6.place(x=650, y=300)


if __name__ == '__main__':
    window = Tk()
    database = BookCard(window)
    window.mainloop()
