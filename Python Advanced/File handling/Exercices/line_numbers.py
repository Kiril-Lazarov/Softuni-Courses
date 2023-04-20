import string
punctuation = str(string.punctuation)
number = 0

with open('./text.xt', 'r') as text:
    lines = text.readlines()
    for sentence in lines:
        punctuation_marks_count = 0
        number +=1
        for letter in sentence:
            if letter in punctuation:
                sentence = sentence.replace(letter, '')
                punctuation_marks_count +=1
            if letter == ' ':
                sentence = sentence.replace(letter, '')
            if letter == '\n':
                sentence = sentence.replace(letter, '')
        letters = len(sentence)
        with open('output.txt', 'a') as output:
            output.write(f'Line {number} {lines[number-1].strip()}({letters})({punctuation_marks_count})\n')
