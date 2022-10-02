# ფუნქციები ორობითი, რვაობითი და თექვსმეტობითი სისტემებისთვის ათობითში გადასაყვანად

def to_dec(num, base=2):
    if base==2:
        if num!=int(num):
            num = int(num)
        base = base**0
        dec_num = 0
        while num:
            nash = num % 10
            num //= 10
            dec_num += nash*base
            base = base*2
        return dec_num

    if base==8:
        if num!=int(num):
            num = int(num)
        base = base**0
        dec_num = 0
        while num:
            nash = num % 10
            num //= 10
            dec_num += nash*base
            base = base*8
        return dec_num
    if base==16:
        dict_hex = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8, '9':9,
                'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        base = base ** 0
        dec_num = 0
        num_list = list(num)
        for i in num_list[::-1]:
            dec_num += dict_hex[i]*base
            base = base*16
        return dec_num

# ფუნქციები ათობითიდან, ორობითში რვაობითში და თექვსმეტობით სისტემებში გადასაყვანად

def dec_to_base(num, to_base=2):
    list = []

    if to_base==2 or to_base==8:
        while num:
            nash = num % to_base
            num //= to_base
            list.append(str(nash))

    if to_base==16:
        dict_hex = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
                    10: 'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        num = int(num)
        while num:
            nash = num % to_base
            num //= to_base
            list.append(dict_hex[nash])

    return ''.join(list[::-1])


def to_bin(num, base=10):
    if base==10:
        return dec_to_base(num)
    num = to_dec(num, base)
    return dec_to_base(num)


def to_oct(num, base=10):
    if base==10:
        return dec_to_base(num, 8)

    num = to_dec(num, base)
    return dec_to_base(num, 8)


def to_hex(num, base=10):
    if base==10:
        return dec_to_base(num, 16)

    num = to_dec(num, base)
    return dec_to_base(num, 16)

# პროგრამის რესტარტი

def againFunction():
    print("\n 1. Yes \n 2. No \n")
    again = int(input("Want to try again ? : "))
    if again == 1:
        input_system()
    elif again == 2:
        print("Done of Program")
    elif again != 1 or 2:
        print("\nChoose number from 1 to 2")
        againFunction()

# პროგრამის სტარტი, სისტემის არჩევა

def input_system () :
    print("\n 1. Binary \n 2. Octa Decimal \n 3. Decimal \n 4. Hexa Decimal \n")
    inputSystem = int(input("Choose system for number : "))
    if inputSystem not in [1, 2, 3, 4]:
        print("\n Choose number from 1 to 4")
        return input_system()
    else:
        dict_bases = {1:"2", 2:"8", 3:"10", 4:"16"}
        change_system(dict_bases[inputSystem])
        return inputSystem

# რიცხვის სისტემის ცვლილება, შეყვანილი მონაცემების შესაბამისად

def change_system (inputBase) :
    inputBase = int(inputBase)
    print("\n 1. Binary \n 2. Octa Decimal \n 3. Decimal \n 4. Hexa Decimal \n")
    changeSystem = int(input("Choose system for Change number system : "))
    if changeSystem not in [1, 2, 3, 4]:
        print("\n Choose number from 1 to 4")
        return change_system()
    else:
        number = input("\nChoose number : ")
        if (inputBase != 16) and (changeSystem != 4):
            number = int(number)
        if changeSystem == 1:
            #To Binary
            if inputBase == 1:
                print(number)
            else:
                print("\nThe answer is : ", to_bin(number, inputBase))
                againFunction()

        elif changeSystem == 2:
            #To Octa
            if inputBase == 2:
                print(number)
            else:
                print("\nThe answer is : ", to_oct(number, inputBase))
                againFunction()

        elif changeSystem == 3:
            #To Decimal
            if inputBase == 3:
                print(number)
            else:
                print("\nThe answer is : ", to_dec(number, inputBase))
                againFunction()

        else:
            #To Hexa
            number = str(number)
            if inputBase == 4:
                print(number)
            else:
                print("\nThe answer is : ", to_hex(number, inputBase))
                againFunction()

    return 0

input_system()