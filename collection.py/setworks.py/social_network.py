users=["rahul","rohit","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

#follow suggestions ["sanju","pandya","siraj"]

user_set=set(users)

rahul_followers_set=set(rahul_followers)

rahul_suggestions=user_set.difference(rahul_followers_set)

print(rahul_suggestions)

mutual_friend=rahul_followers_set.intersection(set(sanju_followers))

print(mutual_friend)



