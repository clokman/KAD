# This Python file uses the following encoding: utf-8
# The line above is a magic comment and it should not be removed.

import bibtexparser
with open("C:\Users\Clokman\Google Drive\__Projects__\Code\KAD\Milestone2\Pure_research_output-51017.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Print specific part of the example
for each_entry in bib_database.entries:
    #print (each_entry['author'])
    try:
        print (each_entry["ENTRYTYPE"])
    except:
        pass
