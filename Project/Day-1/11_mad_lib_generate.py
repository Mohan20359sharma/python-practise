def mad_lib():
    noun = input("Enter a noun. ")
    verb = input("Enter a verb. ")
    adjective = input("Enter a adjective. ")
    place = input("Enter a place. ")

    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}"
    print(story)

mad_lib()