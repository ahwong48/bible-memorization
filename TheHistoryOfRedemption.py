def menu():
    thorFile = open("./THOR.txt","r")    
    print("-------------------------")
    print("Type \"memorize\" to go to memorize mode")
    print("Type \"recite\" to go to recite mode")
    print("Type \"quit\" at any input to quit the program")
    userInput = input()
    switch(userInput, thorFile)
    
def switch(userInput, thorFile):
    if(userInput == "memorize"):
        memorize(thorFile)
    elif(userInput == "recite"):
        recite(thorFile)
    elif(userInput == "quit"):
        exit()
    else:
        print("Incorrect input! Use \"memorize\", \"recite\", or \"quit\"")
        newUI = input()
        switch(userInput)

def restartRecite():
    thorFile = open("./THOR.txt","r")
    switch("recite", thorFile)

def recite(thorFile):
    verses = thorFile.readlines()
    for line1 in verses:
        x = line1.split("||")
        reference = x[0]
        print(reference)
        verseText = x[1].split("\n")[0]
        userInput = input()
        if(userInput == "quit"):
            exit()
        elif(userInput!=verseText):
            print("incorrect")
            print("Correct: " + verseText)
            print("Input:   " + userInput)
            print("Would you like to try again? (Y|N)")
            userInput = input()
            if(userInput=="Y" or userInput=="y"):
                print("Good Luck, starting from the beginning")
                restartRecite()
            else:
                menu()
        else:
            print("correct")
        #print(line1)

def memorize(thorFile):
    verseDictionary = {}
    verseList = []
    verses = thorFile.readlines()
    for line1 in verses:
        x = line1.split("||")
        reference = x[0]
        #print(reference)
        verseText = x[1].split("\n")[0]
        verseList.append(reference)
        verseDictionary[reference] = verseText
    cont = True
    while cont:
        print("===========================")
        print("Type \"quit\" at any input to quit the program")
        print("Choose Verse:")
        print(verseList)
        verseChoice = input()
        if(verseChoice == "quit"):
            cont = False
            exit()
        elif(verseList.count(verseChoice) != 0):
            while cont:
                print(verseChoice)
                userInput = input()
                if(userInput == "quit"):
                    exit()
                elif(userInput!=verseDictionary[verseChoice]):
                    print("incorrect")
                    print("Correct: " + verseDictionary[verseChoice])
                    print("Input:   " + userInput)
                    print("Would you like to try again? (Y|N)")
                    userInput = input()
                    if(userInput=="Y" or userInput=="y"):
                        print("Good Luck")
                    elif(userInput=="quit"):
                        exit()
                    else:
                        cont = False
                        menu()
                else:
                    print("correct")
        else:
            print("Invalid Verse Choice.")
            
print("The History Of Redemption")
menu()