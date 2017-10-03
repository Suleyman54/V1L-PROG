scorebehaald = int(input("Wat is je score voor multiplechoice? "))
text1 = "met een score van " + str(scorebehaald) + " ben je geslaagd"
text2 = "met een score van " + str(scorebehaald) + " ben je gezakt"
if scorebehaald >= 15:
    print(text1)

else:
    print(text2)