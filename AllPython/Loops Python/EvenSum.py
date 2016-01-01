#P4.1
#Add all even numbers between start and end
start = int(input("enter starting value"))
end = int(input("enter ending value"))
total = 0.0
for start in range(start,end,2):
    total = total + start
    print(total)

