from a_bibtex_parser_ascii import bibDictionary

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################

# Gather all triples to be generated here; this will be the output of this script.
triples_list = []

# Add triples to the list of triples
add_triple = triples_list.append


#################################################################################
#                   STATIC DEFINITIONS: PROPERTIES, CLASSES                     #
#################################################################################

###### NAMESPACE PREFIX DEFINITIONS ######
sr  = "http://clokman.com/ontologies/scientific-research#"
rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl = "http://www.w3.org/2002/07/owl#"


###### STATIC CLASS DEFINITIONS (c_ )######
c_document         = "<" + sr   + "Document"        + ">"
c_publication      = "<" + sr   + "Publication"     + ">"
c_named_individual = "<" + owl  + "NamedIndividual" + ">"
c_object_property  = "<" + owl  + "ObjectProperty"  + ">"
c_class            = "<" + rdfs + "Class"           + ">"


###### STATIC PROPERTY DEFINITIONS (p_) ######
p_subclass_of      = "<" + rdfs + "subClassOf"      + ">"
p_is_author_of     = "<" + sr  + "isAuthorOf"       + ">"
p_is_published_on  = "<" + sr  + "isPublishedOn"    + ">"
p_rdf_type         = "<" + rdf + "type"             + ">"
p_label            = "<" + rdfs + "label"           + ">"


#################################################################################
#                            STATIC TRIPLES: TYPES                              #
#################################################################################

###### STATIC TYPE TRIPLES (p_) ######
add_triple (p_is_author_of      + " " +     p_rdf_type  + " " + c_object_property + " .")
add_triple (p_is_published_on   + " " +     p_rdf_type  + " " + c_object_property + " .")
add_triple (p_rdf_type          + " " +     p_rdf_type  + " " + c_object_property + " .")


#################################################################################
#                     DYNAMIC TRIPLES: INSTANCES AND TYPES                      #
#################################################################################

# Instances (i_)
for each_entry in bibDictionary.items():
    # The structure of bibDictionary:
    #     print(each_entry[0])     # identifier
    #     print(each_entry[1])     # all information
    #     print(each_entry[1][0])  # authors
    #     print(each_entry[1][1])  # document instance
    #     print(each_entry[1][2])  # type
    #     print(each_entry[1][3:]) # varies


    # author - is_author_of - document_instance
    # instance of and author (i_author)equals each of the authors in the authors list
    i_author              = ("<" +  sr + each_entry[1][0]["b_author"][0]            + ">")
    i_document_instance   = ("<" +  sr + each_entry[1][1]["b_document_instance"]    + ">")

    add_triple (i_author             + " " +     p_is_author_of  + " " +     i_document_instance    + " .")
    add_triple (i_author             + " " +     p_rdf_type      + " " +     c_named_individual     + " .")
    add_triple (i_document_instance  + " " +     p_rdf_type      + " " +     c_named_individual     + " .")

    # document_instance - type of  - document class
    c_document_class      = ("<" + sr + each_entry[1][2]["b_type"] + ">")
    add_triple (i_document_instance + " " +       p_rdf_type      + " " +     c_document_class       + " .")
    add_triple (c_document_class    + " " +       p_subclass_of   + " " +     c_document             + " .")

    ## document_instance - published_on - publication
    for each_sub_entry in (each_entry[1][3:]):
        if "b_publication" in each_sub_entry:
            i_document_instance   = "<" +  sr + each_entry[1][1]["b_document_instance"]    + ">"
            i_publication         = "<" +  sr + each_sub_entry["b_publication"]            + ">"

            add_triple (i_document_instance   + " "   + p_is_published_on     + " " + i_publication + " .")
            add_triple (i_publication         + " "   + p_rdf_type            + " " + c_named_individual + " ." )



from pprint import pprint
pprint(triples_list)