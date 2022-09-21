# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_user():
    return [x for x in sorted([x.split(';') for x in csv.split('\n')], key=lambda x: int(x[1])) if int(x[1]) > 10]

if __name__ == "__main__":
    print(get_user())
