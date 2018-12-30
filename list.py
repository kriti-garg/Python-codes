shoplist = ['apple','banana','carrot','mango']
print('length is ',len(shoplist))
for item in shoplist:
    print('item ',item )
shoplist.append('rice')
print('appending',shoplist)
shoplist.sort()
print('sorting',shoplist)
print('first item is: ',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('deleted item is: ',olditem)
print('updated shoplist : ',shoplist)
