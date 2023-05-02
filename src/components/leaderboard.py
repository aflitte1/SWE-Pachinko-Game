from datetime import date
import os

scores = [[], [], [], []]
last_score = [[], [], [], []]
FileName = "leaderboard_file.txt"


def getscore(game_score, username):
    temp_score = []
    # This will need to be done with pygame, it will make it more complicated
    today = date.today()
    reformated = today.strftime("%m/%d/%y")
    temp_score.append(username)
    temp_score.append(game_score)
    temp_score.append(reformated)
    # Returns an list with players username, score, and date they got the score formated as a string
    return temp_score


def putscore(userscore, level):
    # checks to see if it is the first score
    if len(scores[level-1]) == 0:
        scores[level-1].append(userscore)

        # if it is not the first score, we need to find where it goes
    else:
        # the number of scores currently in,
        temp_higher = len(scores[level-1])
        # I iterate backwards, but I don't think you need to
        for ii in range(len(scores[level-1]), 0, -1):
            # if the score we just got is higher than the past score, we place it lower in the list by 1
            if int(userscore[1]) >= int(scores[level-1][ii - 1][1]):
                temp_higher -= 1
        # we need to add it to the list
        if temp_higher != 10:
            scores[level-1].insert(temp_higher, userscore)
        # if we have more than 10 scores delete the lowest one
        if len(scores[level-1]) == 11:
            del scores[level-1][10]
    last_score[level-1] = userscore


def write_to_file(scores):
    file1 = open(FileName, "w")
    for kk in range(0, 4):
        for jj in range(0, len(scores[kk])):
            # for each level(kk), for each score(jj), break into 3 parts with delimiter $
            file1.writelines(
                scores[kk][jj][0] + "$" + scores[kk][jj][1] + "$" + scores[kk][jj][2] + "\n")
        # After writing lines, put delimiter so we know when the scores for that level stop
        file1.writelines("next_level_scores\n")
    file1.close()


def read_to_file():
    # checks to see if the file exists
    if os.path.isfile(FileName):
        # checks to see if the file is empty(This is redundent, but just in case)
        if os.path.getsize(FileName) > 1:
            file1 = open(FileName, "r")
            # For each level
            for kk in range(0, 4):
                # read in one line at a time until you get to breaker
                temp_score = file1.readline()
                temp_score = temp_score[:-1]
                while (temp_score != "next_level_scores"):
                    # split on $ so we get an array with [username, score, date] and append it
                    score_array = temp_score.split('$')
                    scores[kk].append(score_array)
                    temp_score = file1.readline()
                    temp_score = temp_score[:-1]
            file1.close()


# Note Level should be 1,2,3,4
def update_leaderboard(level, game_score, username):
    # Only want to read in the file the first time you update
    userscore = getscore(game_score, username)
    putscore(userscore, level)
    write_to_file(scores)


def format_leaderboard_display(user_score, ii):
    match len(user_score[0]):
        case 0:
            name = "    "
        case 1:
            name = user_score[0] + "   "
        case 2:
            name = user_score[0] + "  "
        case 3:
            name = user_score[0] + " "
        case 4:
            name = user_score[0]
    if len(user_score[1]) == 1:
        score = " " + user_score[1]
    else:
        score = user_score[1]
    date = user_score[2]
    if ii == -1:
        count = ""
    elif ii+1 == 10:
        count = str(ii+1) + " "
    else:
        count = str(ii+1) + "  "
    display_string = count + name + "  " + score + "  " + date
    return display_string
