with open('moby_clean.txt', 'r') as file:
    words = file.readlines()
    word_list = []
    for word in words:
        new_word = word.strip()
        word_list.append(new_word)
    def histogram(word_list):
        word_count = {}
        for item in word_list:
            word_count.setdefault(item, 0)
            word_count[item] += 1      
        return word_count
    import operator
    sorted_words = sorted(histogram(word_list).items(), key=operator.itemgetter(1))
    print('Первые 5 слов c наибольшей частотой:', sorted_words[len(sorted_words)-1], sorted_words[len(sorted_words)-2], sorted_words[len(sorted_words)-3], sorted_words[len(sorted_words)-4], sorted_words[len(sorted_words)-5])
    print('Первые 5 слов c наименьшей частотой:', sorted_words[0], sorted_words[1], sorted_words[2], sorted_words[3], sorted_words[4])
