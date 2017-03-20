def problem1_1():
    daumstock = 89000
    naverstock = 751000

    someonedaumcount = 0
    someonenavercount = 0

    someonedaumcount = input("input daumstock count : ")
    someonenavercount = input("input naverstock count : ")

    daumvalue = daumstock * someonedaumcount
    navervalue = naverstock * someonenavercount
    print("Total stock Value : %d", daumvalue + navervalue)
    return daumvalue+navervalue

def problem1_2(value):
    arr = []
    tmpvalue = value

    while (tmpvalue):
        if (tmpvalue >= 1000):
            arr.append(tmpvalue % 1000)
            tmpvalue = (int)(tmpvalue / 1000)
        else:
            arr.append(tmpvalue)
            break
    cnt = 0
    resultstr = ""
    while (arr):
        val = arr.pop()
        if (cnt == 0 and val == 0):
            print("0")
            break
        elif (cnt == 0 and val > 0):
            resultstr = str(val)
        elif (cnt != 0 and val > 0):
            resultstr = resultstr + "," + str(val)
        elif (cnt != 0 and val == 0):
            resultstr += ",000"
        cnt+=1

    print(resultstr)

val = problem1_1()
problem1_2(val)
	