from random import choice as choose, seed
from datetime import datetime

class GameEnded(BaseException):
    pass

class State(object):
    def __init__(self, description, predicate, new_items, use_items):
        self.description = description
        self.children = {}
        self.predicate = predicate
        self.new_items = new_items
        self.use_items = use_items

    def add(self, name, states):
        self.children[name] = states

    def next(self):
        if len(self.children.keys()) == 0:
            raise GameEnded()
        else:
            names = self.children.keys()

            choice = -2

            while choice < 0 or choice > len(names)-1:
                for i in enumerate(names):
                    print "%d: %s" % i 

                try:
                    choice = int(raw_input("Choose from [0-%d] > " % (len(names) - 1)))
                except:
                    pass

            chosen_name = names[choice]

            possible_choices = filter(lambda x: x.predicate(), self.children[chosen_name])


            next_state = choose(possible_choices)
            history.append(next_state)

            print next_state.description

            if len(next_state.children.keys()) == 0:
                next_state.next()

            return next_state

    def select(self):
        global items

        new_items = items[-1][:]

        for i in self.use_items:
            try:
                new_items.remove(i)
            except:
                pass

        for i in self.new_items:
            new_items.append(i)

Birth = State("You are born", lambda: True, [], [])
BirthDeath = State("You decided to kill yourself", lambda: True, [], [])

FirstDayInSchool = State("You draw something nice", lambda: True, [], [])
FirstDayInSchool2 = State("You draw some kind of crazy shit, turns out you became a junky and got lots of condoms on you now", lambda: True, ["condoms", "pills"], [])

PsychHospital = State("People think you're mad, it probably has something to do with the pills you take.", lambda: "pills" in items, [], ["condoms", "book"])
PsychDeath = State("You die alone from madness in an hospital", lambda: True, [], [])

FirstSexGood = State("You got laid and that was the best day of your life", lambda: "condoms" in items, [], [])
FirstSexBad = State("You got laid but realized you got AID", lambda: "condoms" not in items, ["aid"], [])
FirstSexBad2 = State("You got laid but you got your first kid", lambda: "condoms" not in items, ["wife", "baby"], [])

Sick = State("You're pretty sick and die alone", lambda: True, [], [])

FirstJob = State("You got your first job and everything is fine", lambda: True, ["money", "condoms"], [])
FirstJob1 = State("You got your first job and everything is fine", lambda: True, [], ["money"])
FirstJob2 = State("You work like mad but nothing works", lambda: True, ["pills"], [])

Space = State("Everything was going so well but you end up in space... suffocating... you don't remember anything you just die", lambda: True, [], [])


Birth.add("First day in school", [FirstDayInSchool, FirstDayInSchool2])
Birth.add("Death", [BirthDeath])

FirstDayInSchool2.add("First sex", [PsychHospital, FirstSexGood, FirstSexBad2, FirstSexBad])
FirstDayInSchool.add("First sex", [PsychHospital, FirstSexGood, FirstSexBad2, FirstSexBad])

PsychHospital.add("Death", [PsychDeath])

FirstSexGood.add("First job", [FirstJob, FirstJob1])

FirstSexBad.add("Sick", [Sick])

FirstJob.add("Everything was going so well", [Space])

current_state = None


history = [Birth, FirstDayInSchool, FirstSexGood, FirstJob]
items = [[], [], []]


def show_items():
    if len(items) > 0:
        print "The item you have"
        for item in items:
            print item
    else:
        print "you have no items"

def forward():
    current = history[-1]
    current.next()

def backtrack():
    global history
    choice = -1

    while choice < 0 or choice > len(history)-1:
        for i, state in enumerate(history):
            print "%d: %s" % (i, state.description) 

        try:
            choice = int(raw_input("choose from [0:%d] > " % (len(history) - 1)))
        except:
            pass

    history = history[:choice+1]

def show_history():
    print " -> ".join(map(lambda x: x.description, history))

def main_loop():

    while True:
        try:
            command = raw_input("> ")

            if command == "history":
                show_history()
            elif command == "items":
                show_items()
            elif command == "back":
                backtrack()
            elif command == "next":
                forward()
            else:
                print "history, items, backtrack, forward"
        except GameEnded:
            break

seed(datetime.now())
main_loop()
