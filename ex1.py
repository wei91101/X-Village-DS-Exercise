from lib import Stack

s = Stack.Stack()
count = 0
def dec_to_bin(dec):
    count = 0
    while ( dec > 0):
        rem = dec % 2
        # print(rem)
        s.push(rem)
        dec = dec // 2
        count += 1
    while (count > 0):
        print(s.pop(), sep = '', end = '')
        count -= 1
dec_to_bin(100)


        