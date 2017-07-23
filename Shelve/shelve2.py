import shelve

with shelve.open('ShelfTest') as fruit:
    fruit= {'orange': "a sweet, orange citrus fruit",
            'apple' : "good for making cider",
            'lemon' : "a sour, yellow citrus fruit",
            'grape': "a small, sweet fruit growing in bunches",
            'lime' : "a sour, green citrus fruit"}

    print(fruit["orange"])

print(fruit["lime"])
print(fruit)
#The above lines would print out the dictionary details even though the ShelfTest is closed