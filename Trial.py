import csv

dic={}
the_file = open('1.csv', 'r')
reader = csv.reader(the_file)
i = 1
for row in reader:
    dic[i]=row[1]
    i+=1
print('The DMA table is:')

for i in range(1,85):
    print i,dic[i]

count=0
N = input('What DMA do you need?  ')
t=N
tool=str(dic[t])+'.csv'
f = open(tool,'w')
f.write('Month'+','+'Consumption'+'\n')
N=N-1
for j in range(1,16):
    trial=str(j)+'.csv'
    the_file = open(trial, 'r')

    reader = csv.reader(the_file)
    i = 0
    for row in reader:

        if i == N:
            print("This is the line.")
            print(row)
            f.write(str(j)+','+row[0])
            f.write('\n')
            count+=1
            break


        i += 1
the_file.close()
f.close()
