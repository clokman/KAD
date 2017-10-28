import React from 'react';
import ObjectIViewer from '../../ObjectIViewer';
import URIUtil from '../../../utils/URIUtil';
import { Checkbox, Segment } from 'semantic-ui-react';

class CheckboxItem extends React.Component {
    constructor(props) {
        super(props);
    }
    checkBox(status) {
        this.props.onCheck(status, this.props.spec.value);
    }
    reClick(e){
        //prevent opening it in new window
        e.preventDefault();
        //like check box click
        this.props.onCheck(status, this.props.spec.value);
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
        let title, c;
        let datasetURI = this.props.datasetURI;
        if(this.props.config && this.props.config.objectIViewer){
            c = this.props.config;
            title = <ObjectIViewer datasetURI={this.props.datasetURI} spec={this.props.spec} config={c}/>;
        }else{
            title = this.props.spec.value;
            if(this.props.spec.label){
                title = this.props.spec.label;
            }else if(this.props.shortenURI && !(this.props.config && this.props.config.shortenURI === 0)){
                title = URIUtil.getURILabel(this.props.spec.value);
            }
            if(this.props.spec.valueType === 'uri'){
                if(this.props.config && this.props.config.hasLinkedValue){
                    if(this.props.config.containerDatasetURI){
                        datasetURI = this.props.config.containerDatasetURI[0];
                    }
                    title = <a className="ui label" href={'/dataset/' + encodeURIComponent(datasetURI) + '/resource/' + encodeURIComponent(this.props.spec.value)} target="_blank"> {title} </a>;
                }else{
                    title = <a style={{color: '#000'}} href={this.props.spec.value} target="_blank" onClick={this.reClick.bind(this)}> {title} </a>;
                }
            }
        }

        if(this.props.checked){
            title = <b> {title} </b>;
        }
        return (
            <div className="ui" ref="checkboxItem">
                <div className="ui horizontal list">
                    <div className="item">
                        <div className="ui basic icon mini button" onClick={this.checkBox.bind(this)}>
                            <Checkbox checked={this.props.checked} />
                        </div>
                    </div>
                    <div className="item">
                        {title}
                    </div>
                    <div className="item">
                        {this.props.total ? <span className="ui small blue circular label"> {this.addCommas(this.props.total)} </span> : ''}
                    </div>
                </div>
            </div>
        );
    }
}

export default CheckboxItem;
