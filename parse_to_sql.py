import json
import codecs
import datetime
from pprint import pprint

with open('institution.json') as data:
	sql = file('institution.sql', 'w');
	identifier = 0
	while True:

		line = data.readline()
		if len(line) == 0:
			break
		INSERT_TEMPLATE = 'INSERT INTO institution(`id`'
		identifier += 1

		# if identifier == 900:
		# 	break

		line = json.loads(line, "utf-8")
		values = []
		for key in line.keys():
			value = line[key]
			if type(value) is list:
				value = ','.join(value)
			if key in ['avatar']:
				value = value[(value.rfind('/') + 1):]
			if key not in ['url', 'images']:
				values.append(value)
				INSERT_TEMPLATE += ', `' + key + '`'
		INSERT_TEMPLATE += ') values(' + `identifier`

		for value in values:
			INSERT_TEMPLATE += ", '" + value.strip() + "'"
		INSERT_TEMPLATE += ');\n'
		sql.write(INSERT_TEMPLATE.encode('utf-8'))
	sql.close()
	data.close()