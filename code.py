#sub functions
def Convert(lst):
    res_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return res_dct

def calculation(array,n,k,l): 
    distrubute.clear()
    result = +2147483647
   
    # Sorting the array. 
    array.sort() 
   
    # Find minimum difference 
    # all K size subarray. 
    for i in range(n-k+1): 
        result = int(min(result, array[i+k-1] - array[i])) 
    for j in range(0,l):
        for name,value in goodies.items():
            if(int(value)==array[k+j]):
                val = Convert([name,value])
                distrubute.update(val)  
    return result


#main functions
input_file = open("input.txt",'r')
global goodies, disturbute 
goodies = {}
distrubute = {}

for line in input_file:
    lines = line.split(":")
    val = Convert(lines)
    goodies.update(val)

val = (goodies.values())
actual = []
for n in val:
    actual.append(int(n))

arr= actual 
n =len(arr) 
input_file.close()
while(True):
    f = open("output.txt", "a")
    k = int(input("Number of employees : ")) 
    f.write("Number of employees : "+str(k))
    print("\n")
    f.write("\n")
    print("Here the goodies that are selected for distribution are:")
    f.write("Here the goodies that are selected for distribution are:")
    f.write("\n")
    result = calculation(arr, n, k,k)
    for name,value in distrubute.items():
        print(name+" : "+value,end="")
        f.write(name+" : "+value)
    print("\n")
    f.write("\n")
    print("And the difference between the chosen goodie with highest price and the lowest price is ",result)
    f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    f.write("\n")
    f.close()
