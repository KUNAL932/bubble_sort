Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information
=============================== RESTART: Shell ===============================
>>> def bubblesort(list):
	for item_num in range(len(list)-1,0,-1):
		for idx in range(item_num):
			if list[idx]>list[idx+1]:
				temp=list[idx]
				list[idx]=list[idx+1]
				list[idx+1]=temp

				
>>> list=[9,38,88,66,43,1,7,5,3,65]
>>> bubblesort(list)
>>> print(list)
[1, 3, 5, 7, 9, 38, 43, 65, 66, 88]
>>> 
