# SortingHat_ChatBot
![Alt](/Python_Bot/hat.jpg "The sorting hat")
## Class Description
Calling all Harry Potter fans! Come build a simple chatbot based on the sorting hat! We'll go over the NLP/AI that goes into writing a legit chatbot before trying your hand at your own, simplified sorting hat! All experience levels are welcome!

## Instructions for setup
1. Make a github account if you don't already have one and log in
2. Click the "Fork" button in the top right corner to make your own copy of the repository
3. Go to your forked repository and clone onto your local machine
For beginners, here's a tutorial on [how to fork and clone with git](https://help.github.com/en/articles/fork-a-repo "Forking a Repo with Git").

## Repository Contents
### Python_Bot
Contains code for a simplified chatbot that does not use AI/NLP (HPSortingBot.py) and a "multipage" skeleton example for those who want to try making a GUI (tkintertest.py). There is also a picture of a sorting hat (hat.jpeg) that students can incorporate on their own if they want to add a GUI/change up the code. 

The logic of the sorting is based on Reddit user u/N1ffler's [analysis of the pottermore sorting quiz](https://www.reddit.com/r/Pottermore/comments/44os14/pottermore_sorting_hat_quiz_analysis/ "Pottermore Sorting Hat Quiz analysis"). There are 28 possible question and 8 question subsets to choose from, resulting in 8 total questions per test. For subgroups with multiple question possibilites, the question is chosen at random by using a randomized number flag. Based on the percentage of each house that chose each answer to a question, points are added to a user's Gryffindor, Ravenclaw, Hufflepuff, and Slytherin scores. 
#### Example
![Alt](/probabilities_example.PNG "Example probabilites for a question")
In this example, for users who choose dawn, 73 is added to gryffindor, 73 to ravenclaw, 30 to hufflepuff, and 26 to slytherin.


At the end, the user has the option to see how they score across houses. This is calculated by dividing the user's individual house points by the user's total points across all houses to get a house compatibility percentage. 

## Possible improvements
- fix spacing for certain multiline questions

### For advanced students to try:
- change "I didn't quite get that" to a method that supplies randomized multiple synonymous responses
- add NLP:
    use fuzzywuzzy to approximate matching of inputs to the questions instead of returning a b c d etc for multi-answer questions
- create a GUI using tkinter (could use pages as per the given example)
