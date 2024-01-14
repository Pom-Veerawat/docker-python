from random import randint

print('โปรแกรมที่ทำให้รวยทุก 15 วัน...')
min_number = int(input('ใส่เลขค่าต่ำสุดที่ต้องการ: '))
max_number = int(input('ใส่เลขค่ามากสุดที่ต้องการ: '))

if (max_number < min_number): 
  print('กรุณากรอกค่าที่ถูกต้อง...')
else:
  rnd_number = randint(min_number, max_number)
  print('เลขที่ออก...!!!')
  print(rnd_number)

