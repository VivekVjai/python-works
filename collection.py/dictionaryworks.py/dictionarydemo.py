#create a dictionary product with keys id, title,pricr,brand 

product={"id":123,"title":"shirt","price":1200,"brand":"dnmx"}

print(product["price"])

#update product price 

product["price"]=1350

print(product)

#updte brand to louis philppie

product["brand"]="louis philippie"

print(product)

#to add key 

product["mgf date"]="12-10-2023" #already ulla key word anenkil update cheyyum allenkil add cheyyum 

print(product)

#check key is exist or not 

if "brand" in product:

    print("exist")

else:

    print("not exist")

#add offer as 10 if offer exist else add offer as 20 

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)