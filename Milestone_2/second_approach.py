from pybtex.database.input import bibtex

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("test.bib")

#loop through the individual references
authorsList =  []
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
# change these lines to create a SQL insert
        #print(b["title"])
        #print(b["journal"])
        #print(b["year"])
        #deal with multiple authors
        for author in bibdata.entries[bib_id].persons["author"]:
            #print(author.first(), author.last())
            try:
                authorsList.append(str(author.last()[0].encode("utf-8") + "_" + author.first()[0].encode("utf-8")))
            except:
                authorsList.append(str(author.last()[0].encode("utf-8")))

    # 'author' field may not exist for a reference (i.e., both the first and last name of an author may be missing)
    except(KeyError):
        authorsList.append("noName")

print (authorsList)

import re
authorsListFormatted = []
for each_author in authorsList:
    authorsListFormatted.append(re.sub("[\{\}\ \.]", "", each_author))
print (authorsListFormatted)
