#!/usr/bin/env python3

import psycopg2


# Connecting to the database
def connect(dbname):
    try:
        conn = psycopg2.connect('dbname= %s' % dbname)
        c = conn.cursor()
        return (conn, c)
    except BaseException:
        return None


# This function executes the sql query
def query_executer(sql_query):

    cur = connect("news")

    cur[1].execute(sql_query)

    results = cur[1].fetchall()

    cur[0].close()

    return results


# This function returns most popular 3 articles
def popular_articles():

    query = (
        "select articles.title, count(*) as num_of_views from articles, log"
        " where log.path = concat('/article/', articles.slug)"
        " and log.status = '200 OK' group by articles.title"
        " order by num_of_views desc limit 3")

    results = query_executer(query)

    print("Most Popular Three Articles\n")

    for result in results:
        print(result[0] + " - views " + str(result[1]))


# This function returns most popular 3 authors
def popular_authors():

    query = (
        "select authors.name, count(*) as num_of_views from articles,"
        " authors, log where log.path = concat('/article/', articles.slug)"
        " and articles.author = authors.id group by authors.name"
        " order by num_of_views desc")

    results = query_executer(query)

    print("\nMost Popluar Three Articles Authors\n")

    for result in results:
        print(result[0] + ' - views ' + str(result[1]))


# function returns date with more than 1% request error
def days_with_lotsoferrors():

    query = ("SELECT to_char(status_error.dates, 'dd-mm-yyyy'),"
             " round((status_error.e*1.0 / requests_sum.r*1.0)*100, 2)"
             " as per FROM status_error, requests_sum WHERE"
             " status_error.dates = requests_sum.dates and"
             " (status_error.e*1.0 / requests_sum.r*1.0)*100 > 1"
             " ORDER BY per desc")

    results = query_executer(query)

    print("\nDays with more than 1'%' request errors\n")

    for result in results:
        print(result[0] +
              " - Request Error percentage is:- " +
              str(result[1]) +
              "%")


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    days_with_lotsoferrors()
