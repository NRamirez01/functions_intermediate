# 1
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15 # 1
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students)
students[0]['last_name'] = 'Bryant' # 2
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] =  'Andres' #3
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30 # 4
print(students)
print(sports_directory)
print(z)
print("")
# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterateDictionary(rollcall):
#     for i in range(len(rollcall)):
#         dict = rollcall[i]
#         first_name = list(dict.keys())[0] #I gave up on trying to do a nested loop.
#         last_name = list(dict.keys())[1]
#         print("{} - {}, {} - {}".format(first_name, dict['first_name'], last_name, dict['last_name']))
# iterateDictionary(students) 
# I FINALLY FIGURED OUT HOW TO AVOID USING THE [0] and [1] FROM ABOVE
def iterateDictionary(rollcall): 
        i = 0
        while i < len(rollcall):
            for first, last in rollcall:
                dict = rollcall[i] #to consolidate a bit
                print("{} - {}, {} - {}".format(first, dict[first], last, dict[last]))
                i += 1
iterateDictionary(students) 
print("")
# 3
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {
        'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def interateDictionary2(key, names):
    for name in names:
        print(name[key])
interateDictionary2('first_name',students)
print("")
interateDictionary2('last_name',students)
print("")
# 4 I'm proud of this one
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for i in dict:
        if i == 'locations':
            locations = dict[i]
            print(str(len(locations)), i.upper())
            for city in locations:
                print(city)
            print("")
        if i == 'instructors':
            instructors = dict[i]
            print(str(len(instructors)), i.upper())
            for names in locations:
                print(names)
printInfo(dojo)

