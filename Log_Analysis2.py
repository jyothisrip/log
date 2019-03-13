#!/usr/bin/env python
import psycopg2
# first top three courses execution

databasename = "news"
username = 'vagrant'


def condatabase():
    try:
        j = psycopg2.connect(dbname=databasename, user=username)
        jhr = j.cursor()
        return jhr
    except Exception as error:
        print(error)
        print("It's difficult to connect news database")
        return


def Mighty_Prominent_Course():
    ''' Display output as most popular three articles of all time '''
    quern1 = ''' SELECT * FROM logudaanalysis_articles LIMIT 3; '''
    if (quern1):
        jhr.execute(quern1)
        gr = jhr.fetchall()
        try:
            if (gr):
                print('\n(1).Three mighty prominent course of all time')
                print('=============================================')
                for rlt in gr:
                    t = rlt[0]
                    v = rlt[1]
                    tup = (t, v)
                    if (tup):
                        print('"{tle}"===>{cot} views'.format(tle=t, cot=v))
                    else:
                        print("no result")
            else:
                print("not recognize")
        except Exception as error:
            print(error)
    else:
        print("error in code")


def Mighty_Prominent_Fabulators():
    ''' Display output as most popular article authors of all time '''
    quern2 = '''SELECT au.name, COUNT(ar.author) AS display
                FROM articles AS ar, log, authors AS au
                WHERE log.path = CONCAT('/article/',ar.slug)
                AND ar.author = au.id
                GROUP BY au.name ORDER BY display DESC;'''
    try:
        jhr.execute(quern2)
        gr = jhr.fetchall()
        try:
            if (gr):
                print('\n(2).mighty prominent fabulators of all time')
                print('=============================================')
                for rlt in gr:
                    t = rlt[0]
                    v = rlt[1]
                    tuple = (t, v)
                    if (tuple):
                        print('"{fabu}"==>{cot} views'.format(fabu=t, cot=v))
            else:
                print("error")
        except Exception as e:
            print(e)
    except Exception as error:
        print(error)
    return


def Billet_Absurdity_Anatomizing():
    ''' Display as days on which more than 1% of requests lead to errors '''
    quern3 = '''
    select Day,request_total,request_error,
    (request_error::float*100)/request_total::float
    as error_percent from
(select time::timestamp::date as Day,
count(status) as request_total,
sum(case when status = '404 NOT FOUND'
then 1 else 0 end) as request_error from log
group by time::timestamp::date) as
output
where (request_error::float*100)/
request_total::float > 1.0 order by
error_percent desc;
'''
    jhr.execute(quern3)
    gr = jhr.fetchall()
    try:
        if (gr):
            print("\n(3).Days on which more than 1% "
                  "of requests lead to errors ? ")
            print('====================================================')
            for i in range(0, len(gr), 1):
                print(str(gr[i][0]) + " - "+str(round(gr[i][3], 2))+"% errors")
            return
        else:
            print("error")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    jhr = condatabase()
    print("Log analysis project three requirements")
    Mighty_Prominent_Course()
    Mighty_Prominent_Fabulators()
    Billet_Absurdity_Anatomizing()
    jhr.close()
