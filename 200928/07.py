# f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
# context manager
from log_parse import row_parse, parser

parsed_data = row_parse('nginx_logs_head.txt')
save_parsed_data('nginx_logs_parsed.csv', parsed_data)
