## 시각
n = int(input())

count = 0

if n == 0:
    for hh in range(24):
        if hh < 10:
            hh = str(0) + str(hh)
        for mm in range(60):
            if mm < 10:
                mm = str(0) + str(mm)
            for ss in range(60):
                if ss < 10:
                    ss = str(0) + str(ss)
                if '0' in str(hh) + str(mm) + str(ss):
                    count+=1
else :
    for hh in range(n+1):
        for mm in range(60):
            for ss in range(60):
                if str(n) in str(hh) + str(mm) + str(ss):
                    count+=1
print(count)                    
