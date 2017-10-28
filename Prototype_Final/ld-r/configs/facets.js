export default {
    facets: {
        'generic': {
            list: [
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
            ],
            config: {

            }
        },
        //Configuration Manager: change the graph name if you use another name in your general.js config
        // This file is also sepecified in reactor.js and general.js
        // This is where the configuration graph (http://ld-r.org/configurations) is actually configured

        ////////////////////////////////////////////////////////
        //                 META ONTOLOGY                      //
        ////////////////////////////////////////////////////////

        'http://ld-r.org/configurations': {


            list: [
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#scope',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#dataset',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#resource',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#property',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#endpointType',
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#createdBy->[http://ld-r.org/users]http://xmlns.com/foaf/0.1/accountName'
            ],
            config: {
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#type': {
                    objectBrowser: ['TagListBrowser'],
                    position: 1
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#dataset': {
                    shortenURI: 0,
                    position: 3
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#resource': {
                    shortenURI: 0,
                    objectIViewer: ['PrefixBasedView'],
                    position: 4
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#property': {
                    shortenURI: 0,
                    objectIViewer: ['PrefixBasedView'],
                    position: 5
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#scope': {
                    objectIViewer: ['BasicOptionView'],
                    options: [
                        {label: 'Dataset', value: 'D'},
                        {label: 'Resource', value: 'R'},
                        {label: 'Property', value: 'P'},
                        {label: 'Dataset-Resource', value: 'DR'},
                        {label: 'Dataset-Property', value: 'DP'},
                        {label: 'Resource-Property', value: 'RP'},
                        {label: 'Dataset-Resource-Property', value: 'DRP'},
                    ],
                    position: 2
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#endpointType': {
                    position: 6
                },
                'https://github.com/ali1k/ld-reactor/blob/master/vocabulary/index.ttl#createdBy->[http://ld-r.org/users]http://xmlns.com/foaf/0.1/accountName': {
                    label: ['Creator'],
                    position: 7
                }
            }
        },


        ////////////////////////////////////////////////////////
        //          FACETED BROWSER CONFIGURATIONS            //
        ////////////////////////////////////////////////////////

        ////////// Faceted Browser for DBpedia universities //////////

        'http://dbpedia.org/sparql': {
            list: [
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
                'http://dbpedia.org/ontology/country',
                'http://dbpedia.org/property/established'
            ],

            config: {
                'http://dbpedia.org/property/established': {
                    label: ['Established Year']
                },
                'http://dbpedia.org/ontology/country': {
                    objectBrowser: ['TagListBrowser']
                }
            }
        },


        ////////// Faceted Browser for Scientific Research //////////

        'localhost/sr2/query': {
            list: [
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
                'http://clokman.com/ontologies/scientific-research#hasAuthor',
                'http://clokman.com/ontologies/scientific-research#isPublishedOn',
                'http://clokman.com/ontologies/scientific-research#isPublishedBy',
                'http://clokman.com/ontologies/scientific-research#isPublishedOnYear',
                'http://clokman.com/ontologies/scientific-research#isPublishedOnMonth',
                'http://clokman.com/ontologies/scientific-research#hasDOI',
                'http://clokman.com/ontologies/scientific-research#hasISSN',
                'http://clokman.com/ontologies/scientific-research#hasISBN',
                'http://clokman.com/ontologies/scientific-research#isChapterOf',
                'http://clokman.com/ontologies/scientific-research#isAbout'
            ],
            config: {
                'http://clokman.com/ontologies/scientific-research#hasAuthor': {
                    label: ['Author']
                },
                'http://clokman.com/ontologies/scientific-research#isPublishedOn': {
                    label: ['Publication']
                },
                'http://clokman.com/ontologies/scientific-research#isPublishedBy': {
                    label: ['Publisher']
                },
                'http://clokman.com/ontologies/scientific-research#isPublishedOnYear': {
                    label: ['Year']
                },
                'http://clokman.com/ontologies/scientific-research#isPublishedOnMonth': {
                    label: ['Month']
                },
                'http://clokman.com/ontologies/scientific-research#hasDOI': {
                    label: ['DOI']
                },
                'http://clokman.com/ontologies/scientific-research#hasISSN': {
                    label: ['ISSN']
                },
                'http://clokman.com/ontologies/scientific-research#hasISBN': {
                    label: ['ISBN']
                },
                'http://clokman.com/ontologies/scientific-research#isChapterOf': {
                    label: ['Parent Book']
                },
                'http://clokman.com/ontologies/scientific-research#isAbout': {
                    label: ['Topic']
                }
            }
        }
    }
};
