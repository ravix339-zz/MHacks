from eventregistry import *
er = EventRegistry(apiKey = r'01a08d73-9e38-40f2-bd38-416ce2242351')
q = QueryArticlesIter(conceptUri = er.getConceptUri("Bitcoin"), lang="eng", dateStart=datetime.date(2017, 1, 23 ), dateEnd=datetime.date(2017, 10, 1))
for art in q.execQuery(er, sortBy = "date", sortByAsc= True):
    print (art)
    break