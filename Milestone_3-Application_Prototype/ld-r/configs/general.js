export default {

    ////////////////////////////////////////////////////////
    //                     Title                          //
    ////////////////////////////////////////////////////////

    //full page title
    appFullTitle: ['Scientific Research'],
    //short page title
    appShortTitle: ['SR'],


    ////////////////////////////////////////////////////////
    //              DEFAULT DATASET URI                   //
    ////////////////////////////////////////////////////////

    // URI of the default dataset to be viewed/browsed/edited.
    defaultDatasetURI: [''],
    // ***IMPORTANT***: If not set, will consider all existing graph names
    // in 'generic' endpoint as a fallback option.

    ////////////////////////////////////////////////////////
    //        DYNAMIC CONFIGURATION OPTIONS               //
    ///////////////////////////////////////////////////////

    ////////// DYNAMIC SERVER CONFIG ///////////

    //if set, will use the configs stored in a triple store
	  //if set to '1', will use the server configs stored in a triple store.
    enableDynamicServerConfiguration: 1,

	  //if set to '1', will use the reactor configs stored in a triple store.
    enableDynamicReactorConfiguration: 1,

	  //if set to '1', will use the facets configs stored in a triple store.
    enableDynamicFacetsConfiguration: 1,


    ///////// GENERAL CONFIGURATION FOR ALL DATABASES ////////////

    // MANUAL CONFIGURATION
    //graph that stores your configurations
    configDatasetURI: ['http://ld-r.org/configurations'],
    // This file is further sepecified in reactor.js and especially facets.js

    // AUTOMATIC CONFIGURATION
    //will enable/disable auto config
    enableAutomaticConfiguration: 0,


    ///////// DB EDITING ////////////

    //if set, wil allow users to create new datasets
    //only works if enableDynamicReactorConfiguration is set to 1 and triple store allows update qureies
    enableAddingNewDatasets: 1,

    //allows users to annotate datasets using NLP APIs
    enableDatasetAnnotation: 1,

    ////////////////////////////////////////////////////////
    //              USERS AND AUTHENTICATION              //
    ////////////////////////////////////////////////////////

    //the domain name under which basic DYNAMIC resources and USER RESOURCE will be defined
    baseResourceDomain: ['http://ld-r.org'],

    //graph that stores users data, must be loaded beforehand
    //is required if enableAuthentication is set to '1'.
    authDatasetURI: ['http://ld-r.org/users'], // defined further in reactor.js

    //will prevent access if not logged in (
    //If set to '1', will prevent access to datasets unless user is registered and logged in to the system.
    enableAuthentication: 0, // continues on reactor.js (there, a graph of users should be adressed)

    //will allow super users to confirm and activate regiastered users
    enableUserConfirmation: 0, // continues on reactor.js (there, a graph of users should be adressed)

    //if enabled will allow a recaptcha box in the registration form
    //note: if it is enabled, you need to set the key parameteres for recaptcha in the  SERVER.JS file
    useGoogleRecaptcha: 0,

    //will enable email notifications
    //If set to '1', will enable email notifications on new user registration, user account activation, etc.
    enableEmailNotifications: 0,

    //will put all update actions in log folder
    enableLogs: 0,

    //When provided, will track the users on your LD-R instance using Google Analytics.
    googleAnalyticsID: ''


};
