from json import load

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\countries.json",encoding="UTF-8")

data=load(f)

##print number of data

#print(len(data))

###all country names 

all_country_names=[country.get("name") for country in data]

#print(all_country_names)

####print all regions

all_regions=[country.get("region") for country in data]

#print(set(all_regions))

#####region wise count of countries

region_count={region:all_regions.count(region) for region in all_regions}

#print(region_count)

##max region count

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count)

#value koody venam enkil

#print(max_region_count,region_count.get(max_region_count))

#print capital of specific country

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

#print(country_capital)

###countries with most number of borders 

country_border_count={country.get("name"):len(country.get("borders",[]))for country in data}

#print(country_border_count)

##len(country.get("borders",[]))  --> chila countiresnu border illa athintae len edukumbol error verum so angana verathae irikkan 
##.get("borders",[]) oru [] empty set kodukkum appol border illatha countriesnu value oru null set athayathu len =0 verum 

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_border_country)

####most populated country

most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")

#print(most_populated_country)

#borders of india 

#alpha_three_code=[country.get("borders") for country in data if country.get("name")=="India"][0]
#[0] koduthathu enthinanennu vechal [0] illathae process cheyumbol rand listil ayittanu borders verunnathu athayathu borders oru listilum
#aa borders edukkan nammal kodutha list comprehensionum koody randu list so parent listl ninnu child list nae mathram edukkan [0] kodukthu

#ithu sherikum borders alla aa countriesntae alpha3code aanu 

#borders country names kittan

alpha_three_code=[country.get("borders") for country in data if country.get("name")=="India"][0]  #ini ivdae country name matty koduthal borders mary kittum

for code in alpha_three_code:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))


