import React from 'react';
import PropTypes from 'prop-types';
//import ReactDOM from 'react-dom';
import {NavLink} from 'fluxible-router';
import URIUtil from '../utils/URIUtil';
import {Popup} from 'semantic-ui-react';

class DatasetHeader extends React.Component {
    constructor(props){
        super(props);
    }
    componentDidMount() {
    }
    addCommas(n){
        let rx = /(\d+)(\d{3})/;
        return String(n).replace(/^\d+/, function(w){
            while(rx.test(w)){
                w = w.replace(rx, '$1,$2');
            }
            return w;
        });
    }
    render() {
        let self = this;
        let dcnf = this.props.config;
        let resourceFocusType = dcnf.resourceFocusType;
        let typeSt, typesLink = [];
        if(resourceFocusType){
            if(!resourceFocusType.length || (resourceFocusType.length && !resourceFocusType[0]) ){
                typeSt = <span className="ui black label"> Everything </span>;
            }else{
                resourceFocusType.forEach(function(uri) {
                    typesLink.push(<a key={uri} className="ui black label" target="_blank" href={uri}> {URIUtil.getURILabel(uri)} </a>);
                });
                typeSt = typesLink;
            }
        }
        let constraintSt, constraints = [];
        if(dcnf.constraint){
            for (let prop in dcnf.constraint){
                constraints.push(URIUtil.getURILabel(prop) + ': ' + dcnf.constraint[prop].join(','));
            }
            constraintSt = constraints.join(' && ');
        }
        let datasetTitle;
        if(this.props.datasetURI){
            datasetTitle = <a href={this.props.datasetURI}> {this.props.datasetURI} </a>;
            if(dcnf && dcnf.datasetLabel){
                datasetTitle = <a href={this.props.datasetURI}> {dcnf.datasetLabel} </a>;
            }
        }
        return (
            <div className="ui" ref="datasetHeader">
                <h3 className="ui header">
                    {this.props.total ? <a target="_blank" href={'/export/NTriples/' + encodeURIComponent(this.props.datasetURI)}><span className="ui big blue circular label">{this.props.searchMode ? this.addCommas(this.props.resourcesLength) + '/' :''}{this.addCommas(this.props.total)}</span></a> : ''} Resources of type {typeSt} in {datasetTitle ? datasetTitle : ' all local datasets'} {dcnf.constraint ? <span><Popup trigger={<i className="ui orange filter icon link "> </i>} content={constraintSt} wide position='bottom center' /></span>: ''}
                </h3>
            </div>
        );
    }
}
DatasetHeader.contextTypes = {
    executeAction: PropTypes.func.isRequired
};
export default DatasetHeader;
