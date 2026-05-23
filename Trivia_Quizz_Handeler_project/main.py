import requests
import html


class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl ="https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questtionlist = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl+str(numQuestions))

        if response.ok:
            data = response.json()
            restults = data["results"]

            for q in restults:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1', 'yes']
 
                qObj = Question(category, questionStr , correctAnswerFlag)
                self.questtionlist.append(qObj)
    
    def startQuiz(self):
        print("Welcome in Quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questtionlist)
        
        while(n<numQuestions):
            q= self.questtionlist[n]
            print("Question number: " + str(n) + ": ", q.questionStr)
            print("Anwer flag: ", q.correctAnswerFlag)
            
            answer = input("Give correct answer as y/n:")
            answerBool = False
            if answer == "y": answerBool = True
            
            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers +=1
            else:
                print("Not correct!")
            n+=1

        print("Number of correct answers: ", numCorrectUserAnswers, "from ", len(self.questtionlist), " questions")

quiz = Quiz(10)
quiz.startQuiz()