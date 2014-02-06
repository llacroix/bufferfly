


history = {
    'Birth': {
        "description": "Your mom gave birth",
        "die": {
            "description": "You kill yourself inside your mom to be"
         }
     }
}


def get_choices(current):
    choices = current.keys()
    for i in enumerate(current.keys()):
        print "%d: %s" % i 

    number = raw_input("Choose from [0-%d]: " % (len(choices) - 1))

    return number



print get_choices(history)
