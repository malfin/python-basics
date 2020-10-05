from statistics import mean

with open("student_log's.txt", 'r', encoding='utf-8') as f:
    for list in f.read().splitlines():
        l = len(list)
        s_list = []
        i = 0
        while i < l:
            s_int = ''
            a = list[i]
            if '0' < a <= '5':
                s_int += a
                i += 1
                if i < l:
                    a = list[i]
                else:
                    break
            i += 1
            if s_int != '':
                s_list.append(int(s_int))
        print(list.split()[0], list.split()[1], list.split()[2].replace(",", ":"), s_list)
        print('Средний балл:', mean(s_list))
