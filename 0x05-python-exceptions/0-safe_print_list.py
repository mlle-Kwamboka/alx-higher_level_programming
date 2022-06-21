#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   num = 0
   for i in range(0,x):
       try:
           num += len(my_list[i])
           print(num)
       except:
           pass
       print()
       return num
