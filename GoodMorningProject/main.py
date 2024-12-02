import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

a = int(time.strftime('%H'))

if 4<a<12 : 
  print("GoodMorning Sir")
elif 12<=a<18 :
  print("GoodAfternoon Sir")
elif 18<=a<21 : 
  print("GoodEvening Sir")
else: 
  print("GoodNight Sir Have a good sleep")


