lst1=[(),('paras',5),('ankit',11),(),('adithiyan',115),(),('adithi',3),()]
lst2=[]
for item in lst1:
    if len(item)!=0:
        lst2.append(item)
print(lst2)
output:
[('paras',5),('ankit',11),('adithiyan',115),('adithi',3)]
