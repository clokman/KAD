# This Python file uses the following encoding: utf-8
# The line above is a magic comment and it should not be removed.

# Example bibtex data
bibtex = """
@ARTICLE{Cesar2013,
  author = {Jean César},
  title = {An amazing title},
  year = {2013},
  month = jan,
  volume = {12},
  pages = {12--23},
  journal = {Nice Journal},
  abstract = {This is an abstract. This line should be long enough to test
     multilines...},
  comments = {A comment},
  keywords = {keyword1, keyword2}

@ARTICLE{Cesar2014,
  author = {Jean César44},
  title = {An amazing title44},
  year = {201344},
  month = jan44,
  volume = {142},
  pages = {12--234},
  journal = {Nice Journa4l},
  abstract = {This is an abstract. This line should be long enough to test
     multilines...},
  comments = {A comment},
  keywords = {keyword1, keyword2}


}
"""
# Write example above to a file
with open('bibtex.bib', 'w') as bibfile:
    bibfile.write(bibtex)


# Parse the example above
import bibtexparser
with open('bibtex.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()
bib_database = bibtexparser.loads(bibtex_str)
#print(bib_database.entries)



# Customize format
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record

with open('bibtex.bib') as bibtex_file:
    parser = BibTexParser()
    parser.customization = customizations
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
    #print(bib_database.entries)


# Print specific part of the example
for each_entry in bib_database.entries:

    #print (each_entry['author'])
    try:
        #print (each_entry)
        print (each_entry["title"])
        #print (each_entry["ENTRYTYPE"])
    except:
        pass
