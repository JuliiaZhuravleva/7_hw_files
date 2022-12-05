def get_number_of_rows(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        length = len(file.readlines())
        return length


def sort_files(files_to_sort):
    unsorted_files = []
    for f in files_to_sort:
        number_of_rows = get_number_of_rows(f)
        unsorted_files.append({"file": f, "number_of_rows": int(number_of_rows)})
    sorted_files = sorted(unsorted_files, key=lambda d: d['number_of_rows'])
    return sorted_files


def file_transfer(file_to_transfer, target_file):
    with open(file_to_transfer, 'rt', encoding='utf-8') as ft:
        content = ft.read()
    with open(target_file, 'a', encoding='utf-8') as tf:
        tf.write(f'{file_to_transfer}\n{get_number_of_rows(file_to_transfer)}\n{content}\n')


files_list = ['1.txt', '2.txt', '3.txt']
files_list_sorted = sort_files(files_list)

for fls in files_list_sorted:
    file_transfer(fls['file'], 'result.txt')


