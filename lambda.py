nums = range(2, 50) 
for i in range(2, 8): 
	nums = filter(lambda x: x == i or x % i, nums)

print nums
----------------------------------------------------------------------------------
sentence = 'It is raining cats and dogs'
words = sentence.split()
print words
lengths = map(lambda word: len(word), words)
print lengths
