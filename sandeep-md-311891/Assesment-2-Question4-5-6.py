def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


word1 = "listen"
word2 = "silent"

result = is_anagram(word1, word2)

print(f'Is "{word1}" an anagram of "{word2}"? {result}')

#Question5

def flat(nested):
    flat_list = []

    for item in nested:
        if isinstance(item, list):
            flat_list += flat(item)
        else:
            flat_list.append(item)

    return flat_list



nested = [1, [2, 3], [4, [5, 6]], 7]


print("Flat:", flat(nested))

#---------------------------------------------------
#Question-6

def reverse_words(sentence):
    words = sentence.split( )
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)

sentence = "Python is awesome"

print(reverse_words(sentence))

#-------------------------------------------------------


