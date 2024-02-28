n = 11
for i in range(n, 0, -1):
  spaces = (n-i) * 2 * ' '
  signs = i * '$ '
  print(spaces + signs)
