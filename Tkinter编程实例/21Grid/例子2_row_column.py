# -*- coding: cp936 -*-
#row��ָ����
# column��ָ����
from tkinter import *
root = Tk()
# �������� Label
lb1 = Label(root,text = 'Hello',bg='red')
lb2 = Label(root,text = 'Grid',bg='yellow')
lb1.grid(row=0,column=0)
# ָ�� lb2 Ϊ��һ�У�ʹ������ 0 ��ʼ�����ڶ��У�ʹ������ 0 ��ʼ��
lb2.grid(row = 0,column = 1)
root.mainloop()