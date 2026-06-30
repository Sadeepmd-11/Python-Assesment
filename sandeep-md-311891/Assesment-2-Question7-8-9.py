def is_palindrome_sentence(sentence):
    cleaned = ""

    for char in sentence:
        if char.isalnum():  # keeps only letters and numbers
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

sentence = "A man, a plan, a canal: Panama"

print(is_palindrome_sentence(sentence))

#-----------------------------------------------
#Question8

words = ["apple", "education", "ice", "ocean", "python", "umbrella"]

res=[x for x in words if len(x) > 5 and x[0].lower() in 'aeiou']
print(res)

#--------------------------------------------------
#Question9

def duplicate(list):
    dup=[]

    for i in list:
        if i not in dup:
            dup.append(i)

    return dup

list=[1, 2, 2, 3, 1, 4, 2]

print(duplicate(list))