# TODO: Multi-author support

from pybtex.database.input import bibtex
import re

# open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("Input//pure_bib_limited.bib")

# this is the container for the main dictionary
bibDictionary = {}


def transform_to_ontology_property(target, bibtex_field_name, ontology_property_name):
    """
    Function for basic transformation of parsed bibtex values to a triple-ready format.
    :param bibtex_field_name: Name of the property (i.e., field) in pybtex.
    :param ontology_property_name: The property (i.e., predicate) name in the new ontology
    :return:
    """
    try:
        bibDictionary[target.encode("ascii", errors="ignore")].append(
            {ontology_property_name: b[bibtex_field_name].encode("ascii", errors="ignore")})

    # if title field is missing from bibliography:
    except(KeyError):
        pass


# loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields

    try:
        # change these lines to create a SQL insert
        # print(b["title"])
        # print(b["journal"])
        # print(b["year"])
        # deal with multiple authors

        # AUTHOR
        for author in bibdata.entries[bib_id].persons["author"]:
            # print(author.first(), author.last())

            # prepare an empty container for author entities (merged author first names and last names), so it can be
            # appended later. This is a JSON-like structure.
            bibDictionary[bib_id.encode("ascii",errors="ignore")] = [{"b_author": []}]

            # omit these characters from text
            omittedCharacters = "[\{\}\ \.\'\"\(\)]"

            try:
                # simplify the format of author last and first names
                lastName = re.sub(omittedCharacters, "", author.last()[0].encode("ascii",errors="ignore"))
                firstName = re.sub(omittedCharacters, "", author.first()[0].encode("ascii",errors="ignore"))

                # stitch last and first names to each other
                # and add them to the JSON-like container constructed before
                bibDictionary[bib_id.encode("ascii",errors="ignore")][0]["b_author"].append((str(lastName + "_" + firstName)))

                # bibDictionary[bib_id.encode("ascii",errors="ignore")] = [{"b_author":[(str(lastName + "_" + firstName))]}]


            # if author's first name is missing:
            except:
                lastName = re.sub(omittedCharacters, "", author.last()[0].encode("ascii",errors="ignore"))
                bibDictionary[bib_id.encode("ascii",errors="ignore")][0]["b_author"].append((str(lastName)))

                # a case where author's last name is missing but first name is present was deliberately not included.

    # the whole author field is missing from bibliography
    except(KeyError):
        pass

    # INSTANCE NAME
    try:
        longTitle = b["title"]

        longTitle = re.sub(" in ", " In ", longTitle)
        longTitle = re.sub(" on ", " On ", longTitle)
        longTitle = re.sub(" at ", " At ", longTitle)
        longTitle = re.sub(" for ", " For ", longTitle)
        longTitle = re.sub(" with ", " With ", longTitle)
        longTitle = re.sub(" from ", " From ", longTitle)

        longTitle = re.sub(" ", "_", longTitle)
        longTitle = re.sub("-", "_", longTitle)

        omittedCharactersForInstanceNames = "[\{\}\.,;:\\\#\'\"\(\)]"

        longTitle = re.sub(omittedCharactersForInstanceNames, "", longTitle.encode("ascii",errors="ignore"))

        bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"b_document_instance": longTitle})

    # if title field missing from bibliography:
    except(KeyError):
        pass


    # TYPE
    try:
        bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"b_type": bibdata.entries[bib_id].type.encode("ascii",errors="ignore")})
    # if the type information is missing from bibliography:
    except(KeyError):
        pass


    # JOURNAL
    try:
        journalName = b["journal"]

        journalName = re.sub(" in ", " In ", journalName)
        journalName = re.sub(" on ", " On ", journalName)
        journalName = re.sub(" at ", " At ", journalName)
        journalName = re.sub(" for ", " For ", journalName)
        journalName = re.sub(" with ", " With ", journalName)
        journalName = re.sub(" from ", " From ", journalName)

        omittedCharactersForJournalNames = "[\{\}\ \. ,\'\"\(\)]"
        journalName = re.sub(omittedCharactersForJournalNames, "", journalName.encode("ascii",errors="ignore"))

        bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"b_publication": journalName.encode("ascii",errors="ignore")})

    # if journal field missing from bibliography
    except(KeyError):
        pass


    # PUBLISHER
    try:
        publisherName = b["publisher"]

        publisherName = re.sub(" in ", " In ", publisherName)
        publisherName = re.sub(" on ", " On ", publisherName)
        publisherName = re.sub(" at ", " At ", publisherName)
        publisherName = re.sub(" for ", " For ", publisherName)
        publisherName = re.sub(" with ", " With ", publisherName)
        publisherName = re.sub(" from ", " From ", publisherName)

        omittedCharactersForPublisherNames = "[\{\}\ \. ,\'\"\(\)]"
        publisherName = re.sub(omittedCharactersForPublisherNames, "", publisherName.encode("ascii",errors="ignore"))

        bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"b_publisher": publisherName.encode("ascii",errors="ignore")})
    # if publisher field missing from bibliography
    except(KeyError):
        pass

    # TITLE
    transform_to_ontology_property(bib_id, "title", "b_title")

    # YEAR
    transform_to_ontology_property(bib_id, "year", "b_publication_year")

    # MONTH
    transform_to_ontology_property(bib_id, "month", "b_publication_month")

    # NUMBER
    transform_to_ontology_property(bib_id, "number", "b_issue_number")

    # VOLUME
    transform_to_ontology_property(bib_id, "volume", "b_volume")

    # PAGES
    transform_to_ontology_property(bib_id, "pages", "b_pages")

    # DOI
    transform_to_ontology_property(bib_id, "doi", "b_doi")

    # ISSN
    transform_to_ontology_property(bib_id, "issn", "b_issn")

    # ISBN
    transform_to_ontology_property(bib_id, "isbn", "b_isbn")

    # EDITION
    transform_to_ontology_property(bib_id, "edition", "b_edition")

    # BOOKTITLE
    transform_to_ontology_property(bib_id, "booktitle", "b_book_title")

    # ABSTRACT
    transform_to_ontology_property(bib_id, "abstract", "b_abstract")

    # KEYWORDS
    transform_to_ontology_property(bib_id, "keywords", "b_keywords")

    # NOTE
    transform_to_ontology_property(bib_id, "note", "b_note")


# SERIES_TITLE AND ID -- This has to be kept out of the main loop, as series is not a field, but a whole bibliography entry themselves.
# They are not nested within individual entries, and are rather parallel to them.
#try:
#    # collection refers to a full reference entity, and this is why the title of the collection is nested quite deeper than other elements parsed before in this script
#    for series_id in bibdata.entries[bib_id].collection.entries:
#        print series_id, bib_id
#        #bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"is_part_of_series_with_title":[bib_id].fields["title"].encode("ascii",errors="ignore")
#        bibDictionary[bib_id.encode("ascii",errors="ignore")].append({"is_part_of_series_with_id":series_id})
#        #[bib_id].fields["title"].encode("ascii",errors="ignore")
## field missing from bibliography
#except(KeyError):
#    pass

# MAIN PRINT FUNCTION
#from pprint import pprint
#pprint(bibDictionary)