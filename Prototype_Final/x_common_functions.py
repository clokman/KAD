def construct_uri(prefix, name):  # universal function
    """
    :return:
    :example:
        construct_uri(sr, "Document")
    """
    uri = "<" + prefix + name + ">"
    return uri


def construct_string_literal(input_string):  # universal function
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


triples_list = []

def add_triple(sub, prop, obj, triples_list_to_append=triples_list):  # local function
    """
    Constructs a triple from three given arguments and adds it to triples_list.

    :param sub: The subject; the 1st element of triple
    :param prop:  The property in triple; the predicate, the 2nd element of triple.
    :param obj: The object in triple; the 3rd element of triple.
    :param triples_list_to_append: The variable name that will be used to append the triple. Default value is refers
        to the variable triples_list. If triples_list variable is stored in the same script with this function
        i.e., in this file), and can be called by its name from the file which the function is executed, provided that
        it is imported (e.g., using "from x_common_functions import *").
    :exception: If no list variable is defined before the function is called, function will return error.

    :return: Adds the triple to triples_list.
    :example:
        add_triple("<http://clokman.com/ontologies/scientific-research>", "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "http://www.w3.org/2002/07/owl#Ontology")
    :example:
        c_book      = <SOME_URI>
        p_rdf_type  = <SOME URI>
        c_class     = <SOME URI>
        add_triple(c_book, p_rdf_type, c_class)
)
    """
    triple = sub + " " + prop + " " + obj + " ."  # construct a triple in turtle format.
    triples_list_to_append.append(triple)         # add the triples_list

def add_prefix_triple(desired_prefix_name, prefix_uri_string, triples_list_to_append=triples_list):  # local function
    """
    Constructs a prefix assertion from given arguments and adds it to triples_list. Is a variant of add_triple function
    (see add_triple function for full docstring).

    :param desired_prefix_name: Enter empty string ("") to specify default prefix (i.e., ":")
    :returns: Adds prefixes to triples_list in the following manner (examples):
        @prefix : <http://clokman.com/ontologies/scientific-research#> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    """
    prefix_triple = "@prefix " + desired_prefix_name + ": <" + prefix_uri_string + "> ." # construct a prefix triple in turtle format.
    triples_list_to_append.append(prefix_triple)                                        # add the triples_list
