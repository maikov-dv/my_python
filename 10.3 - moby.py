# форматирование текста moby

with open('moby.txt', 'r') as file, open('moby_clean.txt', 'w') as outfile:
    for line in file:
        changed_line = line.lower()
        trantab = str.maketrans({'.': None, ',': None, ';': None, '-': None})
        changed_line = changed_line.translate(trantab)
        words = changed_line.split()
        changed_words = '\n'.join(words) + '\n'
        outfile.write(changed_words)
