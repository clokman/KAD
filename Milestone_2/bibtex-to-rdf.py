# This Python file uses the following encoding: utf-8
# The line above is a magic comment and it should not be removed.

import bibtexparser
with open("C:\\Users\\Clokman\\Google Drive\\__Projects__\\Code\\KAD\\Milestone_2\\test.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)


# Print specific part of the example
for each_entry in bib_database.entries:
    print (str(each_entry['author'] + " has_article ") + each_entry['title'] + ' .')
    #try:
    #    print (each_entry["ENTRYTYPE"])
    #except:
    #    pass