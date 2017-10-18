from b_bibtex_to_rdf import triples_list
print (triples_list)

file_obj = open("pure_bib_limited_0.3.ttl", "w")
for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')



#from rdflib import Graph, RDF, Namespace, Literal, URIRef
#
#def serialize():
#    print Graph().serialize(format='turtle')
#
#
#def save(filename):
#    with open(filename, 'w') as f:
#        Graph().serialize(f, format='turtle')
#
#
#def load(filename):
#    with open(filename, 'r') as f:
#        Graph().load(f, format='turtle')
#
#load("pure.ttl")
#
#for each_triple in triples_list:
#    Graph().add(each_triple)
#
#
#