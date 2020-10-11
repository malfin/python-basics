# very BAD practice
concrete_request_1 = 'https://translate.google.com/?view=home&op=translate&sl=en&tl=ru&text=patronymic'
trash, raw_get_data = concrete_request_1.split('?', maxsplit=1)
get_data = raw_get_data.split('&')
parsed_get_data_as_dict = {}
for pair in get_data:
    tmp = pair.split('=')
    parsed_get_data_as_dict[tmp[0]] = tmp[1]
print(parsed_get_data_as_dict)

concrete_request_2 = 'https://translate.google.com/?view=home&op=translate&sl=ru&tl=en&text=отчество'
trash, raw_get_data = concrete_request_2.split('?', maxsplit=1)
get_data = raw_get_data.split('&')
parsed_get_data_as_dict = {}
for pair in get_data:
    tmp = pair.split('=')
    parsed_get_data_as_dict[tmp[0]] = tmp[1]
print(parsed_get_data_as_dict)
