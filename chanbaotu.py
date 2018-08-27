s1 = 'oxoxoxox'
s2 = 'ooxxoo'
for i in s1:
    if s2 and i==s2[0]:
        s2=s2[1:]
print("No" if s2 else "Yes")