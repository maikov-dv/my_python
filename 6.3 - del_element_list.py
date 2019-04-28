names = ["John", "Paul", "George", "Ringo"]

names = list(filter((lambda item: len(item) == 4), names))

print(names)
