from django.test import TestCase
from django.db import models
#from daily.models import Journal
import sqlite3

import os

bad_words = ['Travis','travis','/home']

class StaticTestCases(TestCase):
    def test_no_bad_words(self):
        for f_name in os.listdir('blog'):
            if f_name.endswith('.py'):
                with open('blog/{}'.format(f_name)) as f:
                    for line in f.readlines():
                        for word in bad_words:
                            assert line.find(word) == -1, 'Found an invalid word {} in {}'.format(word, line)
    
    def test_sql_titles(self):
        #journal = Journal.objects.get()
        #t1 = Journal.objects.raw('SELECT TOP 1 FROM entries')[0]
        #assert t1 == 'Setting Up Blog with Django', 'Not the correct title: {}'.format(t1)
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        query = cur.execute('SELECT * FROM daily_journal LIMIT 1;')
        values = query.fetchall()[0]
        assert values[0] == 1, 'Invalid index number {}'.format(values[0])
        assert values[1] == 'Setting Up Blog with Django', 'Invalid title'
        assert values[2] == '2019-12-07 02:08:00', 'Invalid date'
