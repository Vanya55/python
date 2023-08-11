#!/usr/bin/python3

import random
import os.path


def get_random_5_questions(questions):
    tmp = []
    while len(tmp) < 5:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in tmp:
            tmp.append(questions[num])
    return tmp


def structure_questions(tmp):
    gquestions = {}

    for el in tmp:
        q, a = el.split("?")
        gquestions[q] = a.split(",")
    return gquestions


def fiv(an,correct):
    list=an
    list.remove(correct)
    newList= [random.choice(list),correct]
    random.shuffle(newList)
    return  newList


def users(an):
    for el in an:
       print(el + " " +str(random.randint(1, 100)) + "%")


def proverka(correct):
    answer = input("Enter your answer: ").title()
    if answer == correct:
        print("Correct")
        return 1
    else:
        print("Incorrect. The correct answer was", correct)
        return 0


def game(gquestions):
    cnt = 0
    helps=['50/50','Call','Audience']
    for q, a in gquestions.items():
        print(q)
        correct = a[0]
        random.shuffle(a)
        for el in a:
            print(el)
        print("You have the opportunity to use the help :",", ".join(helps))
        answer = input("Enter your answer: ").title()
        if answer == "50/50" and '50/50' in helps:
           res2 = fiv(a,correct)
           for el in res2:
               print(el)
           helps.remove('50/50')
           cnt+=proverka(correct)
        elif answer == "Call" and 'Call' in helps:
            print("Correct answer is ,",correct)
            helps.remove('Call')
            cnt+=proverka(correct)
        elif answer == "Audience" and 'Audience' in helps:
             users(a)
             helps.remove('Audience')
             cnt+=proverka(correct)
        elif answer == correct:
            print("Correct")
            cnt += 1
        else:
            print("Incorrect. The correct answer was", correct)
    print("You got %d/5" % cnt)
    return cnt


def get_questions_from_file(fname):
    with open(fname) as f:
        return f.readlines()


def sanitize_data(ml):
    return [el.strip() for el in ml]


def check_file_existence(fname):
    if not os.path.isfile(fname):
        print("Your files does not exists: %s. Please check" % fname)
        return False
    return True


def get_top_players_from_file(fname):
    with open(fname) as f:
        return f.readlines()


def create_file(fname):
    f = open(fname, "w")
    f.close()


def create_players_dict(data):
    # should be written "username: XP"
    md = {}
    for el in data:
        p, x = el.split(": ")
        md[p] = int(x)
    return md


def confirm_username(username, players):
    if username in players:
        ans = input("Would you like to rewrite your XP? ")
        if ans.lower() == "y":
            pass
        else:
            username = input("Enter your username: ")
            while username in players:
                username = input("Enter your username: ")
    return username


def sort_players_by_xp(players):
    ml = list(players.items())
    ml.sort(key=lambda x: x[1], reverse=True)
    return ml


def write_player_xp(fname, ml):
    with open(fname, "w") as f:
        for pl, xp in ml:
            f.write(pl + ": " + str(xp) + "\n")


def main():
    username = input("Enter your username: ")
    question_file = "questions.txt"
    fl = check_file_existence(question_file)
    if not fl:
        exit()
    top_file = "top_players.txt"
    fl = check_file_existence(top_file)
    if not fl:
        create_file(top_file)
    players_data = get_top_players_from_file(top_file)
    players = sanitize_data(players_data)
    players_dict = create_players_dict(players)
    username = confirm_username(username, players_dict)
    questions = get_questions_from_file(question_file)
    questions = sanitize_data(questions)
    random5 = get_random_5_questions(questions)
    game_questions = structure_questions(random5)
    xp = game(game_questions, )
    players_dict[username] = xp
    players = sort_players_by_xp(players_dict)
    write_player_xp(top_file, players)


main()


