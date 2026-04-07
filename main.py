from wordfreq import top_n_list
import time
import random
import difflib 

words = top_n_list("en", 1000)

testlength = int(input("With how many words do you want to test yourself? (max. 1000): "))


if testlength > 1000:
    print("max. 1000, pls run the programm again.")
    exit()

testwords = random.choices(words, k=testlength)
testtext = " ".join(testwords)
print(testtext)

input("\nPress ENTER when ready...")

start = time.time()
answer = input("\nStart typing:\n")
end = time.time()

elapsed = end - start

wordcount = len(answer.split())
wpm = (wordcount / elapsed) * 60 if elapsed > 0 else 0

ratio = difflib.SequenceMatcher(None, testtext, answer).ratio()
accuracy = ratio * 100


print("\n--Results--")
print(f"WPM = {wpm}, Time = {elapsed}, Accuracy = {accuracy}")
