# -*- coding: cp936 -*-
# x��ָ�� x ����
# y��ָ�� y ����
# anchor��ָ������λ��
from tkinter import *
root = Tk()
lb = Label(root,text = 'hello Place')
# lb.place(relx = 1,rely = 0.5,anchor = CENTER)
# ʹ�þ������꽫 Label ���õ�(0,0)λ����
lb.place(x = 0,y = 0,anchor = NW)
#lb.pack()
root.mainloop()
# x,y ָ��������õľ���λ��