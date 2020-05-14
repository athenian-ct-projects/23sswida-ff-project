# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)

#random number generator
import random
#input list for starting the game
start_list = ["Yes", "yes", "y", "Y", "yep", "Yep", "Yeah", "yeah", "ok", "Ok", "OK", "Okay", "okay", "k", "K"]
#questions
question1 = "What is the difference between an epidemic and a pandemic?"
question2 = "Where was the first reported case of the Spanish Flu?"
question3 = "When was the first confirmed case of coronavirus?"
question4 = "What does CDC stand for?"
question5 = "What does an epidemiologist mainly do?"
question6 = "What century was the Black Plague in?"
question7 = "How many people are estimated to have died from the Black Plague?"
question8 = "What is the mortality rate of rabies?"
question9 = "Which of the following is NOT a symptom of yellow fever?"
question10 = "What is Typhoid Mary's real name?"
question11 = "Which outbreak started in 1918?"
question12 = "About how many people have died from AIDS?"
question13 = "What is another name for smallpox?"
question14 = "How is Mononucleosis known for being transmitted?"
question15 = "What is the annual leading cause of death?"
question16 = "Approximately how many 'rare' diseases are there?"
question17 = "Which of the following is NOT a common symptom of Lyme Disease?"
question18 = "How common is Alzheimer's disease in people over 65?"
question19 = "How many adults in the US are considered obese?"
question20 = "What is believed to be the oldest human disease?"
trivia_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20]

#question 1 answers
queans1 = ["a.", "A.", "a", "A"]

def ask_question():
    random.choice(trivia_list) 
    for question1:  
        print("a. the size of the region the disease affects" +'\n'+ "b. the mortality rate" + '\n' + "c. how quickly the disease spreads" + '\n' + "d. virus vs bacteria")
        answer1 = input("Which letter is the correct answer? ")
            if answer in queans1:
                print("Correct!")
            else:
                print()

for random_cases>5000
    print("Oops! You reached over 5000 cases. Better luck next time!")
#instructions
start = input("Welcome to 'Cure That Disease!' To start the game, you will be given a number of cases between 1 and 5000. This is how many cases you have to begin with. You will then be given a series of questions. Before each question, you can 'bet' a number of cases. If you get the question right, that number is taken off your case count. If you get it wrong, it is added to your case count. Be careful, because if your case count goes over 5000, you lose the game. There are only 20 questions, so keep that in mind when making your bets. Your objective is to get down to 0 cases. Are you ready? " )
while start not in start_list:
    print("Sorry, I didn't understand that. Try typing in a different answer.")
    start = input("Are you ready? ")
#number of cases
random_cases = random.randint(1,5001)
print ("We have just discovered a new disease! There are already " + str(random_cases) + " confirmed cases.")
#naming the disease
disease_name = input("What should we call this disease? ")
for random_cases > 5000:
    print("Oops! You reached over 5000 cases. Better luck next time!")
for random_cases = 0:
    print("You cured the disease! Congratulations!")
