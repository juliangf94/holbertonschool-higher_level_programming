>>> to_json_string = __import__('3-to_json_string').to_json_string

>>> to_json_string([1, 2, 3])
'[1, 2, 3]'
>>> to_json_string({"id": 12})
'{"id": 12}'
>>> type(to_json_string([1]))
<class 'str'>
