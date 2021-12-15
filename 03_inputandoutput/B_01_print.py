print('funny','python')
print('python','java','c',sep='-')
print()
print('Mr_Choo_C_AI')
print('point',end=':')
print('5 points')

fos=open('B_02_print.py',mode='wt')
print('print("hellow world")',file=fos)
fos.close()

import time 

for i in range(10): 
	print(i,end=' ' ,flush=False) 
	time.sleep(1)

for i in range(10): 
	print(i,end=' ' ,flush=True) 
	time.sleep(1) 

