# l1 = ['b','c','d','b','c','a','a']
# l2 = list(set(l1))
# print(l2)

# words = ['whOO','lOOve','sAAm']
# result = []
# for word in words:
#     read = list(set(word))
#     result.append(word)
# print(result)

words= ['whOO','lOOvEE','sAAm','pOOOL','illegel','committeee','committe']
word2 = []
yuan = 'AEIOUaeiou'
for word in words:
    i = 0
    flag = True
    while i < len(word):
        if i>=1 and word[i] in yuan and flag:
            if word[i] == word[i-1]:
                i += 1 
                flag = False
                continue
        else:
            flag = True

        if word[i].isupper():
            letter = word[i].lower()

        else:
            letter = word[i]

        word2.append(letter)
        i += 1

    word2.append(' ')

word2 = ''.join(word2)

print(word2)