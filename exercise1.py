n = int(input())
if n < 2 :
  print('не соответствует условию')
else:
  list = list(map(int,input().split()))
  print(min(list),max(list))