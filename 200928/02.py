f = open('nginx_logs_head.txt', 'r', encoding='utf-8')

file_data = f.readlines()
# print(file_data)
for row in file_data:
    print(row.strip())
