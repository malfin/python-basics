# f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
# context manager

# __enter__
# __exit__ -> f.close()
# transaction.atomic() -> restore point
with open('nginx_logs_head.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        print(row)
# print(f.closed)
