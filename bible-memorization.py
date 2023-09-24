import os

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    memoFile = open("./THOR.txt","r")
    clearScreen()
    print("bible-memorization")
    print("-------------------------")
    print("Type \"memorize\" to go to memorize mode")
    print("Type \"recite\" to go to recite mode")
    print("Type \"quit\" at any input to quit the program")
    userInput = input()
    switch(userInput, memoFile)
    
def switch(userInput, memoFile):
    if(userInput == "memorize"):
        memorize(memoFile)
    elif(userInput == "recite"):
        recite(memoFile)
    elif(userInput == "quit"):
        exit()
    else:
        print("Incorrect input! Use \"memorize\", \"recite\", or \"quit\"", end="\r")
        newUI = input()
        switch(userInput)

def restartRecite():
    memoFile = open("./THOR.txt","r")
    switch("recite", memoFile)

def recite(memoFile):
    verses = memoFile.readlines()
    clearScreen()
    print("==RECITE==")
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
                restartRecite()
            else:
                menu()
        else:
            print("correct")
        #print(line1)

def memorize(memoFile):
    verseDictionary = {}
    verseList = []
    verses = memoFile.readlines()
    for line1 in verses:
        x = line1.split("||")
        reference = x[0]
        #print(reference)
        verseText = x[1].split("\n")[0]
        verseList.append(reference)
        verseDictionary[reference] = verseText
    cont = True
    clearScreen()
    print("==Memorize==")
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
            correct = False
            while cont:
                clearScreen()
                if(correct):
                    print("correct")
                correct = False
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
                    correct = True
        else:
            print("Invalid Verse Choice.")
            
menu()