n=int(input("enter number of records"))
l=[]
for i in range(0,n):
    id=int(input("enter id  "))
    name=str(input("enter your name  "))
    mobile=int(input("enter 10-digit mobile number  "))
    address=str(input("enter your address  "))
    d={'id':id,'name':name,'mobile':mobile,'address':address}
    l.append(d)
for j in l:
    print(j)
    
