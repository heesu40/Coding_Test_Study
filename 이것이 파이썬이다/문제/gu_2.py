#왕실의 나이트
step = (
    [2,1],
    [-2,1],
    [2,-1],
    [-2,-1],
    [-1,2],
    [1,2],
    [1,-2],
    [-1,-2],
)


basestr = input()
base1 = basestr[0]
base2 = int(basestr[1])

if base1 == 'a':
    base1 = 1
elif base1 == 'b':
    base1 = 2
elif base1 == 'c':
    base1 = 3
elif base1 == 'd':
    base1 = 4
elif base1 == 'e':
    base1 = 5
elif base1 == 'f':
    base1 = 6
elif base1 == 'g':
    base1 = 7                
elif base1 == 'h':
    base1 = 8

base = [base1, base2]
result = []
for slist in step:
    print(slist[0] , base[0] , type(slist[0]), type(base[0]))
    dx = slist[0] + base[0]
    dy = slist[1] + base[1]
    if dx > 0  and dy > 0 and dx < 9 and dy < 9:
        result.append([dx, dy])
print(len(result))
