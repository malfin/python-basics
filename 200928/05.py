# f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
# context manager

# __enter__
# __exit__ -> f.close()
# transaction.atomic() -> restore point
# settings
src_data_file = 'nginx_logs_head.txt'
parsed_data_file = 'nginx_logs_parsed.csv'

# init
parsed_data = []

# parse
with open(src_data_file, 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        # row parse
        remote_IP_address, row_tail = row.split(maxsplit=1)
        _, _request_datetime = row_tail.split('[', maxsplit=1)
        request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)

        _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
        request_method, requested_resource, _ = _request_method.split(maxsplit=2)
        # prepare result
        parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
        parsed_row = list(map(str.strip, parsed_row))
        #append result
        parsed_data.append(parsed_row)
        # print(parsed_row)
# print(f.closed)
# save
with open(parsed_data_file, 'w', encoding='utf-8') as f:
    for row in parsed_data:
        f.write(f"{', '.join(row)}\n")  # .txt _> .csv
