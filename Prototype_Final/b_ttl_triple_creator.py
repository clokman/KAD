## TODO: Use different domain names and prefixes for ontology, instances ,datasets, etc...
## TODO: Add basic class equivalencies (e.g., article = JournalArticle) to script

from a_bibtex_parser_ascii import bibDictionary
from pprint import pprint
from x_common_functions import *

#################################################################################
#                   STATIC DEFINITIONS: PROPERTIES, CLASSES                     #
#################################################################################

###### NAMESPACE PREFIX DEFINITIONS ######
sr   = "http://clokman.com/ontologies/scientific-research#"  # assign long domain  name to short variable.
pvu  = "http://clokman.com/ontologies/pure-vu#"  # assign long domain  name to short variable.
rdf  = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl  = "http://www.w3.org/2002/07/owl#"

add_prefix_triple("",    sr)
add_prefix_triple("pvu",  pvu)
add_prefix_triple("rdf",  rdf)
add_prefix_triple("rdfs", rdfs)
add_prefix_triple("owl",  owl)


###### STATIC CLASS DEFINITIONS (c_ )######
c_document         = construct_uri( sr,   "Document"        )  # assign URI to document superclass
c_journal          = construct_uri( sr,   "Journal"     ) # assign URI to Journal class
c_named_individual = construct_uri( owl , "NamedIndividual" )  # ...
c_object_property  = construct_uri( owl , "ObjectProperty"  )  # ...
c_class            = construct_uri( rdfs, "Class"           )  # ...


###### STATIC PROPERTY DEFINITIONS (p_) ######
p_subclass_of            = construct_uri( rdfs,"subClassOf"          )  # assign URI to subclass of
p_is_author_of           = construct_uri( sr,  "isAuthorOf"          )  # assign URI to is author of
p_is_published_on        = construct_uri( sr,  "isPublishedOn"       )  # ...
p_rdf_type               = construct_uri( rdf, "type"                )  # ...
p_label                  = construct_uri( rdfs,"label"               )  # ...
p_equivalent_class       = construct_uri( owl, "equivalentClass" )      # ...

add_triple( p_subclass_of,              p_rdf_type,     c_object_property )  # is author of is a property
add_triple( p_is_author_of,             p_rdf_type,     c_object_property )  # is author of is a property
add_triple( p_is_published_on,          p_rdf_type,     c_object_property )  # is published on is a property
add_triple( p_rdf_type,                 p_rdf_type,     c_object_property )  # type is a property
add_triple( p_label,                    p_rdf_type,     c_object_property )
add_triple( p_equivalent_class,         p_rdf_type,     c_object_property )

#################################################################################
#       DOCUMENT CLASS DECLARATIONS AND CLASS EQUIVALENCY ASSERTIONS            #
#################################################################################


# SR document type definitions
# These are not used to categorize instances in the document directly, but necessary for the class equivalencies with Pure-VU document types.
# As these are the document classes in the main ontology, their variable names are not suffixed as in other cases (e.g., c_article_pvu).
c_journal_article = construct_uri(sr, "JournalArticle")
c_book            = construct_uri(sr, "Book")
c_book_chapter    = construct_uri(sr, "BookChapter")
c_miscellaneous   = construct_uri(sr, "Miscellaneous")

add_triple(c_journal_article,  p_rdf_type, c_class)
add_triple(c_book,             p_rdf_type, c_class)
add_triple(c_book_chapter,     p_rdf_type, c_class)
add_triple(c_miscellaneous,    p_rdf_type, c_class)


# Pure-VU document type definitions
# These are necessary for class equivalency assertions between Pure-VU and SR document classes
# These pure VU class names (e.g., 'article', 'book', 'inbook') are not coded anywhere in these scripts, but they are parsed with the below names by pybtex package.
# These classes are *automatically* (hence no explicit usage anywhere) used to assign types to instances in the code below.
# As these are NOT the document classes in the main ontology, their variable names are suffixed (e.g., c_article_pvu).
c_article_pvu = construct_uri(pvu, "article")
c_book_pvu    = construct_uri(pvu, "book")
c_inbook_pvu  = construct_uri(pvu, "inbook")
c_misc_pvu    = construct_uri(pvu, "misc")

