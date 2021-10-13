# coding:utf-8
import tkinter.messagebox
from tkinter import *
import bookcard
from tkinter.scrolledtext import *


def open_window():
    window = Toplevel()
    window.geometry('1200x600')
    window.title('读书卡片索引系统-制作卡片')

    collection = IntVar()
    collection.set(0)

    # 函数
    def clean_input():
        text1.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0',END)
        text6.delete(0,END)
        text7.delete(0,END)
        text8.delete(0,END)
        text9.delete(0,END)
        text10.delete(0,END)
        text11.delete('1.0',END)

    def get_input():
        card_text = text1.get('1.0', END)
        author = text2.get('1.0', END)
        name = text3.get('1.0', END)
        publish = text4.get('1.0', END)
        ways = text5.get('1.0',END)
        tag1 = text6.get()
        tag2 = text7.get()
        tag3 = text8.get()
        tag4 = text9.get()
        tag5 = text10.get()
        thought = text11.get('1.0',END)
        return card_text, author, name, publish, ways, \
               tag1, tag2, tag3, tag4, tag5, thought

    def clean():
        is_clean = tkinter.messagebox.askyesno('警告',
                                               '未保存的记录将消失！\n您确定要删除记录吗？')
        if is_clean > 0:
            clean_input()

    def close():
        is_close = tkinter.messagebox.askyesno('警告','未保存的记录将消失！\n您确定要退出编辑吗？')
        if is_close > 0:
            window.destroy()

    def save():
        is_save = tkinter.messagebox.askyesno('提示','您确定要保存吗？')
        if is_save and text1.get('1.0', END) != '\n':
            tup = get_input()
            tkinter.messagebox.showinfo('提示','点击确定开始保存。\n由于生成摘要，您可能需要稍作等候。')
            clean_input()
            bookcard.add(tup[0],tup[1],tup[2],tup[3],tup[4],
                         collection.get(),tup[5],tup[6],tup[7],tup[8],
                         tup[9],tup[10])
            tkinter.messagebox.showinfo('提示','保存成功！')
        else:
            if text1.get('1.0', END) == '\n':
                tkinter.messagebox.showerror('警告','未输入内容！')

    # 部件
    label1 = Label(window, text='文本内容', font=('宋体', 16))
    label1.grid(column=0, row=0)
    text1 = ScrolledText(window, font=('宋体', 16), height=6,
                         width=60)
    text1.grid(column=1, row=0)

    label2 = Label(window, text='作者信息', font=('宋体', 16))
    label2.grid(column=0, row=1)
    text2 = ScrolledText(window, font=('宋体', 16), width=60,
                         height=2)
    text2.grid(column=1, row=1)

    label3 = Label(window, text='书名信息', font=('宋体', 16))
    label3.grid(column=0, row=2)
    text3 = ScrolledText(window, font=('宋体', 16), width=60,
                         height=2)
    text3.grid(column=1, row=2)

    label4 = Label(window, text='出版信息', font=('宋体', 16))
    label4.grid(column=0, row=3)
    text4 = ScrolledText(window, font=('宋体', 16), width=60,
                         height=2)
    text4.grid(column=1, row=3)

    label5 = Label(window, text='获取途径', font=('宋体', 16))
    label5.grid(column=0, row=4)
    text5 = ScrolledText(window, font=('宋体', 16), width=60,height=2)
    text5.grid(column=1, row=4)

    label6 = Label(window, text='标签1', font=('宋体', 16))
    label6.grid(column=0, row=5)
    text6 = Entry(window, font=('宋体', 16), width=59)
    text6.grid(column=1, row=5)

    label7 = Label(window, text='标签2', font=('宋体', 16))
    label7.grid(column=0, row=6)
    text7 = Entry(window, font=('宋体', 16), width=59)
    text7.grid(column=1, row=6)

    label8 = Label(window, text='标签3', font=('宋体', 16))
    label8.grid(column=0, row=7)
    text8 = Entry(window, font=('宋体', 16), width=59)
    text8.grid(column=1, row=7)

    label9 = Label(window, text='标签4', font=('宋体', 16))
    label9.grid(column=0, row=8)
    text9 = Entry(window, font=('宋体', 16), width=59)
    text9.grid(column=1, row=8)

    label10 = Label(window, text='标签5', font=('宋体', 16))
    label10.grid(column=0, row=9)
    text10 = Entry(window, font=('宋体', 16), width=59)
    text10.grid(column=1, row=9)

    label11 = Label(window,text='读书随感',font=('宋体', 16))
    label11.grid(column=0,row=10)
    text11 = ScrolledText(window,font=('宋体', 16), width=60,height=6)
    text11.grid(column=1,row=10)

    button1 = Button(window, height=2, width=8, text='保存记录',
                     font=('宋体', 16),command=save)
    button1.place(x=1000, y=50)
    button2 = Button(window, height=2, width=8, text='清除记录',
                     font=('宋体', 16),command=clean)
    button2.place(x=1000, y=150)
    button3 = Button(window, height=2, width=8, text='退出编辑',
                     font=('宋体', 16),command=close)
    button3.place(x=1000, y=250)

    radio1 = Radiobutton(window, text='收藏',
                         variable=collection,
                         value=1, font=('宋体', 16))
    radio1.place(x=1000, y=350)
    radio2 = Radiobutton(window, text='不收藏',
                         variable=collection,
                         value=0, font=('宋体', 16))
    radio2.place(x=1000, y=375)

    window.mainloop()


if __name__ == '__main__':
    open_window()
