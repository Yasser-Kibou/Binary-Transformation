
binary = str(input('Give a binary value: '))

#the condition of testing if the data is 1 or 0
condition =  True 

value     =  0       
power     =  0       
index     = -1      

#testing if the data is 1 or 0
for x in binary:
    if x == '1' or x == '0' :
        pass
    else:
        condition = False
        print("you must insert a binary value Bunghole.")
        break

#transofrming bits into decimal number
if condition:
    binary = [int(x) for x in binary]
    
    for y in binary:
        value += binary[index] * pow(2, power)
        index -= 1
        power += 1

    print(value)