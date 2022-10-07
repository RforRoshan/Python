a='16,56,890'
hike='56%'
a=a.replace(",","")
hike=hike.replace("%","")
a=float(a)
hike=float(hike)
print(a*hike/100)