import random

a = b = c = d = e = f = 0
angle = 0
questions = []


def addQuestion(question):
    questions.append(question)


def randomVectorValueGenerate():
    a = random.randrange(15)
    b = random.randrange(15)
    c = random.randrange(15)
    d = random.randrange(15)
    e = random.randrange(15)
    f = random.randrange(15)


def randomAngleGenerate():
    angle = angles[random.randrange(6)]


angles = [0, 30, 45, 60, 90, 180]

for i in range(5):
    for j in range(5):
        randomVectorValueGenerate()
        questionOne = 'Find the addition of ' + str(a) + 'i+' + str(b) + 'j+' + str(c) + 'k' + ' and ' + str(
            d) + 'i+' + str(e) + 'j+' + str(f) + 'k'
        questions.append(questionOne)

    for j in range(5):
        randomVectorValueGenerate()
        questionTwo = 'Find the dot product of ' + str(a) + 'i+' + str(b) + 'j+' + str(c) + 'k' + ' and ' + str(
            d) + 'i+' + str(e) + 'j+' + str(f) + 'k'
        questions.append(questionTwo)

    for j in range(5):
        randomVectorValueGenerate()
        randomAngleGenerate()
        questionThree = 'Find the dot product of ' + str(a) + 'i+' + str(b) + 'j+' + str(c) + 'k' + ' and ' + str(
            d) + 'i+' + str(e) + 'j+' + str(f) + 'k' + ' , provided angle between them is ' + str(angle) + ' degrees.'
        questions.append(questionThree)

    for j in range(5):
        randomVectorValueGenerate()
        randomAngleGenerate()
        questionFour = 'Find the cross product of ' + str(a) + 'i+' + str(b) + 'j+' + str(c) + 'k' + ' and ' + str(
            d) + 'i+' + str(e) + 'j+' + str(f) + 'k' + ' , provided angle between them is ' + str(angle) + ' degrees.'
        questions.append(questionFour)

# for question in questions:
#	print(question)

