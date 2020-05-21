# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)

#random number generator
import random
#input list for starting the game
start_list = ["Yes", "yes", "y", "Y", "yep", "Yep", "Yeah", "yeah", "ok", "Ok", "OK", "Okay", "okay", "k", "K"]
#questions
question1 = ("What is the difference between an epidemic and a pandemic?" + '\n' + "a. the size of the region the disease affects" + '\n' + "b. the mortality rate" + '\n' + "c. how quickly the disease spreads" + '\n' + "d. virus vs. bacteria")
question2 = ("Where was the first reported case of the Spanish Flu?" + '\n' + "a. Spain " + '\n' + "b. Kansas" + '\n' + "c. Venezuela" + '\n' + "d. Egypt")
question3 = ("When was the first confirmed case of coronavirus?" + '\n' + "a. January 21, 2020" + '\n' + "b. December 2, 2019" + '\n' + "c. December 31, 2019" + '\n' + "d. February 3, 2020")
question4 = ("What does CDC stand for?" + '\n' + "a. Center for the Doctors of California"  + '\n' + "b. Coronavirus Death Count" + '\n' + "c. California Department of Care"  + '\n' + "Center for Disease Control")
question5 = ("What does an epidemiologist mainly do?" + '\n' + "a. Study disease and how to control them"  + '\n' + "b. Help surgeons deliver the right amount of anesthetic"  + '\n' + "c. Study groups of people within certain demographics"  + '\n' + "d. Write newspaper and magazine articles about disease outbreaks")
question6 = ("Which century was the Black Plague in?" + '\n' + "a. 1200's"  + '\n' + "b. 1300's"  + '\n' + "c. 1400's" + '\n' + "d. 1500's")
question7 = ("How many people are estimated to have died from the Black Plague?" + '\n' + "a. 100,000-600,000" + '\n' + "b. 3 million-12 million" + '\n' + "c. 75 million-200million" + '\n' + "d. 250 million+")
question8 = ("What is the mortality rate of rabies?" + '\n' + "a. ~61%" + '\n' + "b. ~64%" + '\n' + "c. ~89%" + '\n' + "d. ~100%")
question9 = ("Which of the following is NOT a symptom of yellow fever?" + '\n' + "a. Swollen lymph nodes" + '\n' + "b. Yellowing skin and/or eyes" + '\n' + "c. Internal bleeding" + '\n' + "d. Organ failure")
question10 = ("What is Typhoid Mary's real name?" + '\n' + "a. Mary J. Blige" + '\n' + "b. Mary Mallon" + '\n' + "c. Mary Pope Osborn" + '\n' + "d. Mary Wollstonecraft")
question11 = ("Which outbreak started in 1918?" + '\n' + "a. Cocolizti Epidemic" + '\n' + "b. Yellow Fever Epidemic" + '\n' + "c. Spanish Influenza" + '\n' + "d. Asian Flu")
question12 = ("About how many people have died from AIDS?" + '\n' + "a. 700,000" + '\n' + "b. 18 million" + '\n' + "c. 98 million" + '\n' + "d. 35 million")
question13 = ("What is another name for smallpox?" + '\n' + "a. Variola Major/Minor" + '\n' + "b. Pharyngitis" + '\n' + "c. Anaplasmosis" + '\n' + "d. Valley Fever")
question14 = ("How is mononucleosis known for being transmitted?" + '\n' + "a. Air" + '\n' + "b. Kissing" + '\n' + "c. Skin contact" + '\n' + "d. It isn't contagious")
question15 = ("What is the annual leading cause of death?" + '\n' + "a. Respiratory diseases" + '\n' + "b. Alzheimer's" + '\n' + "c. Heart disease" + '\n' + "d. Cancer")
question16 = ("Approximately how many 'rare' diseases are there?" + '\n' + "a. 2,100" + '\n' + "b. 3,000" + '\n' + "c. 6,800" + '\n' + "d. 7,000")
question17 = ("Which of the following is NOT a common symptom of Lyme Disease?" + '\n' + "a. Shortness of breath" + '\n' + "b. Fever" + '\n' + "c. Chills" + '\n' + "d. Muscle aches")
question18 = ("How common is Alzheimer's in people over 65?" + '\n' + "a. 1 in 11" + '\n' + "b. 1 in 14" + '\n' + "c. 1 in 16" + '\n' + "1 in 63")
question19 = ("How many adults in the US are considered obese?" + '\n' + "a. 480,000" + '\n' + "b. 36 million" + '\n' + "c. 70 million" + '\n' + "d. 99 million")
question20 = ("What is believed to be the oldest human disease?" + '\n' + "a. Smallpox" + '\n' + "b. Malaria" + '\n' + "c. Cholera" + '\n' + "d. Leprosy")
trivia_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20]

