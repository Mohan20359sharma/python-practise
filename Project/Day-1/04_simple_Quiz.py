questions = {
    "What is the father of gravity ?":"a",
    "What is 2 + 2 ?":"b",
    "Who wrote Ramayan":"c"
}

answers={
    "a" : "Newtown",
    "b" : "4",
    "c" : "Tulsidas"
}
score = 0
for question,answer in questions.items():
    print(question)
    print(f"a) {answers['a']}\nb) {answers['b']}\nc){answers['c']}")
    user_answer = input("choose an answer(a, b, c): ")
    if user_answer == answer:
        score += 1
print(f"Your score is {score}/{len(questions)}")