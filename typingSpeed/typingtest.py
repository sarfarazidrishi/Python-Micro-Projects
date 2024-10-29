import time
import random as r


paragraphs = [
    """"When possibilities arise, every decimal matters. One calculator shows 0.0099, 
        acknowledging even the smallest chance, while another rounds down to zero, dismissing it. 
        In a world full of hidden potentials, even the slightest possibility can lead to great outcomes.""",

    """Some occurrences may seem too small to be important, yet that tiny probability might hold the 
        key to a significant outcome. One calculator accounts for this with 0.0099, grasping even the 
        slightest chance. The other disregards it. Life rewards those who notice even invisible opportunities.""",

    """Life is filled with subtle chances that often slip by unnoticed. One calculator registers 
        the faintest possibility with 0.0099, seizing every opening. The other rounds to zero, discarding
        it entirely. Sometimes, all it takes is one small chance to spark something remarkable.""",

    """If we dismiss the smallest opportunities, we risk losing what might have been extraordinary.
        One calculator captures this by showing 0.0099, valuing every potential. The other rounds it away 
        to zero. Let every fraction of a chance count; sometimes, that’s all it takes to make a difference.""",

    """Precision makes an impact in math and in life. The difference between 0.0099 and 0 may 
        seem trivial, but it carries weight. One captures every chance, however slight, while the other
        ignores it. Success often lies in what others fail to observe; pay attention to every decimal."""
]
testing_para=r.choice(paragraphs)

typing_start_time=time.time()
user_input=input(f"Type the paragraph: {testing_para} \n ")
typing_end_time=time.time()

def word_count(testing_para, userInput):
    testing_words=testing_para.split()
    user_input_words=userInput.split()
    
    total_words_typed=0
    correct_words_count=0
    wrong_words=[]
    wrong_words_typed_by_user=[]
    
    for i in range(len(user_input_words)):
        if i>= len(testing_words):
            break
        if testing_words[i]==user_input_words[i]:
            correct_words_count=correct_words_count+1
        else:
            wrong_words.append(testing_words[i])
            wrong_words_typed_by_user.append(user_input_words[i])
        
    total_words_typed=len(user_input_words) 
    print(f"total correct words: {correct_words_count}")
    for index, (correct, wrong) in enumerate(zip(wrong_words, wrong_words_typed_by_user), start=1):
        print(f"{index:<3} Expected: {correct:<20} | you typed: {wrong:}")

    return correct_words_count, wrong_words, total_words_typed, wrong_words_typed_by_user


correct_words_count, wrong_words, total_words_typed, wrong_words_typed_by_user=word_count(testing_para, user_input)
time_taken = typing_end_time-typing_start_time

def speed_calculator(timeUsed, total_words_typed, correctWordCount):
    speed_wpm= total_words_typed/timeUsed*60
    accuracy=(correctWordCount/total_words_typed)*100
    print(f"speed: {(speed_wpm):.2f}WPM")
    print(f"accuracy: {accuracy:.2f}%")
    

# word_count(testing_para, user_input)
speed_calculator(time_taken, total_words_typed,correct_words_count )
    