from random import randint

min_number = int(input('ใส่เลขค่าต่ำสุด: '))
max_number = int(input('ใส่เลขค่ามากสุด: '))

if (max_number < min_number): 
  print('กรุณากรอกค่าที่ถูกต้อง...')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

