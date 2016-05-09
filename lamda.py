"""script 1"""

my_list = range(1,100)
print filter(lambda x: x % 3 == 0, my_list)

"""script 2"""

squares=[x**2 for x in range(1,11)]
print filter(lambda x: x>30and x<70,squares)

"""scipt 3"""

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=='Python',languages)
