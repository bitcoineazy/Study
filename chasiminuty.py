X = int(input('Икс'))
H = int(input('Икс'))
M = int(input('Икс'))

print(X // 60 +H+(X % 60 +M)//60)
print((X % 60 + M)%60)