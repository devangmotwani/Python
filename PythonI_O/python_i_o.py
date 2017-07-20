#data = open("C:\\Users\\devan\\GitRepositories\\Python\\PythonI_O\\sample.txt",'r')
# data = open("sample.txt",'r')
# for line in data:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# data.close()

cities=["Fairfax","Arlington", "DC", "New York"]

with open("cities.txt",'w') as city_file:
    for city in cities:
        print(city, file=city_file)