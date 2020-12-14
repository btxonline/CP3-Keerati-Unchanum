number = int(input('please input number tree level:'))

for i in range(number):
  blank = (number - i)
  print((' '* blank) + ('*' * (((i+1)*2) - 1)))
