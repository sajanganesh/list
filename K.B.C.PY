print( "WELLCOME TO K.B.C.")
question_list=["1)How many continents are there?",            
                "2)What is the capital of India?",            
                "3)NG mei kaun se course padhaya jaata hai?"]
options_list=[["1)Four", "2)Nine", "3)Seven", "4)Eight"],
               ["1)Chandigarh", "2)Bhopal", "3)Chennai", "4)delhi"],
               ["1)Software Engineering", "2)Counseling", "3)Tourism", "4)Agriculture"]]

answer_list=[3,4,1]

answer_5050=[["1)Four","3)Seven"],["2)Bhopal","4)delhi"],["1)Software Engineering","4)Agriculture"]]


i=0
count=0
while i<len(question_list):
    j=0
    while j<len(question_list[0]):
        print(question_list[0])
        break    
    print(options_list[0])
    num=input("do you want 5050 lifeline")
    if num=="yes" :
        print("accept")
        if count<1:
            print(answer_5050[0])
            num1=int(input("enter the number"))
            if num1==1:
                print("it is wrong answer,write answer is seven.you are out of this game")
                break
            elif num1==3:
                print("it is write answer")
                count=+1
                break
    
            else :
                print("you already used 5050 lifeline")       
                number=int(input("enter the number:"))
                if number==1 or number==2 or number==4:
                    print("it is wrong answer.write answer is seven.you are out of this game")
                    break
                elif number==3:
                    print("seven it is write answer")              
                else:
                    print("it is invalid number")
                    break
             
              
                    
            i=0
            while i<len(question_list):
                j=0
                while j<len(question_list[1]):
                    print(question_list[1])
                    break
                print(options_list[1])
                num=input("do you want 5050 lifeline")
                if num=="yes" :
                    print("accept")
                    if count<1:
                        print(answer_5050[1])
                        num1=int(input("enter the number"))
                        if num1==2:
                            print("it is wrong answer,write answer is seven.you are out of this game")
                            break
                        elif num1==4:
                            print("it is write answer")
                            count+=1
                            break
                        elif num=="yes":
                            print("you already used 5050 lifeline")       
                            number=int(input("enter the number:"))
                            if number==1 or number==2 or number==3:
                                print("it is wrong answer.write answer is delhi.you are out of this game")
                                break
                            elif number==4:
                                print("delhi it is write answer")              
                            else:
                                print("it is invalid number")
                    i=i+1
                    break 
        i=i+1
        break                   
    else :
        print("not accept")
        number=int(input("enter the number:"))
        if number==1 or number==2 or number==4:
            print("it is wrong answer.write answer is seven.you are out of this game")
            break
        elif number==3:
            print("seven it is write answer")              
        else:
            print("it is invalid number")
            break
    
        i=0
        while i<len(question_list):
            j=0
            while j<len(question_list[1]):
                print(question_list[1])
                break
            print(options_list[1])
            num=input("do you want 5050 lifeline")
            if num=="yes" :
                print("accept")
                if count<1:
                    print(answer_5050[1])
                    num1=int(input("enter the number"))
                    if num1==2:
                        print("it is wrong answer,write answer is seven.you are out of this game")
                    else:
                        print("it is write answer")
                    count+=1
                else :
                    print("you already used 5050 lifeline")       
                    number=int(input("enter the number:"))
                    if number==1 or number==2 or number==3:
                        print("it is wrong answer.write answer is delhi.you are out of this game")
                        break
                    elif number==4:
                        print("delhi it is write answer")              
                    else:
                        print("it is invalid number")
                i=i+1
                break
        i=i+1
        break    
                