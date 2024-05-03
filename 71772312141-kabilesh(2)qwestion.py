import operator
lst=[('key',101.25),('lock',320.85),('hammer',100.55),('spanner',67.77),('tong',93.05)]
print(sorted(lst,reverse=True,key=operator.itemgetter(1)))
output:
[('lock',320.85),('key',101.25),('hammer',100.55),('tong',93.05),('spanner',67.77)]
