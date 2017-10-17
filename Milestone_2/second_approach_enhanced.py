from pybtex.database.input import bibtex
import re

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("test.bib")

#loop through the individual references
bibDictionary =  {}
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        # change these lines to create a SQL insert
        #print(b["title"])
        #print(b["journal"])
        #print(b["year"])
        #deal with multiple authors

    # AUTHOR
        for author in bibdata.entries[bib_id].persons["author"]:
            #print(author.first(), author.last())

            # prepare an empty container for author entities (merged author first names and last names), so it can be
            # appended later. This is a JSON-like structure.
            bibDictionary[bib_id.encode("utf-8")] = [{"has_author":[]}]

            # omit these characters from text
            omittedCharacters = "[\{\}\ \.]"

            try:
                # simplify the format of author last and first names
                lastName  = re.sub(omittedCharacters, "", author.last()[0].encode("utf-8"))
                firstName = re.sub(omittedCharacters, "", author.first()[0].encode("utf-8"))

                # stitch last and first names to each other
                # and add them to the JSON-like container constructed before
                bibDictionary[bib_id.encode("utf-8")][0]["has_author"].append( (str(lastName + "_" + firstName)) )

                #bibDictionary[bib_id.encode("utf-8")] = [{"authors":[(str(lastName + "_" + firstName))]}]


            # author's first name may be missing
            except:
                lastName = re.sub(omittedCharacters, "", author.last()[0].encode("utf-8"))
                bibDictionary[bib_id.encode("utf-8")][0]["has_author"].append( (str(lastName)) )

                # a case where author's last name is missing but first name is present was deliberately not included.

    # the whole author field is missing from bibliography
    except(KeyError):
        continue

    # TITLE
    try:
        bibDictionary[bib_id.encode("utf-8")].append({"has_title":b["title"].encode("utf-8")})

    # title field missing from bibliography
    except(KeyError):
        continue


    # JOURNAL
    try:
        journalName = b["journal"]

        journalName = re.sub(" in ", " In ", journalName)
        journalName = re.sub(" on ", " On ", journalName)
        journalName = re.sub(" at ", " At ", journalName)
        journalName = re.sub(" for ", " For ", journalName)
        journalName = re.sub(" with ", " With ", journalName)
        journalName = re.sub(" from ", " From ", journalName)

        omittedCharactersForJournalNames = "[\{\}\ \. ,]"
        journalName = re.sub(omittedCharactersForJournalNames, "", journalName.encode("utf-8"))

        bibDictionary[bib_id.encode("utf-8")].append({"is_published_by":journalName.encode("utf-8")})

    # journal field missing from bibliography
    except(KeyError):
        continue


    # YEAR
    try:
        bibDictionary[bib_id.encode("utf-8")].append({"is_published_on_year": b["year"].encode("utf-8")})
        # title field missing from bibliography
    except(KeyError):
        continue

    # MONTH
    try:
        bibDictionary[bib_id.encode("utf-8")].append({"is_published_on_month": b["month"].encode("utf-8")})
        # title field missing from bibliography
    except(KeyError):
        continue

    # DAY -- Not sure if 'day' is the correct bibtex tag for day of the month.
    try:
        bibDictionary[bib_id.encode("utf-8")].append({"is_published_on_day": b["day"].encode("utf-8")})
        # title field missing from bibliography
    except(KeyError):
        continue


from pprint import pprint
pprint(bibDictionary)



#import re
#bibDictionaryFormatted = []
#for each_id, each_list in bibDictionary.items():
#    bibDictionaryFormatted[each_id]=re.sub("[\{\}\ \.]", "", each_list[0])
#print (authorsListFormatted)
