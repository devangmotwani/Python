import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["orange"])
    print(fruit["lime"])

print(fruit)

#The above line would not print out the details of the shelve when the file is closed