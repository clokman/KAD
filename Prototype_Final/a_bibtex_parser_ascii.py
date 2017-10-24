# TODO: Conversion to Python 3
# TODO: Change "publication"  to "jounal"
# DONE: Add labels
# DONE: Multi-author support


from pybtex.database.input import bibtex
import re

# Parse input file
parser = bibtex.Parser()                                            # shorten parser function
bibdata = parser.parse_file("Input//pure_bib_limited_test.bib")     # parse the given bibtex file into variables

# Output container
bibDictionary = {}  # container for the main dictionary that will be outputted from the script


def transform_to_ontology_property(bib_data_object, target_entry_id, parsed_bibtex_field_name, new_ontology_property_name):
    """
    Function for basic transformation of parsed bibtex values to a triple-ready format.
    :param target_entry_id: the index key of the bibliography entry (e.g., 321098471224)
    :param parsed_bibtex_field_name: Name of the property (i.e., field) as it is parsed in pybtex.
    :param new_ontology_property_name: The desired property (i.e., predicate) name in the new ontology
    :return:

    :example:
        # import from pybtex.database.input import bibtex; parser.parse_file("Input//pure_bib_limited_test.bib") # parse the file
        # bibDictionary = {} # container entities to be extracted
        # for each_entry_id in bibdata.entries:
        #     current_entry           = bibdata.entries[each_entry_id]
        #     transform_to_ontology_property(bibDictionary, current_entry, "title", "b_title")
    """
    try:
        bibDictionary[target_entry_id][new_ontology_property_name] = \
            bib_data_object.entries[each_entry_id].fields[parsed_bibtex_field_name].encode("ascii", errors="ignore")  # variable with the desired name, which now stores the referenced bibtex entity

    # if title field is missing from bibliography:
    except(KeyError):
        pass


