cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

#print count of vehicles

print(f"total vehicles= {len(cars)}")

#print available colours of baleno

baleno_colours=[c.get("colors") for c in cars if c.get("name")=="baleno"]

print(baleno_colours[0]) #[0] koduthathu oru listinu akathulla veroru listintae values nae edukkan athintae index koduthal mathy


#print all brands

all_brands=[c.get("brand") for c in cars] #but inganae koduthal same brnads repeated aay print aakum 

#athu mattan namukku dict nae set aakyal mathy duplicates verathilla

print(set(all_brands))

#print cars available in amt transmission 

amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_cars)

#cars available in  blue colour

blue_colour_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_colour_cars)

#print all transmissions

all_trnasmissions=[t for c in cars for t in c.get("transmissions")]

# all_trnasmissions={t for c in cars for t in c.get("transmissions")} --> sqaure brackets maty curly brackets koduthal athu set akum 

print(set(all_trnasmissions))

#print all colours 

all_colours={color for c in cars for color in c.get("colors")}

print(all_colours)

#most costly car

costly_car=max(cars,key=lambda d:d.get("price"))

print(costly_car.get("name"))

low_cost=min(cars,key=lambda d:d.get("price"))

print(low_cost.get("name"))

sorted_cars=sorted(cars,key=lambda d:d.get("price")) #ithu print akiyyal full listum print aakum ithu list aanu ithil get funtion work aakilla

sorted_cars_name=[c.get("name") for c in sorted_cars]  

print(sorted_cars_name)

#carntae name an price venam 

sorted_cars_name_price={c.get("name"):c.get("price") for c in sorted_cars}

print(sorted_cars_name_price)

#name and rand values vannal enganae eg:name:price,brand 

sorted_cars_name_price_brand={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_cars}

print(sorted_cars_name_price_brand)  #randu values naem koody cherth oru listil angu kodukkam 

