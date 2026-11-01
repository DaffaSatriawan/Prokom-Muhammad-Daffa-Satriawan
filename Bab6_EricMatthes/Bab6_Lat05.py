#rivers
rivers = {
    'bengawan solo': 'solo',
    'kapuas':'kalimantan',
    'amazon': 'brazil'
    }

#print all
print ("=================================================")
print ("informasi keseluruhan")
for sungai, berasal in rivers.items():
    print (f"sungai {sungai} berasal dari {berasal}")

#print key
print ("=================================================")
print ("informasi nama sungai")
for sungai in rivers.keys():
    print (f"sungai {sungai}")

#print values
print ("=================================================")
print ("Infomasi asal sungai")
for asal in rivers.values():
    print (f"Asal {asal}")