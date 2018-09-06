
s = input()
n = input()

count = 0
for i in range(len(s)):
  if s[i].isalnum():
    if int(n[i]) ==1:
      count+=1
  else:
    if int(n[i]) ==0:
      count+=1


rate = float(count)/len(s)
print('%.2f%%' % (rate * 100))