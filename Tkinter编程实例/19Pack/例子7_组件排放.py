# -*- coding: cp936 -*-
# side���ı�����ķ���λ��
from tkinter import *
root = Tk()
# �ı� root �Ĵ�СΪ 80x80
root.geometry('80x80+0+0')
print(root.pack_slaves())
# �������� Label �ֱ�ʹ�ò�ͬ�� fill ����,��Ϊˮƽ����
# ����һ�� Label �������
Label(root,
text = 'pack1',
bg = 'red').pack(fill = Y,expand = 1,side = LEFT)
# ���ڶ��� Label ���ҷ���
Label(root,
text = 'pack2',
bg = 'blue').pack(fill = BOTH,expand = 1,side = RIGHT)
# �������� Label ������ã��� Label ���ã�ע��������ŵ� Label1 �����
Label(root,
text = 'pack3',
bg = 'green').pack(fill = X,expand = 0,side = LEFT)
print(root.pack_slaves())
root.mainloop()