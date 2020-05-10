n=int(input('NHAP MOT SO'))
boolean=False
for i in range(2,n):
    if n%i==0 and n!=i:
        boolean=True;

if(boolean==True):
    print("khong phai so nguyen to")

else:
    print("LA SO NGUYEN TO")        