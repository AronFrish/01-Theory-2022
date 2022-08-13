#importing data from data.txt
f = open("data.txt", "r")
g = f.read()
if (len(g)==0) :
    zeroes = 0
    ones = 0
    n = 0
else :
    zeroes = int(g[len("zeroes:"):g.index(",")])
    g = g[g.index(",") + 1:]
    ones = int(g[len("ones:")+1:g.index(",")])
    g = g[g.index(",") + 1:]
    n = int(g[len("number:")+1:])
f.close()
#importing data from data.txt

#save data to data.txt
def save() :
    f = open("data.txt", "w")
    f.write("zeroes:" + str(zeroes) + ", ones:" + str(ones) + ", number:" + str(n))
    f.close()

def save_data_point() :
    f = open("data_dump.txt", "a")
    f.write(str(n) + " : " + str(zeroes) + ", " + str(ones) + "\n")
    f.close()
#save data to data.txt

#running calculations
while (1) :
    z = str(n)
    zeroes+=2*z.count('0')
    ones+=2*z.count('1')
    print(n, ones/zeroes)
    n+=1
    if (n%10000==0) :
        save_data_point()
        save()
#running calculations