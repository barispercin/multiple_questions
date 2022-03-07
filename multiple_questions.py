from Question import Question

question_prompts = [
    "Elmaların rengi ne ?\n(a) kırmızı/yeşil\n(b) kırmızı\n(c) yeşil\n\n)",
    "Muzların durumu ne ?\n(a) çok kötü\n(b) kötü\n(c) iyi\n\n)",
    "Çileklerin durumu ne ?\n(a) çok kötü\n(b) kötü\n(c) iyi\n\n)",
]   
   
questions = [
       Question(question_prompts[0],"a"),
       Question(question_prompts[1],"c"),
       Question(question_prompts[2],"b"),
]
def run_test(questions):
        score=0
        answer=""
        for question in questions:
            answer == input(question.prompt)
            if answer == question.answer:
                score += 1
        print("Scorun " + str(score) + "/" + str(len(questions)))

run_test(questions)