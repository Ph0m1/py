
def count_words(str):
    words = str.split()
    return len(words)

str=input()
count = count_words(str)
print("count =",count)