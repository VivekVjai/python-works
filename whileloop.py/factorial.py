#factorial calculation

n=int(input("enter the no: "))

f=1

while(n>=1):  #n = 1 aakunna vera loop work cheyyum , n zero aayal eq anusarich whole value zero aakum

    f=f*n   #f=1 n=5(eg) ,f=1*5=5(1st loop), f=5*4(2nd loop), and so one n=1 akunna vera loop will continues

    n=n-1   #as per equation n!=n*(n-1)*(n-2)*....*1

print(f"factorial is {f}")