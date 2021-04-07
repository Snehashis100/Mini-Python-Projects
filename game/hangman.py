def counter_func(word,letter):
    if letter not in word:
        return True
    else:
        return False

def printWord(lst):
    for i in lst:
        print(i,end=" ")

def showBlanks(lst):
    blank_lst = []
    for i in lst:
        if i != " ":
            blank_lst.append("_")
        else:
            blank_lst.append(" ")
    return blank_lst

def userGuess(guess_letter, actual_lst, blank_lst):
    updated_lst = []
    for i in range(len(actual_lst)):
        if blank_lst[i]=="_":
            if actual_lst[i] == guess_letter:
                updated_lst.append(guess_letter)
            else:
                if actual_lst[i] == " ":
                    updated_lst.append(" ")
                else:
                    updated_lst.append("_")
        elif blank_lst[i]==" ":
            updated_lst.append(blank_lst[i])
        else:
            updated_lst.append(blank_lst[i])
    return updated_lst

if __name__ == '__main__':
    result = list(input("Enter the word/words------>>>"))
    show = showBlanks(result)
    tried_letter_lst=[]
    for i in show:
        print(i, end=" ")
    i=6
    while(i!=0):
        inp = input("Enter the letter----->>>")
        tried_letter_lst.append(inp)
        if counter_func(result,inp)==True:
            i -=1
            print(f"You have {i} chances left")
            res = userGuess(inp, result, show)
            show=list(res)
            printWord(res)
            print(f"Tried letters: {set(tried_letter_lst)}")
        else:
            res = userGuess(inp, result, show)
            show = res
            if show==result and i!=0:
                print("You have matched!!!!")
                printWord(show)
                break
            else:
                printWord(show)
                print(f"Tried letters: {set(tried_letter_lst)}")
