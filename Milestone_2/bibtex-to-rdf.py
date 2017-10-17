from bibtex_parser import bibDictionary


# Property URIs
has_written_uri_string      = "http://clokman.com/ontologies/scientific-research/#has_written"
rdf_type_uri_string         = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
named_individual_uri_string = "http://www.w3.org/1999/02/22-rdf-syntax-ns#NamedIndividual"
for each_entry in bibDictionary.items():
    #print (each_entry)
    author_uri_string   = "http://clokman.com/ontologies/scientific-research/#" + each_entry[1][0]["b_author"][0]
    document_uri_string = "http://clokman.com/ontologies/scientific-research/#" + each_entry[1][1]["b_instance"]

    print (author_uri_string    + " " +     has_written_uri_string  + " " +     document_uri_string             + " .")
    print (author_uri_string    + " " +     rdf_type_uri_string     + " " +     named_individual_uri_string     + " .")
    print (document_uri_string  + " " +     rdf_type_uri_string     + " " +     named_individual_uri_string     + " .")


#one-time assertions:
property_assertions = [
    "http://clokman.com/ontologies/scientific-research/#has_written " + " http://www.w3.org/1999/02/22-rdf-syntax-ns#type " + " http://www.w3.org/1999/02/22-rdf-syntax-ns#ObjectProperty " + "."
]

print (property_assertions)