dict={}
keys=dict.keys()
x="googl.com'"
z=len(x)
for i in range(z):
    #keys=dict.keys()
    y=x[-i]
    if y in keys:
        dict[y]+=1
    else:
        dict[y]=1
print(dict)
        
