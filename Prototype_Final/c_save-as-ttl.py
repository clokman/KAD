from b_ttl_triple_creator import triples_list

# IMPORTANT: CHANGE FILE NAME WITH EACH NEW VERSION IF THE FILE IS TO BE IMPORTED TO PROTEGE.
# Protege does not always understand that this is a new file if the file name is the same with a previously imported file.
file_obj = open("Output//pure_bib_limited_0.4.9.ttl", "w")

for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')

print ("Success: The triples are written to the specified file.")