import shelve

with shelve.open("locations") as location_dict:

    # location_dict ['0']= {"desc": ["You are sitting in front of a computer learning Python"],
    #                  "exits": [],
    #                  "namedExits": []}
    # location_dict ['1']= {"desc": ["You are standing at the end of a road before a small brick building"],
    #                  "exits": [{"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}],
    #                  "namedExits": [{"2": 2, "3": 3, "5": 5, "4": 4}]}
    # location_dict ['2']= {"desc": ["You are at the top of a hill"],
    #                  "exits": [{"N": 5, "Q": 0}],
    #                  "namedExits": [{"5": 5}]}
    # location_dict ['3']= {"desc": ["You are inside a building, a well house for a small stream"],
    #                  "exits": [{"W": 1, "Q": 0}],
    #                  "namedExits": [{"1": 1}]},
    # location_dict ['4']= {"desc": ["You are in a valley beside a stream"],
    #                  "exits": [{"N": 1, "W": 2, "Q": 0}],
    #                  "namedExits": [{"1": 1, "2": 2}]}
    # location_dict ['5']= {"desc": ["You are in the forest"],
    #                  "exits": [{"W": 2, "S": 1, "Q": 0}],
    #                  "namedExits": [{"2": 2, "1": 1}]}

    print(location_dict['0']["desc"])
    print(location_dict['0']["exits"])
    print(location_dict['0']["namedExits"])
    print(location_dict['1']["desc"])
    print(location_dict['1']["exits"])
    print(location_dict['1']["namedExits"][2])
    #print(location_dict['1'])
    print(location_dict['2'])
    print(location_dict['3'])
    print(location_dict['4'])



#with shelve.open("vocabulary") as vocabulary_dict:
    # vocabulary_dict ["QUIT"]= "Q"
    # vocabulary_dict ["NORTH"]= "N"
    # vocabulary_dict ["SOUTH"]= "S"
    # vocabulary_dict ["EAST"]= "E"
    # vocabulary_dict ["WEST"]= "W"
    # vocabulary_dict ["ROAD"]= "1"
    # vocabulary_dict ["HILL"]= "2"
    # vocabulary_dict ["BUILDING"]= "3"
    # vocabulary_dict ["VALLEY"]= "4"
    # vocabulary_dict ["FOREST"] ="5"
