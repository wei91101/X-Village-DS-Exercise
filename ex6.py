import json

f = open('ptt_0726_s.json', 'r', encoding = 'utf-8')
x = json.load(f)
#print(x)
x1 = x
#print(j[0]['h_推文總數']['推'])
k = []
for i in range (0,len(x)):
    if(x[i]['h_推文總數'] != {}):
        #print(j[i]['h_推文總數']['推'])
        
        s = sorted(x, key = lambda k : k['h_推文總數'].get('推', 0), reverse = True)
        # k.append(x[i]['h_推文總數']['推'])
        # print(s)
s = json.dumps(s, indent = 4, ensure_ascii = False)
print(s)
f = open('test.json', 'w' , encoding = 'utf-8')
f.write(s)

# print(k)
# print(sorted(k))
# print(x)


# for i in range (1, len(x)):
#     if(x[i]['h_推文總數'] != {} and x1[i]['h_推文總數'] != {}):
#         temp = x[i]['h_推文總數']['推']
#         temp1 = x1[i]
#         #print(x[i]['h_推文總數']['推'])
#         j = i-1
#         while j >= 0 and x[j]['h_推文總數'] != {} and x1[j]['h_推文總數'] != {} and temp < x[j]['h_推文總數']['推'] :
#             #print(x[j]['h_推文總數']['推'])
#             x[j+1]['h_推文總數']['推'] = x[j]['h_推文總數']['推']
#             x1[j+1] = x1[j]
#             j += -1
#         x[j+1]['h_推文總數']['推'] = temp
#         x1[j+1] = temp1
#print(x)
# print(type(x))
# print(x)




# for i in range(1,len(k)):
#     temp = k[i]
#     j = i-1
#     while j >= 0 and temp < k[j]:
#         k[j+1] = k[j]
#         j += -1
#     k[j+1] = temp
# print(k)



