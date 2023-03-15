# Madlibs using string concatenation
# youtuber = "Travel the World"

# a few ways to do this
# print("Subscribe to "+ youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

# Answers should be,
# verb1= cleaning
# age = six
# verb2 = Thinking
# verb3 = keep
# verb4 = share

verb1= input("Verb: ")
age= input("Age: ")
verb2= input("Verb: ")
verb3= input("Verb: ")
verb4= input("Verb: ")

madlib = f"I was {verb1} out the pockets of my {age} year old's winter coat, when I found a pair of mittens in each pocket.\
{verb2} that one pair must not be enough to {verb3} her hands warm,I asked her why she was carrying {age} pairs of mittens in her coat.\
She replied,'I've been doing that for long time, Mom. You see, some kids come to school without mittens and if I carry another pair, \
I can {verb4} with them and then their hands won't get cold.'"

print("          ")
print("Cold Hands")
print("==========")
print("          ")
print(madlib)
