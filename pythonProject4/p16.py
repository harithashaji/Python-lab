y = {'manya': 40, 'nayana': 2, 'navya': 1, 'anaya': 3}
l = list(y.items())
l.sort()
print('Ascending order is', l)
l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)
