#!-*- coding: Big5 -*-
money=5000
inputmoney=raw_input('�п�J�z�n��������B:')
inputmoney=int(inputmoney)
result=""

if (money-inputmoney)<0:
    result="�z���s�ڤ���"
    print result
elif (money-inputmoney)==0:
    result="�z���s�ڵL�Ѿl"
    print result
else:
    result="�z���s���ٳ�%d��" %(money-inputmoney)
    print result

f=open('ATM.txt','w')
f.write(result)
f.close()
