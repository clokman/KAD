This ontology pack contains four documents:

- "integrator-ontology" is the ontology that is created by Protege when I imported the three other ontologies/data in the program and then saved (but made no changes to the ontologies in Protege, as everything was already finalized in those files beforehand). I include this file as it contains some information about how I imported the ontologies, so perhaps it could be useful. 

- "scientific-research-v2.6.5.ttl" is the main ontology of this project, which was constructed as a result of the assignments in the first 5 weeks, and then improved.


- "pure_bib_limited_0.6.5.ttl" is the data parsed and converted to .ttl format from the .bib file exported from VU Pure server. 

- Finally, "web_of_science_categories_0.2.5.ttl" contains a categorization of fiels of science according to Web of Science. This file does not contain instances, and is intended for conceptual integration with the scientific-research ontology (i.e., adding fields of science classes to it).

In my workflow, I opened a blank Protege file, and combined these files via direct import, and then saved them with "file/gather ontologies" function.

In their current form, these files should also be directly importable to Stardog, as this is how I constructed my final triple store.

John