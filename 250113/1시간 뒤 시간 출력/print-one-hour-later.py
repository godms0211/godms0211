a = input()
time = a.split(":")

h = int(time[0])
m = int(time[1])

print("%d:%d" %(h+1, m))