# coding:utf-8
import bookcard
from tkinter import *
import tkinter.messagebox
from tkinter.scrolledtext import *
import search_card
import frontend


def open_window():
    # 启动
    tkinter.messagebox.showinfo('提示',
                                '本系统摘要自动生成系统正在完善中，结果仅供参考！')
    window = Toplevel()
    window.geometry('1200x600+0+0')
    window.title('读书卡片检索系统-检索结果')
    collection = IntVar()

    # 函数
    def listbox_output():
        for records in search_card.res:
            card_list.insert('end', records[1])

    def clean_input():
        text1.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0', END)
        text6.delete(0, END)
        text7.delete(0, END)
        text8.delete(0, END)
        text9.delete(0, END)
        text10.delete(0, END)
        text11.delete('1.0', END)

    def delete():
        del_index = card_list.index('active')
        del_item = search_card.res[del_index]
        search_card.res.remove(del_item)
        clean_input()
        bookcard.delete(del_item[0])
        card_list.delete('active')

    def text_output(event):
        choose = card_list.curselection()
        if choose:
            choose_index = choose[0]
            choose_item = search_card.res[choose_index]
            clean_input()
            text1.insert('end', choose_item[1])
            text2.insert('end', choose_item[2])
            text3.insert('end', choose_item[3])
            text4.insert('end', choose_item[4])
            text5.insert('end', choose_item[5])
            collection.set(choose_item[6])
            text6.insert('end', choose_item[7])
            text7.insert('end', choose_item[8])
            text8.insert('end', choose_item[9])
            text9.insert('end', choose_item[10])
            text10.insert('end', choose_item[11])
            text11.insert('end', choose_item[12])
            text12.insert('end', choose_item[13])

    def update_card():
        update_index = card_list.index('active')
        former_item = search_card.res[update_index]
        bookcard.update(former_item[0],
                        card_text=text1.get('1.0', END),
                        author=text2.get('1.0', END),
                        name=text3.get('1.0', END),
                        publish_info=text4.get('1.0', END),
                        ways_to_get=text5.get('1.0', END),
                        collect=collection.get(),
                        tag1=text6.get(),
                        tag2=text7.get(),
                        tag3=text8.get(),
                        tag4=text9.get(),
                        tag5=text10.get(),
                        thoughts=text12.get('1.0', END))
        new_item = (former_item[0], text1.get('1.0', END),
                    text2.get('1.0', END), text3.get('1.0', END),
                    text4.get('1.0', END), text5.get('1.0', END),
                    collection.get(), text6.get(), text7.get(),
                    text8.get(), text9.get(), text10.get(),
                    text11.get('1.0', END), text12.get('1.0', END))
        search_card.res.remove(former_item)
        search_card.res.insert(update_index,new_item)

    def exit_window():
        is_exit = tkinter.messagebox.askyesno('警告',
                                              '未保存的操作将消失！\n您确定要退出吗？')
        if is_exit > 0:
            window.destroy()


    # 部件
    label1 = Label(window, text='文本内容', font=('宋体', 16))
    label1.grid(column=0, row=0)
    text1 = ScrolledText(window, font=('宋体', 16), height=5,
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
    text5 = ScrolledText(window, font=('宋体', 16), width=60,
                         height=2)
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

    label11 = Label(window, text='文本摘要', font=('宋体', 16))
    label11.grid(column=0, row=10)
    text11 = ScrolledText(window, font=('宋体', 16), width=60, height=3)
    text11.grid(column=1, row=10)

    label12 = Label(window, text='读书随感', font=('宋体', 16))
    label12.grid(column=0, row=11)
    text12 = ScrolledText(window, font=('宋体', 16), width=60, height=3)
    text12.grid(column=1, row=11)

    frame = LabelFrame(window, height=380, width=350, font=('宋体', 16),
                       relief=RIDGE, pady=10, text='搜索结果')
    frame.place(x=800, y=0)
    scrollbar1 = Scrollbar(frame)
    scrollbar1.pack(side='right', fill='y')
    card_list = Listbox(frame, font=('宋体', 16), height=15, width=30,
                        yscrollcommand=scrollbar1)
    card_list.pack()
    scrollbar1.config(command=card_list.yview)
    card_list.bind('<<ListboxSelect>>', text_output)

    button1 = Button(window, height=2, width=8, text='删除',
                     font=('宋体', 16), command=delete)
    button1.place(x=800, y=400)

    button2 = Button(window, height=2, width=8, text='更新',
                     font=('宋体', 16), command=update_card)
    button2.place(x=920, y=400)

    button3 = Button(window, height=2, width=8, text='退出',
                     font=('宋体', 16),command=exit_window)
    button3.place(x=1040, y=400)

    radio1 = Radiobutton(window, text='收藏',
                         variable=collection,
                         value=1, font=('宋体', 16))
    radio1.place(x=800, y=500)
    radio2 = Radiobutton(window, text='不收藏',
                         variable=collection,
                         value=0, font=('宋体', 16))
    radio2.place(x=900, y=500)

    # 持续
    listbox_output()
    window.mainloop()


if __name__ == '__main__':
    open_window()
