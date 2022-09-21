s = sorted(input())
word1 = dict(zip(range(len(s)), s))

s = sorted(input())
word2 = dict(zip(range(len(s)), s))

print('YES' if word1 == word2 else 'NO')