# loop through individual reference entries in the parsed bib file
for each_unicode_entry_id in bibdata.entries:
    each_entry_id = each_unicode_entry_id.encode("ascii",errors="ignore")

    current_entry           = bibdata.entries[each_entry_id]
    current_type            = bibdata.entries[each_entry_id].type.encode("ascii", errors="ignore")
    current_entry_fields    = current_entry.fields
    current_entry_persons   = current_entry.persons

    current_title = current_entry_fields["title"].encode("ascii",errors="ignore")

    bibDictionary[each_entry_id] = {} # create a new item in bibDictionary for each entry id,
                                                                      # and let each of these items contain a subdictionary.
                                                                      # e.g., bibDictionary = { 34324242235:{}, 43214321421421:{}, ... }


    ######################### CURRENT TITLE -> B_LABEL ############################

    bibDictionary[each_entry_id]["b_document_label"] = current_title


    ############################ AUTHOR -> B AUTHOR ################################

    try:
        bibDictionary[each_entry_id]["b_authors"]       = []  # prepare an empty container for author entities (which is a sub-dictionary of bibDictionary) so it can be appended later with merged author first names and last names.
        bibDictionary[each_entry_id]["b_author_labels"] = []   # prepare an empty container for author labels

        for author in current_entry_persons["author"]:  # for each author

            omittedCharacters = "[\{\}\ \.\'\"\(\)]"                                        # these characters will be omitted from author names after they are combined

            try:
                # Format names
                lastName = re.sub(omittedCharacters, "", author.last()[0].encode("ascii",errors="ignore"))   # simplify the format of author last and first names by omitting the specified characters
                firstName = re.sub(omittedCharacters, "", author.first()[0].encode("ascii",errors="ignore")) # ...

                # Add to dictionary
                bibDictionary[each_entry_id]["b_authors"].append(str(lastName + "_" + firstName))         # stitch last and first names to each other and add them to the container constructed before
                bibDictionary[each_entry_id]["b_author_labels"].append(str(lastName + ", " + firstName))  # do the same to create author labels

            except:  # if author's first name is missing:
                # Format last name
                lastName = re.sub(omittedCharacters, "", author.last()[0].encode("ascii",errors="ignore"))

                # Add to dictionary
                bibDictionary[each_entry_id]["b_authors"].append((str(lastName)))

            # a case where author's last name is missing but first name is present was deliberately not included.

    except:  # If the whole author field is missing from bibliography:
        pass


    #################### TITLE -> B DOCUMENT INSTANCE #########################

    try:
        current_title = current_entry_fields["title"]                   # extract title
        current_title = current_title.encode("ascii", errors="ignore")  # change character encoding for this string to ascii

        # Format the current title into a variable name format
        current_title = re.sub(" ", "_", current_title)
        current_title = re.sub("-", "_", current_title)
        current_title = re.sub(" in ", " In ", current_title)
        current_title = re.sub(" on ", " On ", current_title)
        current_title = re.sub(" at ", " At ", current_title)
        current_title = re.sub(" for ", " For ", current_title)
        current_title = re.sub(" with ", " With ", current_title)
        current_title = re.sub(" from ", " From ", current_title)

        omitted_characters_for_instance_names = "[\{\}\.,;:\\\#\'\"\(\)]" # these characters will be omitted from the final title names

        current_title = re.sub(omitted_characters_for_instance_names, "", current_title) # omit the given characters

        bibDictionary[each_entry_id]["b_document_instance_name"] = current_title

    # if title field missing from bibliography:
    except(KeyError):
        pass


    ######################### TYPE -> B TYPE (OF DOCUMENT) ############################

    try:
        bibDictionary[each_entry_id]["b_type"] = current_type
    except:
        pass


    ####################### JOURNAL -> B PUBLICATION INSTANCE #############################

    try:
        current_journal = current_entry_fields["journal"]                  # extract journal name from parsed variable
        current_journal = current_journal.encode("ascii",errors="ignore")  # change character encoding for this string to ascii

        current_journal = re.sub(" in ", " In ", current_journal)          # format the journal name
        current_journal = re.sub(" on ", " On ", current_journal)
        current_journal = re.sub(" at ", " At ", current_journal)
        current_journal = re.sub(" for ", " For ", current_journal)
        current_journal = re.sub(" with ", " With ", current_journal)
        current_journal = re.sub(" from ", " From ", current_journal)

        omitted_characters_for_journal_names = "[\{\}\ \. ,\'\"\(\)]"  # these will be omitted from the journal's instance name
        current_journal = re.sub(omitted_characters_for_journal_names, "", current_journal) # omit previously specified characters

        bibDictionary[each_entry_id]["b_journal"] = current_journal # add the formatted journal name, which is now an in instance name format to the dictionary

    except(KeyError): # if journal field missing from bibliography:
        pass          # skip this action


    ######################## PUBLISHER -> PUBLISHER (INSTANCE NAME) ###########################

    try:
        current_publisher_name = current_entry_fields["publisher"]                         # extract publisher name from parsed variable
        current_publisher_name = current_publisher_name.encode("ascii", errors="ignore")   # change character encoding for this string to ascii

        current_publisher_name = re.sub(" in ", " In ", current_publisher_name)            # format the publisher name
        current_publisher_name = re.sub(" on ", " On ", current_publisher_name)
        current_publisher_name = re.sub(" at ", " At ", current_publisher_name)
        current_publisher_name = re.sub(" for ", " For ", current_publisher_name)
        current_publisher_name = re.sub(" with ", " With ", current_publisher_name)
        current_publisher_name = re.sub(" from ", " From ", current_publisher_name)

        omittedCharactersForPublisherNames = "[\{\}\ \. ,\'\"\(\)]"             # these will be omitted from the publisher's instance name
        current_publisher_name = re.sub(omittedCharactersForPublisherNames, "", current_publisher_name) # omit previously specified characters

        bibDictionary[each_entry_id]["b_publisher"] = current_publisher_name    # add the formatted publisher name, which is now in instance name format to the dictionary

    # if publisher field missing from bibliography
    except(KeyError):
        pass


    ######################## TITLE -> B TITLE ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "title", "b_title")

    ######################## YEAR -> B PUBLICATION YEAR ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "year", "b_publication_year")

    ######################## MONTH -> B PUBLICATION MONTH ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "month", "b_publication_month")

    ######################## NUMBER -> B ISSUE NUMBER ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "number", "b_issue_number")

    ######################## VOLUME -> B VOLUME ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "volume", "b_volume")

    ######################## PAGES -> B PAGES ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "pages", "b_pages")

    ######################## DOI -> B DOI ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "doi", "b_doi")

    ######################## ISSN -> B ISSN ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "issn", "b_issn")

    ######################## ISBN -> B ISBN ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "isbn", "b_isbn")

    ######################## EDITION -> B EDITION ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "edition", "b_edition")

    ######################## BOOK TITLE -> B BOOK TITLE ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "booktitle", "b_book_title")

    ######################## ABSTRACT -> B ABSTRACT ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "abstract", "b_abstract")

    ######################## KEYWORDS -> B KEYWORDS ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "keywords", "b_keywords")

    ######################## NOTE -> B NOTE ###########################
    transform_to_ontology_property(bibdata, each_entry_id, "note", "b_note")


# SERIES_TITLE AND ID -- This has to be kept out of the main loop, as series is not a field, but a whole bibliography entry themselves.
# They are not nested within individual entries, and are rather parallel to them.
#try:
#    # collection refers to a full reference entity, and this is why the title of the collection is nested quite deeper than other elements parsed before in this script
#    for series_id in bibdata.entries[each_entry_id].collection.entries:
#        print series_id, each_entry_id
#        #bibDictionary[each_entry_id].append({"is_part_of_series_with_title":[each_entry_id].fields["title"].encode("ascii",errors="ignore")
#        bibDictionary[each_entry_id].append({"is_part_of_series_with_id":series_id})
#        #[each_entry_id].fields["title"].encode("ascii",errors="ignore")
## field missing from bibliography
#except(KeyError):
#    pass

# MAIN PRINT FUNCTION
from pprint import pprint
pprint(bibDictionary)