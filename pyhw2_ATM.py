#!-*- coding: Big5 -*-
money=5000
inputmoney=raw_input('請輸入您要領取的金額:')
inputmoney=int(inputmoney)
result=""

if (money-inputmoney)<0:
    result="您的存款不足"
    print result
elif (money-inputmoney)==0:
    result="您的存款無剩餘"
    print result
else:
    result="您的存款還剩%d元" %(money-inputmoney)
    print result

f=open('ATM.txt','w')
f.write(result)
f.close()
