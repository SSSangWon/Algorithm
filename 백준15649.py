import itertools

n, m = map(int, input().split())
lst=[str(i+1) for i in range(n)]

print('\n'.join(list(map(' '.join,itertools.permutations(lst,m)))))
