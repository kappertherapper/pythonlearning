def answer0(string)
    return string

-------------------------------------------------- 

def answer1(number)
    return number * 2

-------------------------------------------------- 

def answer2(string)
    return string.upper()

-------------------------------------------------- 

def answer3(string):
    return string[::-1]

-------------------------------------------------- 

def answer4(list):
    return sorted(list)

-------------------------------------------------- 

def answer5(list):
    return (list[:3])

-------------------------------------------------- 

def answer6(list):
    result = []
    for i in list:
        result.append(i * 5)
    return result

-------------------------------------------------- 

def answer7(list):
    return list[5]    

-------------------------------------------------- 

def answer8(list):
    return sorted(set(list))

-------------------------------------------------- 

def answer9(string):
    return string.replace('be', 'python')

-------------------------------------------------- 

def answer10(string):
    lastWord = string.split()[-1]
    backwards = lastWord[::-1]
    return string[:-len(lastWord)] + backwards    

-------------------------------------------------- 

def answer11(number):
    list = [number]
    for i in range(19):
        number += 5
        list.append(number)
    return list

-------------------------------------------------- 

def answer12(list):
    for key, value in list:   
        if key == '192.168.1.212':
        return value

-------------------------------------------------- 

def answer13(list):
    total = 0

    for i in list:
        total += i

    return total      

--------------------------------------------------

def answer14(string):
    pairs = string.split(',')
    liste = []

    for pair in pairs:
        key, value = pair.split(':')
        liste.append((key, value))

    return liste

--------------------------------------------------

def answer15(dic):
    dic.pop('192.168.1.243')
    return dic    

--------------------------------------------------

def answer16(string):
    lst = string.split()
    reverse = ""

    for word in lst:
        reverse += word[::-1] + " "

    reverse = reverse.rstrip()

    return reverse

--------------------------------------------------

def answer17(tupl):
    lst = []
    for i in range(10):
        lst.append(tupl)
    return lst

--------------------------------------------------

def answer18(dic):
    dic["yellow"] = 22
    return dic

--------------------------------------------------

def answer19(string):
    lst = string.strip().split()
    ips = set(lst[::10])

    return ips

--------------------------------------------------
def answer20(data):
    lst = data.strip().split()
    codes = lst[8::10]

    ok = lst.count('200')
    notModified = lst.count('304')
    uauthorized = lst.count('401')

    dic = {'200': ok, '304': notModified, '401': uauthorized}

    return dic

--------------------------------------------------

def answer21(data):
    lst = data.strip().split()
    codes, sizes = lst[8::10], lst[9::10]
  
    tup = tuple(zip(codes, sizes))
    total = 0
    count = 0

    for code, size in tup:
        if code == '200' and size != '-':
            total += int(size)
            count += 1

    return total // count

--------------------------------------------------

def answer22(data):
    return data.count('.png')

--------------------------------------------------

def answer23(lst):
    d = {}
    for key, value in lst:
        d[key] = value
    return d

--------------------------------------------------

def answer24(num):
    lst = list(range(1,101))

    i = 0
    while i < len(lst):
        if lst[i] % num == 0:
            lst.pop(i)
        else:
            i += 1
     return lst

--------------------------------------------------

def answer27():
    return 'network'

--------------------------------------------------

def answer28(list):
    return list.split(', ')[3]

--------------------------------------------------

def answer29():
    return 39

--------------------------------------------------

def answer30():
    return 3775708311

--------------------------------------------------

def answer31(data):
    return '0.client-channel.google.com'    


--------------------------------------------------

def answer32(data):
    plusfloor = '^'
    minusfloor = 'v'
    plusroom = '>'
    minusroom = '<'
    
    floorCount = 0
    roomCount = 0
    
    for i in data:
        if i == plusfloor:
            floorCount += 1
        elif i == plusroom:
            roomCount += 1
        elif i == minusfloor:
            floorCount -= 1
        else:
            roomCount -= 1    
    
    return (floorCount, roomCount)


--------------------------------------------------
