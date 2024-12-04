

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

#oder_summary

order_summary={}

for items in orders:

    if items in order_summary:

        order_summary[items]+=1

    else:

        order_summary[items]=1

print(order_summary)