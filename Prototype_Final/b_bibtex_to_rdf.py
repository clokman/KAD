## TODO: Use different domain names and prefixes for ontology, instances ,datasets, etc...

from a_bibtex_parser_ascii import bibDictionary

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################
triples_list = []                 # Gather all triples to be generated here; this will be the output of this script.
#add_triple = triples_list.append # Add triples to the list of triples


def add_triple (subject, property, object): # local function
    """
    Constructs a triple from three given arguments and adds it to triples_list.

    :param subject: The subject; 1st element of triple
    :param property:  The property in triple; the predicate, 2nd element of triple.
    :param object: The object in triple; 3rd element of triple.
    :return: Adds the triple to triples_list.
)
    """
    triple = subject + " " + property + " " + object + " ." # construct a triple in turtle format.
    triples_list.append(triple)                             # add the triples_list


def construct_URI (prefix, name): # universal function
    """
    :return:
    :example:
        construct_URI(sr, "Document")
    """
    URI = "<" + prefix + name + ">"
    return URI

def construct_string_literal(input_string): # universal function
    """
    Constructs an English (@en) string literal in turtle format.

    :param input_string: The string to be formatted as turtle sting literal.
    :return: English string literal in turtle format

    :example:
        construct_string_literal(current_fields["b_document_label"])

    :example:
        add_triple (i_document_instance, p_label,  construct_string_literal(current_fields["b_document_label"]))
    """

    new_string_literal = "\"" + input_string + "\"" + "@en"
    return new_string_literal


#################################################################################
#                   STATIC DEFINITIONS: PROPERTIES, CLASSES                     #
#################################################################################

###### NAMESPACE PREFIX DEFINITIONS ######
sr   = "http://clokman.com/ontologies/scientific-research#"  # assign long domain  name to short variable.
rdf  = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl  = "http://www.w3.org/2002/07/owl#"


###### STATIC CLASS DEFINITIONS (c_ )######
c_document         = construct_URI( sr,   "Document"        ) # assign uri to document superclass
c_publication      = construct_URI( sr,   "Publication"     ) # assign URI to Publication class
c_named_individual = construct_URI( owl , "NamedIndividual" ) # ...
c_object_property  = construct_URI( owl , "ObjectProperty"  ) # ...
c_class            = construct_URI( rdfs, "Class"           ) # ...


###### STATIC PROPERTY DEFINITIONS (p_) ######
p_subclass_of      = construct_URI( rdfs,"subClassOf"    ) # assign URI to subclass of
p_is_author_of     = construct_URI( sr,  "isAuthorOf"    ) # assign URI to is author of
p_is_published_on  = construct_URI( sr,  "isPublishedOn" ) # ...
p_rdf_type         = construct_URI( rdf, "type"          ) # ...
p_label            = construct_URI( rdfs,"label"         ) # ...


#################################################################################
#                            STATIC TRIPLES: TYPES                              #
#################################################################################

###### STATIC TYPE TRIPLES (p_) ######
add_triple( p_is_author_of,     p_rdf_type,     c_object_property ) # is author of is a property
add_triple( p_is_published_on,  p_rdf_type,     c_object_property ) # is published on is a property
add_triple( p_rdf_type,         p_rdf_type,     c_object_property ) # type is a property


#################################################################################
#                     DYNAMIC TRIPLES: INSTANCES AND TYPES                      #
#################################################################################

for each_entry in bibDictionary.items():
    # VARIABLES:
    # These fields exist for each entry:
    current_identifier        = each_entry[0]                          # identifier
    current_fields            = each_entry[1]                          # fields
    current_authors           = current_fields["b_authors"]            # authors
    current_author_labels    = current_fields["b_author_labels"]
    current_document_instance = current_fields["b_document_instance_name"]  # document instance
    current_type              = current_fields["b_type"]               # type
    # Other fields do not exist for each entry. These fields will be treated individually.


    #######  URIs  #######
    # NOTE: Do not move the lines below to category and instance definitions section in the beginning of the script. c_document_class values need to be dynamically assigned within this for loop, as the document classes (e.g., Article, Book) are extracted from the resource file.
    c_document_class      = construct_URI( sr, current_type              )  # extract the class of the current document (e.g., Article, Book) and assign it to the current iteration of the c_document_class variable
    i_document_instance   = construct_URI( sr, current_document_instance )  # assign current document instance to an instance variable (denoted by i_), and give it an URI


    #######  DOCUMENT INSTANCE + DOCUMENT CLASS  #######
    add_triple( c_document_class,     p_subclass_of,    c_document         ) # make current document's class a subclass of the superclass "Document".
    add_triple( i_document_instance,  p_rdf_type,       c_named_individual ) # the current document is an an instance
    add_triple( i_document_instance,  p_rdf_type,       c_document_class   ) # bind the extracted document classes to the document instances (the latter was extracted previously in this loop)


    #######  DOCUMENT LABEL  #######

    add_triple(i_document_instance, p_label, construct_string_literal(current_fields["b_document_label"]))


    #######  AUTHOR  ########
    for each_current_author in current_authors:

        # Assign author to instance
        i_author = construct_URI(sr, each_current_author) # assign this author to an instance variable (denoted by i_), and give it an URI

        # Bind the instances to each other and define their types
        add_triple( i_author,      p_is_author_of,     i_document_instance) # the current author is the author of the current document
        add_triple( i_author,      p_rdf_type,         c_named_individual ) # the current author is an an instance


    #######  AUTHOR  LABEL  ########
    for each_current_author_label in current_author_labels:
        add_triple( i_author,      p_label,            construct_string_literal(each_current_author_label))  # the current author is an an instance


    #######  PUBLICATION INSTANCE + PUBLISHED ON  #######
    # NOTE: Use this "try-except" structure except identifier, authors, document instance, type--all fields except these ones may not always be present.
    try:
        current_publication = current_fields["b_journal"]         # extract current publication instance
        i_publication       = construct_URI(sr, current_publication)  # create  URI from publication instance

        # Bind the instances to each other and define their types
        add_triple( i_document_instance,   p_is_published_on,  i_publication      )  # the current document is published on the current publication
        add_triple( i_publication,         p_rdf_type,         c_named_individual )  # the current publication is an instance

    except:
        pass

from pprint import pprint
pprint(triples_list)
