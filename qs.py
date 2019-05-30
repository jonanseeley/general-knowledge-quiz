from bs4 import BeautifulSoup as bs

with open("jawn.html") as f:
    soup = bs(f, features="html.parser")

table = soup.find_all(id="Tab1")[0]
tds = table.find_all("td")

questions = []
answers = []
for i in range(2, len(tds), 17):
    text = tds[i].p.contents[0].split(" ")
    questions.append(" ".join(text[0:-1]))
    answers.append(text[-1][1:-1])

jawn = "\", \"".join(questions)
print(f"[\"{jawn}\"]")

correct = 0
'''
for i, (q, a) in enumerate(zip(questions, answers)):
    print(q)
    x = input()
    if x == a:
        print("Correct!")
        correct += 1
    else:
        print(f'Your answer: {x}\tCorrect answer: {a}')
    print(f"You have gotten {correct} out of {i+1} correct!\n") 
    '''
