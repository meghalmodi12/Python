import random

articles = ["the", "a", "etc"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

count = 0
numberOfLine = 5

line = input("Enter number of line to be printed : ")
if line:
    try:
        numberOfLine = int(line)
    except ValueError as err:
        print(err)
        
while count < numberOfLine:
    count += 1
    structure = random.randint(1, 2)
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    if structure == 1:
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb,)