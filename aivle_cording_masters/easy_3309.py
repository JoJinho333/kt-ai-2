# 3309 느려지는 시계 해결

import datetime as dt
n = int(input())
time_1 = dt.datetime.strptime('12:00:00',"%H:%M:%S")

if n == 0:
    time_2 = dt.datetime.strptime('00:00:00',"%H:%M:%S")
    time = time_1 - time_2
    print(time)
    
elif n >= 60:
    m = int(n/60)
    re = int(n%60)
    if m >= 60:
        h = int(m/60)
        su = int(m%60)
        time = ('%s:%s:%s' %(h,su,re))
        time_2 = dt.datetime.strptime(time,"%H:%M:%S")
        time = time_1 - time_2
        print(time)
    else:
        a=0
        time = ('%s:%s:%s' %(a,m,re))
        time_2 = dt.datetime.strptime(time,"%H:%M:%S")
        time = time_1 - time_2
        print(time)
elif n == 43200:
    print('00:00:00')
    
else:
    a=0
    b=0
    time = ('%s:%s:%s' %(a,b,n))
    time_2 = dt.datetime.strptime(time,"%H:%M:%S")
    time = time_1 - time_2
    print(time)