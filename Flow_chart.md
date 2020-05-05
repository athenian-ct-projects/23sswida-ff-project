# Project Flow Chart

You may write your flow chart here or upload it as a separate file. 
* If you upload it, be sure to upload a new version at the end, keeping the original version.
* If you use this one, the original will still be available so you just need to save (commit) each time you make changes.

1. Prompt user for name of epidemic
2. Generate random number between 1-1000 for the number of starting cases
3. Function created to prompt user for their 'bet'
4. Before each trivia question, the bet function is called.
5. Another function is created to pick a question from a list of all the questions
6. The user is given a list of possible answers (a., b., c., d.)
7. If the answer is correct, the 'bet' is subtracted from the number of cases, and the question is removed from the list
8. If the answer is incorrect, the user can try again
    a. If the get it right the second time, half of the bet is removed from the cases
    b. If they get it wrong, the bet is added to the number of cases
    c. Regardless of whether they get it right or not, the question is removed from the list after the second try.
9. If the cases get to 0, the user wins.
10. If there are no questions left, or the cases get to over 5000, the user loses.
