from datetime import date

scores = [[],[],[],[]]
level = 1

def getscore():
    temp_score = []
    username = input("New Highscore, what is you user name?(three character cap)\n")
    while(len(username) > 3 or len(username) == 0):
        print("Error with user input, try again")
        username = input("New Highscore, what is you user name?(three character cap)\n")
    #get the users score here, for now manuel input
    score = input("get game score\n")
    today = date.today()
    reformated = today.strftime("%m/%d/%y")
    temp_score.append(username)
    temp_score.append(score)
    temp_score.append(reformated)
    print(temp_score)
    return temp_score

def putscore(userscore):
    if len(scores[level-1]) == 0:
        print("New highscore! WOW")
        scores[level-1].append(userscore)
    else:
        temp_higher = len(scores[level-1])
        print(temp_higher, "before for loop")
        for ii in range(len(scores[level-1]), 0, -1):
            print(userscore[1], "userscore 1")
            print(scores[level-1][ii - 1][1], "scores[ii]")#error here needs to be debugged
            if int(userscore[1]) >= int(scores[level-1][ii - 1][1]):
                temp_higher -= 1
        if temp_higher != 9:
            print(temp_higher)
            scores.insert(temp_higher, userscore)
        if len(scores[level-1]) == 11:
            del scores[10]




while True:
    userscore = getscore()
    putscore(userscore)
    print(scores)
    