from step_2_ttl_triple_creator import triples_list

# IMPORTANT: CHANGE FILE NAME WITH EACH NEW VERSION IF THE FILE IS TO BE IMPORTED TO PROTEGE.
# Protege does not always understand that this is a new file if the file name is the same with a previously imported file.
file_obj = open("Output//pure_bib_head_100k_0.8.3.ttl", "w")
# file_obj = open("Output//pure_bib_limited_0.6.5.ttl", "w")  # use for test version

for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')

print ("Success: The triples are written to the specified file.")

# NOTE: Check the integrity of the produced .ttl file in command line
# > ttl <path to file>
# e.g.,
# > ttl .\pure_bib_head_100k_0.7.0.ttl
# If ttl validator is not installed, it can be obtained from:
# https://github.com/IDLabResearch/TurtleValidator
# (or, npm install -g turtle-validator)