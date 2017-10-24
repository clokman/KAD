from b_ttl_triple_creator import triples_list

file_obj = open("Output//pure_bib_limited_0.4.ttl", "w")
for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')

print ("Success: The triples are written to the specified file.")
