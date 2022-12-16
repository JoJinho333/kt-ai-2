# 3250 콘서트 해결
date = int(input())
daily = input()

def seq_search_for(day, daily, date):
    for i in range(len(day)):
        if day[i] == daily:
            return day[i + date]
    return -1

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']*1500

index = seq_search_for(day, daily, date)
print(index)