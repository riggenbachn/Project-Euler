suncount=0
dayofweek=0
months=[31,28,31,30,31,30,31,31,30,31,30,31]
year=1900
dayofmonth=1
month=1
while year<=2000:
    if dayofweek==6 and dayofmonth==1 and year>1900:
        suncount+=1
    dayofweek+=1
    if dayofweek==7:
        dayofweek=0
    dayofmonth+=1
    if month==2:
        if year%4==0 and year!=1900:
            months[month-1]=29
        else:
            months[month-1]=28
    if dayofmonth>months[month-1]:
        if month==12:
            month=1
            year+=1
        else:
            month+=1
        dayofmonth=1
print(suncount)	