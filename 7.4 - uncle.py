s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

lst = s.split()

for item in lst:
    if item.startswith("м"):
        lst.remove(item)

s = " ".join(lst)
print(s)
