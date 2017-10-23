## TODO: Use different domain names and prefixes for ontology, instances ,datasets, etc...

from a_bibtex_parser_ascii import bibDictionary

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################
triples_list = []                # Gather all triples to be generated here; this will be the output of this script.
add_triple = triples_list.append # Add triples to the list of triples


#################################################################################
#                   STATIC DEFINITIONS: PROPERTIES, CLASSES                     #
#################################################################################

###### NAMESPACE PREFIX DEFINITIONS ######
sr  = "http://clokman.com/ontologies/scientific-research#"  # assign long domain  name to short variable.
rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl = "http://www.w3.org/2002/07/owl#"


###### STATIC CLASS DEFINITIONS (c_ )######
c_document         = "<" + sr   + "Document"        + ">" # assign uri to document superclass
c_publication      = "<" + sr   + "Publication"     + ">" # assign URI to Publication class
c_named_individual = "<" + owl  + "NamedIndividual" + ">" # ...
c_object_property  = "<" + owl  + "ObjectProperty"  + ">" # ...
c_class            = "<" + rdfs + "Class"           + ">" # ...


###### STATIC PROPERTY DEFINITIONS (p_) ######
p_subclass_of      = "<" + rdfs + "subClassOf"      + ">" # assign URI to subclass of
p_is_author_of     = "<" + sr  + "isAuthorOf"       + ">" # assign URI to is author of
p_is_published_on  = "<" + sr  + "isPublishedOn"    + ">" # ...
p_rdf_type         = "<" + rdf + "type"             + ">" # ...
p_label            = "<" + rdfs + "label"           + ">" # ...


#################################################################################
#                            STATIC TRIPLES: TYPES                              #
#################################################################################

###### STATIC TYPE TRIPLES (p_) ######
add_triple (p_is_author_of      + " " +     p_rdf_type  + " " + c_object_property + " .") # is author of is a property
add_triple (p_is_published_on   + " " +     p_rdf_type  + " " + c_object_property + " .") # is published on is a property
add_triple (p_rdf_type          + " " +     p_rdf_type  + " " + c_object_property + " .") # type is a property


#################################################################################
#                     DYNAMIC TRIPLES: INSTANCES AND TYPES                      #
#################################################################################

for each_entry in bibDictionary.items():
    # VARIABLES:
    # These fields exist for each entry:
    current_identifier        = each_entry[0]                          # identifier
    current_fields            = each_entry[1]                          # fields
    current_authors           = current_fields["b_authors"]            # authors
    current_document_instance = current_fields["b_document_instance"]  # document instance
    current_type              = current_fields["b_type"]               # type
    # Other fields do not exist for each entry. These fields will be treated individually.


    #######  URIs  #######
    # NOTE: Do not move the lines below to category and instance definitions section in the beginning of the script. c_document_class values need to be dynamically assigned within this for loop, as the document classes (e.g., Article, Book) are extracted from the resource file.
    c_document_class      = ("<" +  sr + current_type + ">")                  # extract the class of the current document (e.g., Article, Book) and assign it to the current iteration of the c_document_class variable
    i_document_instance   = ("<" +  sr + current_document_instance    + ">")  # assign current document instance to an instance variable (denoted by i_), and give it an URI


    #######  DOCUMENT INSTANCE + DOCUMENT CLASS  #######
    add_triple (c_document_class    + " " +      p_subclass_of   + " " +     c_document             + " .") # make current document's class a subclass of the superclass "Document".
    add_triple (i_document_instance  + " " +     p_rdf_type      + " " +     c_named_individual     + " .") # the current document is an an instance
    add_triple (i_document_instance  + " " +     p_rdf_type      + " " +     c_document_class       + " .") # bind the extracted document classes to the document instances (the latter was extracted previously in this loop)


    #######  AUTHOR  ########
    for each_current_author in current_authors:

        ### Assign author to instance
        i_author              = ("<" +  sr + each_current_author                  + ">") # assign this author to an instance variable (denoted by i_), and give it an URI

        ### Bind the instances to each other and define their types

        add_triple (i_author             + " " +     p_is_author_of  + " " +     i_document_instance    + " .") # the current author is the author of the current document
        add_triple (i_author             + " " +     p_rdf_type      + " " +     c_named_individual     + " .") # the current author is an an instance


    #######  PUBLICATION INSTANCE + PUBLISHED ON #######
    # NOTE: Use this "try-except" structure except identifier, authors, document instance, type--all fields except these ones may not always be present.
    try:
        current_publication = current_fields["b_publication"]  # extract current publication instance
        i_publication         = "<" +  sr + current_publication          + ">"  # create  URI from publication instance

        ### Bind the instances to each other and define their types
        add_triple (i_document_instance   + " "   + p_is_published_on     + " " + i_publication + " .")        # the current document is published on the current publication
        add_triple (i_publication         + " "   + p_rdf_type            + " " + c_named_individual + " ." )  # the current publication is an instance

    except:
        pass

from pprint import pprint
pprint(triples_list)

# TO ADD:
###### AUTHOR             - HAS LABEL   - LAVEL VALUE ######
###### DOCUMENT INSTANCE  - HAS LABEL   - LABEL VALUE ######