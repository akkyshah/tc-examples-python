str = input('Enter a string: ')

result = True   # assume that the str is PALINDROME

n = len(str)
for i in range(0, n):
  j = n - 1 - i           # 'j' moves backward (start = n-1 | end = 0)
  if str[i] != str[j]:    # 'i' moves forward
    result = False
    break

if result:
  print(f'\n{str} - IS a palindrome\n')
else:
  print(f'\n{str} - IS NOT a palindrome\n')