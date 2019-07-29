import random

articles = ["the", "a", "etc"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

count = 0
while count < 5:
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