#question answers
queans1 = ["A"]
queans2 = ["B"]
queans3 = ["C"]
queans4 = ["D"]


def ask_question(queans1, trivia_list, random_cases):
    x = random.choice(trivia_list) 
    print(x)
    if x == trivia_list[0]:
        bet1 = int(input("How many cases are you betting? "))
        answer1 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer1 in queans1:
            print("Correct!")
            random_cases -= bet1
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet1
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[1]:
        bet2 = int(input("How many cases are you betting? "))
        answer2 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer2 in queans2:
            print("Correct!")
            random_cases -= bet2
            print("There are now " + str(random_cases)+ " cases")
        else:
            print("Incorrect")
            random_cases += bet2
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[2]:
        bet3 = int(input("How many cases are you betting? "))
        answer3 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer3 in queans3:
            print("Correct!")
            random_cases -= bet3
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet3
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[3]:
        bet4 = int(input("How many cases are you betting? "))
        answer4 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer4 in queans4:
            print("Correct!")
            random_cases -= bet4
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet4
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[4]:
        bet5 = int(input("How many cases are you betting? "))
        answer5 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer5 in queans1:
            print("Correct!")
            random_cases -= bet5
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet5
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[5]:
        bet6 = int(input("How many cases are you betting? "))
        answer6 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer6 in queans2:
            print("Correct!")
            random_cases -= bet6
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet6
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[6]:
        bet7 = int(input("How many cases are you betting? "))
        answer7 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer7 in queans3:
            print("Correct!")
            random_cases -= bet7
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet7
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[7]:
        bet8 = int(input("How many cases are you betting? "))
        answer8 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer8 in queans4:
            print("Correct!")
            random_cases -= bet8
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet8
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[8]:
        bet9 = int(input("How many cases are you betting? "))
        answer9 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer9 in queans1:
            print("Correct!")
            random_cases -= bet9
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet9
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[9]:
        bet10 = int(input("How many cases are you betting? "))
        answer10 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer10 in queans2:
            print("Correct!")
            random_cases -= bet10
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet10
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[10]:
        bet11 = int(input("How many cases are you betting? "))
        answer11 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer11 in queans3:
            print("Correct!")
            random_cases -= bet11
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet11
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[11]:
        bet12 = int(input("How many cases are you betting? "))
        answer12 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer12 in queans4:
            print("Correct!")
            random_cases -= bet12
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet12
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[12]:
        bet13 = int(input("How many cases are you betting? "))
        answer13 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer13 in queans1:
            print("Correct!")
            random_cases -= bet13
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet13
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[13]:
        bet14 = int(input("How many cases are you betting? "))
        answer14 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer14 in queans2:
            print("Correct!")
            random_cases -= bet14
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet14
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[14]:
        bet15 = int(input("How many cases are you betting? "))
        answer15 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer1 in queans3:
            print("Correct!")
            random_cases -= bet15
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet15
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[15]:
        bet16 = int(input("How many cases are you betting? "))
        answer16 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer16 in queans4:
            print("Correct!")
            random_cases -= bet16
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet16
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[16]:
        bet17 = int(input("How many cases are you betting? "))
        answer17 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer17 in queans1:
            print("Correct!")
            random_cases -= bet17
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet17
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[17]:
        bet18 = int(input("How many cases are you betting? "))
        answer18 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer18 in queans2:
            print("Correct!")
            random_cases -= bet18
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet18
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[18]:
        bet19 = int(input("How many cases are you betting? "))
        answer19 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer19 in queans3:
            print("Correct!")
            random_cases -= bet19
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet19
            print("There are now " + str(random_cases) + " cases")
    if x == trivia_list[19]:
        bet20 = int(input("How many cases are you betting? "))
        answer20 = input("Which letter is the correct answer? (A, B, C, or D) ")
        if answer20 in queans4:
            print("Correct!")
            random_cases -= bet20
            print("There are now " + str(random_cases) + " cases")
        else:
            print("Incorrect")
            random_cases += bet20
            print("There are now " + str(random_cases) + " cases")
    return random_cases
  
        
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
while 0<random_cases<5000:
    random_cases = ask_question(queans1, trivia_list, random_cases)
    if random_cases>5000:
        print("Oops! You reached over 5000 cases. Better luck next time!")
        break
    elif random_cases == 0:
        print("Congrats! You won!")
        break