add_triple(c_article_pvu,    p_rdf_type, c_class)
add_triple(c_book_pvu,       p_rdf_type, c_class)
add_triple(c_inbook_pvu,     p_rdf_type, c_class)
add_triple(c_misc_pvu,       p_rdf_type, c_class)


# Class equivalency assertions
add_triple(c_article_pvu, p_equivalent_class, c_journal_article)
add_triple(c_book_pvu,    p_equivalent_class, c_book)
add_triple(c_inbook_pvu,  p_equivalent_class, c_book_chapter)
add_triple(c_misc_pvu,    p_equivalent_class, c_miscellaneous)


#################################################################################
#                     DYNAMIC TRIPLES: INSTANCES AND TYPES                      #
#################################################################################

for each_entry in bibDictionary.items():

    #######  GENERAL VARIABLES  #######
    # These fields exist for each entry:
    current_identifier             = each_entry[0]                               # identifier
    current_fields                 = each_entry[1]                               # fields that contain bibliographic information
    current_authors                = current_fields["b_authors"]                 # authors
    current_author_labels          = current_fields["b_author_labels"]
    current_document_instance_name = current_fields["b_document_instance_name"]  # document instance
    current_type                   = current_fields["b_type"]                    # type
    # Other fields do not exist for each entry. These fields will be treated individually.


    #######  URIs  #######
    # NOTE: Do not move the lines below to category and instance definitions section in the beginning of the script. c_document_class values need to be dynamically assigned within this for loop, as the document classes (e.g., Article, Book) are extracted from the resource file.
    c_document_class      = construct_uri( pvu, current_type                   )  # extract the class of the current document (e.g., Article, Book) and assign it to the current iteration of the c_document_class variable
    i_document_instance   = construct_uri( pvu, current_document_instance_name )  # assign current document instance to an instance variable (denoted by i_), and give it an URI


    #######  DOCUMENT INSTANCE + DOCUMENT CLASS  #######
    add_triple( c_document_class,     p_subclass_of,    c_document         )  # make current document's class a subclass of the superclass "Document".
    add_triple( i_document_instance,  p_rdf_type,       c_named_individual )  # the current document is an an instance
    add_triple( i_document_instance,  p_rdf_type,       c_document_class   )  # bind the extracted document classes to the document instances (the latter was extracted previously in this loop)


    #######  DOCUMENT LABEL  #######

    add_triple(i_document_instance, p_label, construct_string_literal(current_fields["b_document_label"]))


    #######  AUTHOR  ########
    for each_current_author in current_authors:

        # Assign author to instance
        i_author = construct_uri(pvu, each_current_author)  # assign this author to an instance variable (denoted by i_), and give it an URI

        # Bind the instances to each other and define their types
        add_triple( i_author,      p_is_author_of,     i_document_instance)  # the current author is the author of the current document
        add_triple( i_author,      p_rdf_type,         c_named_individual )  # the current author is an an instance


    #######  AUTHOR  LABEL  ########
    for each_current_author_label in current_author_labels:
        add_triple( i_author,      p_label,            construct_string_literal(each_current_author_label) )  # the current author is an an instance


    #######  PUBLICATION INSTANCE + PUBLISHED ON  #######
    # NOTE: Use this "try-except" structure except identifier, authors, document instance, type--all fields except these ones may not always be present.
    try:
        current_journal = current_fields["b_journal"]         # extract current publication instance
        i_journal       = construct_uri(pvu, current_journal)  # create  URI from publication instance

        # Bind the instances to each other and define their types
        add_triple( i_document_instance,   p_is_published_on,  i_journal          )  # the current document is published on the current publication
        add_triple( i_journal,             p_rdf_type,         c_named_individual )  # the current publication is an instance

    except:
        pass

pprint(triples_list)  # resides in x_common_functions.py
print ("Success: The triples are written to the specified file.")
