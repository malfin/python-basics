f = open('nginx_logs_head.txt', 'r', encoding='utf-8')

# file_data =
# print(file_data)
for row in f.read().splitlines():
    remote_IP_address, row_tail = row.split(maxsplit=1)
    _, _request_datetime = row_tail.split('[', maxsplit=1)
    request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)

    _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
    request_method, requested_resource, _ = _request_method.split(maxsplit=2)

    parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
    parsed_row = list(map(str.strip, parsed_row))
    print(parsed_row)
f.close()
