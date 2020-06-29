def my_freq():
    test_str=input("Enter the string\n")
    res={}
    for keys in test_str:
        res[keys]=res.get(keys,0)+1
    sort_orders=sorted(res.items(),key=lambda x:x[1],reverse=True)
    for i in sort_orders:
        print(i[0],i[1])
my_freq()

output:
Enter the string
mississippi
i 4
s 4
p 2
m 1
