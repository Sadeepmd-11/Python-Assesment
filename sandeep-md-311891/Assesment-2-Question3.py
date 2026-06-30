def character_frequency(text):
    frequency = {}
    
    for char in text.lower():
        if char != " ": 
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    return frequency



text = "Python Programming"

result = character_frequency(text)

print("Character Frequency:", result)