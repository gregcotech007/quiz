# QuizMaster => A multiple-choice quiz game made in Python

[View the Live Project here - QuizMaster](https://p3-mc-quiz.herokuapp.com/)

## Table of Contents
* [How to Play!](#how-to-play)
* [User Stories](#user-story)
* [Features](#features)


## About QuizMaster
The game "QuizMaster" is an online interactive game that provides a list of questions to the player and provides
3 multiple-choice answers to choose from. 


## How to Play!

After the website link loads, the user is presented with the welcome message and is then asked the first randomised question.

The player is asked to input a, b, or c. Once they hit the return key, their answer is submitted and checked against the correct answer. If the player submits as blank, or a character or number that does not match, they will be asked to enter their response again. The play will be asked continually until they enter a valid input as a, b or c only.

If answer is correct, their score is incremented by 1 and the running total score is presented to the player with a message saying the answer is correct.

If the user gets the question incorrect, their score does not change and the player is presented with their running
score and a message that they got the question incorrect.

Once the player has attempted all questions, they will then be presented with their final score. It is broken down into 
3 results:

    - less than or equal to 5 = "Better luck next time." with total score provided.
    - less thank or equal to 15 = "Well done, great answers" with total score provided.
    - greater than 15 = "Congratulations Quizmaster!" with total score provided.

The player is then offered the option to play again by entering y/Y for Yes or n/N for No.

If the player selects 'y', the quiz game starts again.

If the player selects 'n', the player is presented with a message saying "Thank you for playing, come back soon!".


# User Experience (UX)
## User Story
Target Audience – A general audience of adults of all ages who would like to test their general knowledge of a multiple-choice quiz game.
- Play the game across different devices and browsers.
- Understand how to play the game.
- Play a game without a timer function.
- Know if the answer was correct or incorrect.
- Know the running total of my score.
- Know what happens if invalid or blank information is submitted.
- Have the option to play again or to finish the quiz game completely.
- Know the final score and how many questions were correct out of the total number of questions.
- To have fun.

#  Features
## Title Section
A welcome message is presented to the player when the game is started.

![Title](assets/images/welcome_start-quiz.png)

## Answers & Scoring
The player is presented with a multiple choice question at random and they are asked to choose a, b or c as their answer to submit. When the player enters a, b or c and hits enter, their answer is then validated. The player's score is incremented by 1 if correct and presented with a message to say they got it correct.

![Answer Correct](assets/images/score_correct_increment.png)

If the answer is incorrect, then the score does not change and they are presented a message saying the answer is incorrect and it shows their score does not change.

![Incorrect Correct](assets/images/score_incorrect_nochange.png)

The player continues to answer all questions until the final question has been answered.

When all answers have been attempted, the player is then presented with their total score.

- For a score 0 to 5, the player is presented with the following message:

![Score <= 5](assets/images/betterluck_playagain.png)

- For a score 6 to 15, the player is presented with the following message:

![Score <= 15](assets/images/welldone_playagain.png)

- For a score greater than 15, the player is presented with the following message:

![Score > 15](assets/images/congratsquizmaster_playagain.png)

- If the user experiences any issues with the game response, they can simply click on the "Run Program" button to restart the game.

![Run Program](assets/images/run-program.png)


# Technology Used
## Language
### Python
[Python](https://www.python.org/doc/essays/blurb/) is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.

## Programs
- [GitHub](https://github.com/):
    - GitHub was used to backup instances of GitPod Workspaces at intervals.
- [GitPod](https://gitpod.io/):
    - GitPod was used as the main Language Editor for programming the website.
- [Heroku](https://www.heroku.com/):
    - Heroku was used as the deployment platform for the CLI (command line interface) quiz game.

# Testing
## Devices & Browsers
- MacBook Pro
The QuizMaster game was tested on MacBook Pro running the latest MacOS Monterey (12.2.1) and Google Chrome (Version 99.0.4844.51 (Official Build) (arm64)). 
The quiz game performed well without issues and took input from the keyboard.

I also tested the QuizMaster game on the same device MacBook Pro running the latest MacOS Monterey (12.2.1) and Safari (Version 15.3). The quiz game loaded up correctly and displayed the welcome message and first question for player input, but it did not take any keyboard input response and therefore I was unable to play it.

- Windows 10
The QuizMaster game was tested on Windows 10 running Google Chrome (Version 98.0.4768.102 (Official Build)(64-Bit)).
The quiz game performed well without issues and took input from the keyboard.

I also tested it on the same Windows 10 computer running Microsoft Edge (Version 98.0.1108.56 (Official build)(64-Bit)) and also Mozilla Firefox (Version 97.0.1 (64-Bit)).
Both browsers worked seamlessly without any issues.

## Bug Testing
I found a bug when testing the play again option that they player was able to submit anything, for example, a number, as per the screenshot example and it responded as if the user selected n for no.

![Play Again Validation](assets/images/playagain_validate_bug.png)


## Code Validation
- [PEP8 Online](http://pep8online.com/):
    - This website was used validate the Python code for any errors.

    ![PEP8 Online - run.py](assets/images/pep8online_run_passed.png)

    ![PEP8 Online - questions.py](assets/images/pep8online_questions_passed.png)


# Deployment
Before deploying to Heroku, a requirements.txt was created by typing and submitting the following code:
pip3 freeze

Log in to Heroku with login credentials or create a new account if required.
When logged in, click the button labelled "New" from the dashboard in the top right corner.
From the "New" drop-down menu, select "Create New App".
A unique app name must be chosen. I chose "p3-mc-quiz".
Select a region, "United States" or "Europe". I chose "Europe" for my region.
Click on the "Create App" button.

On the next page, select the "Settings" Tab.
There is an option to create Config Vars", but in my case, there were not required.
On the Build Packs section, choose to add the following in the set order:
    - heroku/python
    - heroku/nodejs
Click on python and save changes, then nodejs and save changes.

Scroll to the top of the page and now choose the Deploy tab.
Select Github as the deployment method.
Confirm you want to connect to GitHub and sign-in with GitHub credentials, if required.
Search for the repository name and click the connect button.
Scroll to the bottom of the deploy page and select preferred deployment type:
Choose either "Enable Automatic" Deploys for automatic deployment when you push updates to Github or you can choose "Manual" which allows you to manually deployment when required.

Select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.
## Heroku
For deployment of the website to a live publicly accessible website, the following steps were required:
- Confirmed that correct repository is selected as 'quiz'

- Your site is published at https://p3-mc-quiz.herokuapp.com/

# Cloning
To clone a copy of the code in the repository, the following steps are required:
- Go to https://github.com and select the Repository called 'quiz'
- Click on the button called 'Code" and a pop-out window will show options to Clone through:
    - HTTPS
    - SSH
    - GitHub CLI
1. On GitHub.com, navigate to the main page of the repository.
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click 'Clipboard to copy'. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click 'Clipboard to copy'. To clone a repository using GitHub CLI, click Use GitHub CLI, then click 'Clipboard to copy'.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type > git clone and then paste the URL you copied earlier. 
    > $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7. Press Enter to create your local clone.
    > $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `Spoon-Knife`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
8. Repository Clone is now complete.

# Credits

## Tools


## Tutorials & Resources
- [GitHub: Clone a Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    - The link includes the full step-by-step instructions from GitHub Support on how to clone a repo.
- [Code Institute](https://codeinstitute.net)
    - The LMS tutorials were beneficial in giving me an insight into starting my first Python coding project.
- Code Institute: Mentor: 
    - Thanks to my Mentor who supported me throughout the project.