from db.operation import DatabaseVisitor

db = DatabaseVisitor()

date_begin = "2021-01-08 19:13:32"
date_end = "2021-01-08 21:55:32"
sql = "SELECT * FROM SocietyHistory WHERE Sout between '{0}' and '{1}'".format(date_begin, date_end)
# sql = "SELECT * FROM SocietyHistory WHERE Sint between {0} and {1}".format(date_begin, date_end)
sql1 = "SELECT * FROM SocietyHistory"

re = db.find_all(sql)
if re:
    print(re)
else:
    pass

# print(re)
print("jjjajjj".strip('j'))

print("jhehej""jfieajfiaj1"','"fjaifji")
print([1]+[2])
