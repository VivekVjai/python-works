


def review(rating):

    if rating<0:

        raise Exception("too low")
                   
    elif rating>10:

        raise Exception("too high")
    
    else:

        print("done")

try:

    review(8)

except Exception as e:

    print(e)

print("hai")

print("hello")

def poll(age):

    assert age>18,"invalid age"

    print("voted")

poll(14)  


#

def num_check(number):

    if number>0:

        return ("+ve num")
    
    elif number<0:

        return ("-ve num")
    
    elif number==0:

        return ("zero")
    
def num_check():

    assert num_check(10)=="+ve num",""

