lst=[]
i=0
num_companies=int(input('enter no.of companies:'))
for i in range(num_companies):
    name=input('enter name:')
    no_of_shares=int(input('enter no.of shares:'))
    dt_of_pur=input('enter date of purchase:')
    cost_price=int(input('enter cost price:'))
    selling_price=int(input('enter selling price:'))
    tpl=(name,no_of_shares,dt_of_pur,cost_price,selling_price)
    lst.append(tpl)
tot=0
gaintot=0
losstot=0
for j in lst:
    no_of_shares=j[1]
    cost_price=j[3]
    selling_price=j[4]
    cop=int(no_of_shares*cost_price)
    tot=tot+cop
if selling_price>cost_price:
    gaintot+=(selling_price-cost_price)*no_of_shares
else:
    losstot+=(cost_price-selling_price)*no_of_shares
print(f'total cost portfolio:{tot:.2f}')
if gaintot>losstot:
    net=gaintot-losstot
    gain_per=net/tot*100
    print(f'net amount gained:{net:2f}')
    print(f'percentage profit:{gain_per:.2f}')
else:
    net=losstot-gaintot
    loss_per=net/tot*100
    print(f'net amount lost:{net:.2f}')
    print(f'percentage loss:{loss_per:.2f}')
output:
enter no.of companies:3
enter name:kabilesh
enter no.of shares:100
enter date of purchase:1/04/2024
enter cost price:145
enter selling price:186
enter name:infosys
enter no.of shares:90
enter date of purchase:2/04/2024
enter cost price:775
enter selling price:800
enter name:tata motor
enter no.of shares:120
enter date of purchase:3/04/2024
enter cost price:785
enter selling price:678
total cost of portfolio:178450.00
net amount lost:6490.00
percentage:3.64
