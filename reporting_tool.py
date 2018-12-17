#!/usr/bin/env python
import psycopg2
DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
# 'Question_1'
print
print("""\033[1;35m1.What are the most popular three articles of all time?
\033[1;m""")
c.execute("""SELECT title , count(*) AS views FROM author_title_path GROUP BY
title ORDER BY views DESC LIMIT 3;""")
result = c.fetchall()
for row in result:
        print '\033[1;34m- \"%s\" - %s views\033[1;m' % (row[0], row[1])
# 'Question_2'
print
print("""\033[1;35m2.Who are the most popular article authors of all time?
\033[1;m""")
c.execute("""SELECT name , count(*) AS views FROM author_title_path GROUP BY
name ORDER BY views DESC;""")
result = c.fetchall()
for row in result:
        print '\033[1;34m- %s - %s views\033[1;m' % (row[0], row[1])
# 'Question_3'
print
print("""\033[1;35m3.On which days did more than 1% of requests lead to errors?
\033[1;m""")
c.execute("""SELECT TO_CHAR( date ,'Mon dd, yyyy') AS Date ,  percentage FROM
percentage_of_daily_errors WHERE percentage>1;""")
result = c.fetchall()
for row in result:
        print '\033[1;34m- %s - %s%% errors\033[1;m' % (row[0], row[1])
print
print('NOTE: You can find the output of this tool coped in a plain text file \
at the project directory, called: \"output\"')
print
db.close()
