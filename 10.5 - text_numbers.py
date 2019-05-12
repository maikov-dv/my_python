def num_in_text(in_file, out_file):
    try:
        with open(in_file, 'r') as input_file, open(out_file, 'w') as output_file:
            initial_text = input_file.readlines()
            updated_text = []
            num_order = 0
            for i in initial_text:
                new_list = list(i)
                new_list.insert(0, str(1+num_order) + ' ')
                i = ''.join(new_list)
                updated_text.append(i)
                num_order += 1
            output_file.writelines(updated_text)
        print('Данные успешно записаны!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    num_in_text('text.txt', 'update_text.txt')
