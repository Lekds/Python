import time
print ("Welcome to Zhaoqi's quiz on the CPU")
print ('')
time.sleep(1)
print ('Your score at the end will be based on how many correct answers you get compared to the number of guesses you take.')
print ('')
time.sleep(1)
level=0
score=0
guesses=0
while level not in ['easy', 'medium', 'hard']:
    level = input ('Please select a difficulty (easy, medium, or hard): ').lower() 
easy_questions = ['CPU stands for _ Processing Unit', 'There are _ major registers in a CPU', 'Who came up with the Von Neumann Architecture?']
medium_questions = ['Which is the fastest kind of memory for the CPU to access? RAM or cache?', 'Data travels between the processor and the computers RAM through the address and data _', 'Overclocking is the action of increasing a CPUs _ speed']
hard_questions = ['During the Fetch phase of the FDE cycle, The first step the CPU carries out is to fetch some data and instructions (program) from main memory then store them in its own internal temporary memory areas. These memory areas are called _', 'During the Fetch phase of the FDE cycle, The CPU places the address of the next item to be fetched on to the _ bus.', 'The CPU is designed to understand a specific set of commands. These are called the _ set of the CPU. Each make of CPU has a different _ set.']
easy_answers = ['central','5','von neumann']
medium_answers = ['cache','bus','clock']
hard_answers = ['registers','address','instruction']
if level == 'easy':
    questions = easy_questions
    answers = easy_answers
elif level == 'medium':
    questions = medium_questions
    answers = medium_answers
elif level == 'hard':
    questions = hard_questions
    answers = hard_answers
number_of_questions = 3
question_number = 0
def check_answer(user_answer, questions, answers):
    global guesses
    global question_number
    global score
    if user_answer in answers:
        print ('')
        print ('Correct!')
        score += 1
        guesses += 1
        question_number += 1
    else:
        print ('')
        print ('Not quite, please try again')
        guesses += 1
    return
while question_number < number_of_questions:
    question = questions[question_number]
    user_answer = answers[question_number]
    print('')
    user_answer = input(question + ': ').lower() 
    check_answer(user_answer, questions, answers)
    print ('')
print ('Congratulations, you have completed the ' + str(level) + ' level, with a score of ' + str(score) + ' out of ' + str(guesses) + ' guesses')