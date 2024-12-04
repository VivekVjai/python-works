def is_leapyear(year):

    if year<0:

        return False

    if year%100!=0 and year%4==0 or year%100==0 and year%400==0:

        return True
    
    else:

        return False
    
def test_is_leapyear():

    assert is_leapyear(2024)==True,"non century year check failed "

    assert is_leapyear(2025)==False,"invalid non century check failed "

    assert is_leapyear(2000)==True,"century leap year check failed "

    assert is_leapyear(1900)==False,"invalid century year check failed "

    assert is_leapyear(-2024)==False,"invalid year check failed "

try:
    test_is_leapyear()
    print("test case passed")

except Exception as e:

    print("test case failed",e)