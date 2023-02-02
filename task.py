#the condition of testing if the data is 1 or 0
condition =  True 

binary = str(input('Give a binary value: '))

value     =  0       
hexValue  = ''
power     =  0       
index     = -1      
hexArray  = ['A', 'B', 'C', 'D', 'E', 'F']

#testing if the data is 1 or 0
for x in binary:
    if x in ['1', '0'] :
        pass
    else:
        condition = False
        print("you must insert a binary value Bunghole.")
        break



#transofrming bits into decimal number
if condition:
    binary = [int(x) for x in binary]
    TransformationType = input('Do you want to transform it into decimal or Hex ? (d/h): ')    
    
    def calcValue():
        global value, index, power

        value += binary[index] * pow(2, power)
        index -= 1
        power += 1

    #This section is executed if the Person wants to Transform to Decimal
    if TransformationType in ['d', 'D']:
        for x in binary:
            calcValue()
        
        print(value)
    
    #This section is executed if the Person wants to Transform to Hex
    if TransformationType in ['h', 'H']:
        for x in range(1, 5):
            if len(binary) % 4 != 0:
                binary.insert(0, 0)
            else: 
                break

        for x in binary:
            calcValue()
            
            if power == 4:
                power = 0
                test = value - 10
                
                if test > -1:
                    value = hexArray[test]
                    hexValue = value + hexValue
                    value = 0
                else:
                    hexValue = str(value) + hexValue
                    value = 0
        print(hexValue)

