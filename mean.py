import csv

#opening the file and reading it 
with open("HeightWeight.csv",newline ='') as f :
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

#HeightWeight data is stored in @new_data
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#finding out the length of the new data
n = len(new_data)

#starting from the value "0"
total = 0

#total+x = 0+x
#x is basically the value we get when we add the values
for x in new_data:
    total+= x

mean = total/n
print("mean: "+str(mean))

