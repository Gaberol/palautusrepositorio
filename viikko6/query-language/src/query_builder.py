from matchers import *

class QueryBuilder:
    def __init__(self, query = All()) -> None:
        self.query_object = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_object, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))

    def build(self):
        return self.query_object
