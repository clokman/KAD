from a_bibtex_parser_ascii import bibDictionary

triples_list = []
trpl=triples_list.append

#namespace prefixes
sr  = "http://clokman.com/ontologies/scientific-research#"
rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl = "http://www.w3.org/2002/07/owl#"

# Classes (c_)
c_document         = "<" + sr   + "Document"        + ">"
c_publication      = "<" + sr   + "Publication"     + ">"
c_named_individual = "<" + owl  + "NamedIndividual" + ">"
c_object_property  = "<" + owl  + "ObjectProperty"  + ">"
c_class            = "<" + rdfs + "Class"           + ">"
p_subclass_of      = "<" + rdfs + "subClassOf"      + ">"

# Properties (p_)
p_is_author_of     = "<" + sr  + "isAuthorOf"       + ">"
p_is_published_on  = "<" + sr  + "isPublishedOn"    + ">"
p_rdf_type         = "<" + rdf + "type"             + ">"


trpl (p_is_author_of      + " " +     p_rdf_type  + " " + c_object_property + " .")
trpl (p_is_published_on   + " " +     p_rdf_type  + " " + c_object_property + " .")
trpl (p_rdf_type          + " " +     p_rdf_type  + " " + c_object_property + " .")

# Instances (i_)
for each_entry in bibDictionary.items():
    #print(each_entry[0])    # identifier
    #print(each_entry[1])    # all information
    #print(each_entry[1][0]) # authors
    #print(each_entry[1][1]) # document instance
    #print(each_entry[1][2])  # type
    #print(each_entry[1][3:]) # varies


    # author - is_author_of - document_instance
    i_author              = ("<" +  sr + each_entry[1][0]["b_author"][0]            + ">")
    i_document_instance   = ("<" +  sr + each_entry[1][1]["b_document_instance"]    + ">")

    trpl (i_author             + " " +     p_is_author_of  + " " +     i_document_instance    + " .")
    trpl (i_author             + " " +     p_rdf_type      + " " +     c_named_individual     + " .")
    trpl (i_document_instance  + " " +     p_rdf_type      + " " +     c_named_individual     + " .")

    # document_instance - type of  - document class
    c_document_class      = ("<" + sr + each_entry[1][2]["b_type"] + ">")
    trpl (i_document_instance + " " +       p_rdf_type      + " " +     c_document_class       + " .")
    trpl (c_document_class    + " " +       p_subclass_of   + " " +     c_document             + " .")

    ## document_instance - published_on - publication
    for each_sub_entry in (each_entry[1][3:]):
        if "b_publication" in each_sub_entry:
            i_document_instance   = "<" +  sr + each_entry[1][1]["b_document_instance"]    + ">"
            i_publication         = "<" +  sr + each_sub_entry["b_publication"]            + ">"

            trpl (i_document_instance   + " "   + p_is_published_on     + " " + i_publication + " .")
            trpl (i_publication         + " "   + p_rdf_type            + " " + c_named_individual + " ." )



from pprint import pprint
pprint(triples_list)


