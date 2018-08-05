from lib import queue



def hot_potato (name_list, num):
    q  = queue.Queue()
    for i in range (len(name_list)):
        q.enqueue(name_list[i])
    while(q.size() > 1):
        for i in range (num):
            q.enqueue(q.dequeue())
        q.dequeue()
    print(q.dequeue())


        
        # print(q.size())
        # for i in range (q.size()):
        #     q_correct.enqueue(a[i])
        #     print(q_correct.dequeue(), end = '')

    # print('===============')
    # print(q.dequeue())

hot_potato(["Susan","Brad","Kent","David"], 4)               # 回傳 "Brad"
hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7) # 回傳 "Susan"


# name_list = ['a', 'b', 'c', 'd']


# for j in range(3):
#     a = []
#     for i in range(len(name_list)):
#         if( i == len(name_list) - 1):
#             a.insert(0, name_list[len(name_list) - 1 ])
#         else:
#             a.append(name_list[i])
#     name_list = a
    # print(a)


# name_list.reverse()
# print(name_list)
# for j in range (3):
#     for i in range(len(name_list)):
#         a = []
#         if( i == len(name_list) - 1):
#             a.insert(0, name_list[len(name_list) - 1 ])
#         else:
#             a.append(name_list[i])
# print(a)

