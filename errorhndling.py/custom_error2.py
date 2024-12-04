def poll(age):

    assert age>18,"invalid age"

    print("voted")

try:

    poll(19)  

except Exception as e:

    print(e)

#assert raise nu pakaram use cheyyam 

def review(rating):

    assert rating>0,"too low"

    assert rating in range (0,11),"too high"

    print("rated")

try:

    review(5)

except Exception as e:

    print(e)

