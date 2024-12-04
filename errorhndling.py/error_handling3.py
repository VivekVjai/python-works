arr=[1,2,3,4,5,6]

index=int(input("enter the index"))

try:

    result=arr[index]

    print(result)

except Exception as e: #exception kodukkunathu nthu error aanu occur cheyyunnathu ennu print akum

    print(e)

finally:

    print("file write ")

    print("database commit ")            