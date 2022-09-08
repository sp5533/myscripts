#!/usr/bin/python3

numberstotest =int (input('Hur många tal vill du undersöka?:'))

for i in range (2,numberstotest+1):
   provennotprime = False   
   for k in  range(2,i):
      if  i%k == 0: 
         print(f'{i}')
         provennotprime = True
         break
   if provennotprime == False:
       print(f'***{i} is prime! ***')

