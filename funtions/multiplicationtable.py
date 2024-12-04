#create a funtion multiplication_table(number,n) print multi table till n .

def multiplication_table(number,n=10):

    for i in range(1,n+1):

        print(f"{number}*{i}={number*i}")


multiplication_table(5)

# n nu normally namukku oru default value kodukkam that is n=10 ,athil thannae n nu verae value koduthalm work aakum
#but user value koduthillankilum default aay 10 verae work aakum 