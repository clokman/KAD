//important: first value in the array is considered as default value for the property
//this file is visible to the server-side
export default {

  ////////////////////////////////////////////////////////
  //                   PORT NUMBER                      //
  ////////////////////////////////////////////////////////

    // specify which port will be used
    serverPort: [4000],

    ////////////////////////////////////////////////////////
    //                GRAPH LOCATIONS                     //
    ////////////////////////////////////////////////////////

    // Here goes the specification of your SPARQL endpoint.
    // Endpoints are defined per dataset. Therefore, you need to specify your intended graph name within your SPARQL endpoint too.
    // If you aim to use all graphs, you should set the value of graphName to 'default'.
    // ***IMPORTANT***: If no endpoint is found for your dataset, the config for 'generic' will be used.
    // At the moment only endpoint types 'cliopatria', 'virtuoso' , 'sesame', 'blazegraph'
    // and 'stardog' are supported. Use 'endpointType' parameter to specify the endpoint type (default is set to 'virtuoso').
    // If you want to enable reasoning on your triple store, set 'useReasoning' parameter to '1'.

    sparqlEndpoint: {

        // GRAPH #0
        'generic': {      //default / fallback option if nothing else is specified for an endpoint
            host: 'localhost', port: 8890, path: '/sparql', endpointType: 'virtuoso'
            //host: 'http://192.168.1.124', port: 5820, path: 'sr2/query', graphName: 'default', endpointType: 'sparql', useReasoning: 0
        },
        // Note: if graphName is not specified, the identifer used for configuration will be used as graphName
        // Example config for connecting to a Stardog triple store
        // 'http://localhost:5820/testDB/query': {
        //    host: 'localhost', port: 5820, path: '/testDB/query', graphName: 'default', endpointType: 'stardog', useReasoning: 1

        // GRAPH #1 (continues on server.js)
        'localhost/sr2/query': {
            host: 'localhost', port: 5820, path: '/sr2/query', graphName: 'default', endpointType: 'stardog', useReasoning: 1

        // GRAPH #2 (continues on server.js)
        },
        //Example for connecting to a Virtuoso triple store
        'http://dbpedia.org/sparql': {
            host: 'dbpedia.org', port: 80, path: '/sparql', graphName: 'default', endpointType: 'virtuoso'
        },

        // GRAPH #3
        //Example for connecting to a ClioPatria triple store
        'http://localhost:3020/sparql/': {
            host: 'localhost', port: 3020, path: '/sparql/', endpointType: 'ClioPatria'
        }
    },


    ////////////////////////////////////////////////////////
    //                 LOOKUP SERVICES                    //
    ////////////////////////////////////////////////////////

	  // Address of your DBpedia lookup service.
	  dbpediaLookupService: [
        { host: 'lookup.dbpedia.org' }
    ],

	  // Address of your DBpedia lookup service.
    dbpediaSpotlightService: [
        { host: 'www.dbpedia-spotlight.com', port: 80, path: '/en/annotate' }
    ],


    ////////////////////////////////////////////////////////
    //              USERS AND AUTHENTICATION              //
    ////////////////////////////////////////////////////////

    //CAPTCHA CONTINUES HERE (FROM GENERAL.JS/ADDONS)
    // This is used only if you enabled recaptcha feature for user authentication
    // get keys from https://www.google.com/recaptcha
    googleRecaptchaService: {
        siteKey: ['put your google recaptcha site key here...'],
        secretKey: ['put your google recaptcha secret key here...']
    }
};
