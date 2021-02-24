a = {
    'a' : 5,
    'b' : 4,
    'c' : 3,
    'd' : 2,
    'e' : 1
}

letters = a.keys()

letters.sort(key=lambda x: a[x], reverse=True)
print(letters)