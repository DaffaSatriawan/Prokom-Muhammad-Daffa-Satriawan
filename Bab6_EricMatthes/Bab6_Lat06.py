#favorit codes from page 96
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

#coders
coders_favorit_languages = ['jen', 'sarah', 'edward', 'phil', 'aan', 'kay']

#print loop
for person in coders_favorit_languages:
    if person in favorite_languages:
        print (f"Halo {person} Thankyou for your respond")

    else:
        print (f"Halo {person} Pastikan lagi datamu")

        