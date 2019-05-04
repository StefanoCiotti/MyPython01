# dictionaryForm = {key1: value1, key2: value2, etc}
states = {42: "Washington", 50: "Hawaii", 1: "Delaware"}
# prints Washington
print(states[42])
# prints Hawaii
print(states[50])
# prints Delaware
print(states[1])

# empty dictionary
Dict = {}
# adds the key 30 and its value "Wisconsin"
# to the dictionary Dict
Dict[30] = "Wisconsin"
# adds the key 21 and its value "Illinois"
# to the dictionary Dict
Dict[21] = "Illinois"
# lenOfDict is assigned the length of Dict.
lenOfDict = len(Dict) # lenOfDict = 2

# example dictionary
moreStates = {10: "Virginia", 15: "Kentucky", 48: "New Mexico"}
# prints New Mexico
print(moreStates[48])
# reassigns the key 48 the value Arizona
moreStates[48] = "Arizona"
# prints Arizona
print(moreStates[48])

evenMoreStates = {3: "New Jersey", 17: "Ohio", 19: "Indiana"}
# removes the key: value pair 17: "Ohio" from evenMoreStates
del evenMoreStates[17]
# prints {19: 'Indiana', 3: 'New Jersey'}
print(evenMoreStates)

#------------------------------------

