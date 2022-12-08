#this program grades a drivers licence exam

def main():
    #store the answer key as a list
    answer_key = correct_answers()
    
    #get the students answers and store in a list
    student_answers = get_student_answers()

    #compare students answers to answer key, 
    #wrong answers is a list
    wrong_answers = compare_list(answer_key, student_answers)

    #see how many answers student got wrong,
    #function recieves the number of wrong answers 
    num_wrong = amnt_ans_wrong(wrong_answers)

    #display pass or fail message
    pass_fail_msg(num_wrong)

    #display the students wrong answers
    if num_wrong != 0:
        display_wrong_answers(wrong_answers)
        

def correct_answers():
    #create list of correct answers
    answer_key = ['A','C','A','A','D','B',
                  'C','A','C','B','A','D','C','A','D','C','B','B','D','A']

    #returnt the answer key to main function
    return answer_key

def get_student_answers():
    #create a list for the students answers
    student_answers = []

    #instruct student to enter answers
    print('Please enter all answers in capital')

    #get the students answers, 20 times
    for index in range(20):
        print('Enter answer ', index + 1, ': ', sep='', end='')
        answer = input()

        #validate input
        while answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
            answer = input('You entered an invalid answer, please reenter '
                           'your answer: ')
            
        #add the students answer to the answer list
        student_answers.append(answer)

    #return the list to the main function
    return student_answers

def compare_list(answer_key, student_answers):

    #create a list for incorrect answers
    incorrect_answers = []

    #compare answers from both list to see if students answer are correct
    for i in range(len(answer_key)):

        #for any answer that is not the same,
        #add the question number to incorrect list
        if student_answers[i] != answer_key[i]:
            wrong_ans = i+1
            incorrect_answers.append(wrong_ans)

    #return the list of wrong ansers to main function        
    return incorrect_answers

def amnt_ans_wrong(wrong_answer):
    num_wrong_answer = len(wrong_answer)
    return num_wrong_answer

def pass_fail_msg(num_wrong):

    #calculate the number of questions answered correctly
    num_right = 20 - num_wrong

    #Diplay pass/fail message, based on how many answered correctly
    if num_right >= 15:  #passed
        print()
        print('Congragulations, You passed!!!')
        print('Correct answers: ', num_right, '\nIncorrect answers: ', num_wrong)
    else:                #failed
        print()
        print('Uh oh, you failed...')
        print('Correct answers: ', num_right, '\nIncorrect answers: ', num_wrong)
        print('You need to answer at least 15 questions correctly in order to pass.')
        
def display_wrong_answers(wrong_answers):

    #numbering for the wrongly answered questions
    size_list = 1

    #display message for incorrectly answered questions
    print()
    print('Listed below are the questions you answered incorrectly:')

    #display incorrect answers
    for i in wrong_answers:
        print(size_list, '. Question number ', i, sep='')

        #add one to size list, so it's correct numbering
        size_list+=1
    
    
    
    



main()
