'use strict';
import {getHTTPQuery, getHTTPGetURL} from './utils/helpers';
import {getDynamicEndpointParameters} from './utils/dynamicHelpers';
import {authDatasetURI, enableAuthentication, enableEmailNotifications, baseResourceDomain} from '../configs/general';
import {sendMail} from '../plugins/email/handleEmail';
import AdminQuery from './sparql/AdminQuery';
import AdminUtil from './utils/AdminUtil';
import rp from 'request-promise';
/*-------------config-------------*/
let user;
const headers = {'Accept': 'application/sparql-results+json'};
const outputFormat = 'application/sparql-results+json';
/*-----------------------------------*/
let endpointParameters, dg, graphName, datasetURI, query, queryObject, utilObject, HTTPQueryObject;
queryObject = new AdminQuery();
utilObject = new AdminUtil();

export default {
    name: 'admin',
    // At least one of the CRUD methods is Required
    read: (req, resource, params, config, callback) => {
        if (resource === 'admin.userslist') {
            //SPARQL QUERY
            datasetURI = (params.id ? params.id : authDatasetURI[0]);
            if(enableAuthentication){
                if(!req.user){
                    callback(null, {datasetURI: datasetURI, graphName: '', users: []});
                }else{
                    user = req.user;
                    //only super users have access to admin services
                    if(!parseInt(user.isSuperUser)){
                        callback(null, {datasetURI: datasetURI, graphName: '', users: []});
                    }
                }
            }else{
                user = {accountName: 'open'};
            }
            //build http uri
            getDynamicEndpointParameters(user, datasetURI, (endpointParameters)=>{
                graphName = endpointParameters.graphName;
                query = queryObject.getUsers(endpointParameters, graphName);
                //send request
                rp.get({uri: getHTTPGetURL(getHTTPQuery('read', query, endpointParameters, outputFormat)), headers: headers}).then(function(res){
                    callback(null, {
                        datasetURI: datasetURI,
                        graphName: graphName,
                        users: utilObject.parseUsers(res)
                    });
                }).catch(function (err) {
                    console.log(err);
                    callback(null, {datasetURI: datasetURI, graphName: graphName, users: []});
                });
            });

        }else if(resource === 'admin.sendEmailMsg'){
            //SPARQL QUERY
            datasetURI = (params.id ? params.id : authDatasetURI[0]);
            let subject = params.subject;
            let msg = params.msg;
            if(enableAuthentication){
                if(!req.user){
                    callback(null, {});
                }else{
                    user = req.user;
                    //only super users have access to admin services
                    if(!parseInt(user.isSuperUser)){
                        callback(null, {});
                    }
                }
            }else{
                user = {accountName: 'open'};
            }
            //build http uri
            let userList = [];
            getDynamicEndpointParameters(user, datasetURI, (endpointParameters)=>{
                graphName = endpointParameters.graphName;
                query = queryObject.getUsers(endpointParameters, graphName);
                //send request
                rp.get({uri: getHTTPGetURL(getHTTPQuery('read', query, endpointParameters, outputFormat)), headers: headers}).then(function(res){
                    userList = utilObject.parseUsers(res);
                    userList.forEach((node)=>{
                        if(!parseInt(node.isSuperUser)){
                            sendMail('msg', '', node.mbox.replace('mailto:',''), subject, 'Dear '+node.firstName+', \n' + msg , '');
                        }
                    });
                    callback(null, {});
                }).catch(function (err) {
                    console.log(err);
                    callback(null, {});
                });
            });

        }else if(resource === 'admin.others'){
            console.log('other services');
        }

    },
    // other methods
    create: function(req, resource, params, body, config, callback) {
        if (resource === 'admin.datasetEditor') {
            if(enableAuthentication){
                if(!req.user){
                    callback(null, {});
                }else{
                    user = req.user;
                    //only super users have access to admin services
                    if(!parseInt(user.isSuperUser)){
                        callback(null, {});
                    }
                }
            }else{
                user = {accountName: 'open'};
            }
            if(!params.user){
                callback(null, {});
                return 0;
            }
            let bnode = baseResourceDomain[0] + '/editor' + Math.round(+new Date() / 1000);
            datasetURI = authDatasetURI[0];
            getDynamicEndpointParameters(user, datasetURI, (endpointParameters)=> {
                graphName = endpointParameters.graphName;
                query = queryObject.addDatasetEditor(endpointParameters, graphName, params.user, params.dataset, bnode);
                //console.log(query);
                //build http uri
                //send request
                HTTPQueryObject = getHTTPQuery('update', query, endpointParameters, outputFormat);
                rp.post({uri: HTTPQueryObject.uri, form: HTTPQueryObject.params}).then(function(res){
                    callback(null, {});
                }).catch(function (err) {
                    console.log(err);
                    callback(null, {});
                });
            });
        }
    },
    update: (req, resource, params, body, config, callback) => {
        if (resource === 'admin.activateUser') {
            if(enableAuthentication){
                if(!req.user){
                    callback(null, {});
                }else{
                    user = req.user;
                    //only super users have access to admin services
                    if(!parseInt(user.isSuperUser)){
                        callback(null, {});
                    }
                }
            }else{
                user = {accountName: 'open'};
            }
            datasetURI = authDatasetURI[0];
            getDynamicEndpointParameters(user, datasetURI, (endpointParameters)=> {
                graphName = endpointParameters.graphName;

                query = queryObject.activateUser(endpointParameters, graphName, params.resourceURI);
                //build http uri
                //send request
                HTTPQueryObject = getHTTPQuery('update', query, endpointParameters, outputFormat);
                rp.post({uri: HTTPQueryObject.uri, form: HTTPQueryObject.params}).then(function(res){
                    if(enableEmailNotifications){
                        sendMail('userActivation', '', params.email, '', '', '');
                    }
                    callback(null, {});
                }).catch(function (err) {
                    console.log(err);
                    callback(null, {});
                });
            });
        }
    }
    // delete: function(req, resource, params, config, callback) {}
};
