
def new_game():
    Guesses=[]
    correct=0
    num=0
    for key in questions:
        print("----------------------")
        print(key)
        for i in options[num]:
            print(i)
        guess=input("Enter A,B,C OR D: ") 
        guess= guess.upper()
        Guesses.append(guess)
        correct+=check_answers(questions.get(key),guess)
        num=num+1
    display(correct, Guesses)
    play_again()
    
    
        
        
def display(correct, Guesses):
    print("Result \n")
    print("Answers")
    for i in questions:
        print(questions.get(i), end=" ")
    
    print("\nyour answers: ")
    for i in Guesses:
        print(i, end=" ")
    score= int(correct/len(questions)*100)
    print("\nyou score "+str(score)+"%\n")
        
        
def check_answers(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
        
def play_again():
    response= input("Do u want to play again? ")
    response=response.lower()
    
    if response == "yes":
        new_game()
    else:
        print("byeee")
    



questions={
    
  "which team has most UCL cups":"A",
  "where is FIFA headquatrer":"B",
  "which player has most golden ball":"A",
  "who is the most expensive player":"D",
  "which year the next world cup will take place":"C" 
  }

options=[["A. Real Madrid", "B. Barcelona", "C. AC Milan", "D. Liverpool"],
         ["A. France","B. Swiss", "C. Spain","D. Germany"],
         ["A. Messi","B. Ronaldo","C. Zidane", "D. Cristiano"],
         ["A. Mbappe", "B.Bellingham","C.De Bruyne", "D. Neymar"],
         ["A. Qatar", "B. Morocco", "C. USA", "D. china"]]

new_game()