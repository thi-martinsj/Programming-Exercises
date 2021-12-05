seconds = int(input())

h, m, s = 0, 0, seconds

if seconds >= 60:
    m = int(seconds / 60)
    s = seconds % 60

    if m >= 60:
        h = int(m / 60)
        m = m % 60

print("%d:%d:%d" %(h,m,s))