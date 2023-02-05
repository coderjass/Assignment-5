word=list()
print('Enter your words below. \nEnter "Done" when you are done.')
while 'Done' not in word:
    string=str(input('Enter your word here: '))
    word.append(string)
word.remove('Done')
for x in word:
    z=word.count(x)
    print(x, 'has occured', z, 'times in the given list of words')