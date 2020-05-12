# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)
start_list = ["Yes", "yes", "y", "Y", "yep", "Yep", "Yeah", "yeah", "ok", "Ok", "OK", "Okay", "okay", "k", "K"]

start = input("Welcome to 'Cure That Disease!' To start the game, you will be given a number of cases between 1 and 5000. This is how many cases you have to begin with. You will then be given a series of questions. Before each question, you can 'bet' a number of cases. If you get the question right, that number is taken off your case count. If you get it wrong, it is added to your case count. If you get it wrong, you will get a second chance at the question and if you get it right the second time, you will get half of your bet taken off the case count. Be careful, because if your case count goes over 5000, you lose the game. There are only 20 questions, so keep that in mind when making your bets. Your objective is to get down to 0 cases. Are you ready?" )
if input == start_list:
    print("Great! Let's go.")
else:
    print("Sorry, I didn't understand that. Try typing in a different answer.")