import React from 'react';
import classNames from 'classnames/bind';
import BasicIndividualView from './viewer/individual/BasicIndividualView';
import BasicHTMLContentView from './viewer/individual/BasicHTMLContentView';
import BasicImageView from './viewer/individual/BasicImageView';
import BasicIndividualDetailView from './viewer/individual/BasicIndividualDetailView';
import BasicDBpediaView from './viewer/individual/BasicDBpediaView';
import BasicLinkedIndividualView from './viewer/individual/BasicLinkedIndividualView';
import BasicOptionView from './viewer/individual/BasicOptionView';
import PasswordView from './viewer/individual/PasswordView';
import LanguageView from './viewer/individual/LanguageView';
import TwoLetterCountryView from './viewer/individual/TwoLetterCountryView';
import ThreeLetterCountryView from './viewer/individual/ThreeLetterCountryView';
import BasicDateTimeView from './viewer/individual/BasicDateTimeView';
import PrefixBasedView from './viewer/individual/PrefixBasedView';
import ToggleView from './viewer/individual/ToggleView';
import BasicMapView from './viewer/individual/BasicMapView';
import YASQEViewer from './viewer/individual/YASQEViewer';

class ObjectIViewer extends React.Component {
    render() {
        let category = 0,
            propertyPath = [],
            viewer,
            viewerConfig = '',
            extendedViewer,
            extendedViewerConfig = '';
        if (this.props.config) {
            if (this.props.config.extendedOViewer) {
                extendedViewerConfig = this.props.config.extendedOViewer[0];
            }
            if (this.props.config.objectIViewer) {
                viewerConfig = this.props.config.objectIViewer[0];
            }
        }
        if (this.props.spec.extendedViewData) {
            //go to extended view
            switch (extendedViewerConfig) {
                case 'BasicIndividualDetailView':
                    extendedViewer = <BasicIndividualDetailView datasetURI={this.props.datasetURI} spec={this.props.spec} config={this.props.config}/>;
                    break;
                default:
                    extendedViewer = <BasicIndividualDetailView datasetURI={this.props.datasetURI} spec={this.props.spec} config={this.props.config}/>;
            }
        }
        //always go for linked view when it has extensions (and when BasicIndividualView is selected)
        if (this.props.config && this.props.spec.extended && viewerConfig === 'BasicIndividualView') {
            viewerConfig = 'BasicLinkedIndividualView';
            propertyPath = [this.props.resource, this.props.property];
        }
        if (this.props.config && this.props.config.category) {
            category = this.props.config.category;
        }
        //go to normal view
        switch (viewerConfig) {
            case 'BasicIndividualView':
                viewer = <BasicIndividualView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicHTMLContentView':
                viewer = <BasicHTMLContentView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicImageView':
                viewer = <BasicImageView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'YASQEViewer':
                viewer = <YASQEViewer spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicMapView':
                viewer = <BasicMapView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'ToggleView':
                viewer = <ToggleView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'PrefixBasedView':
                viewer = <PrefixBasedView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicDateTimeView':
                viewer = <BasicDateTimeView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicLinkedIndividualView':
                viewer = <BasicLinkedIndividualView datasetURI={this.props.datasetURI} spec={this.props.spec} config={this.props.config} propertyPath={propertyPath} category={category} property={this.props.property}/>;
                break;
            case 'PasswordView':
                viewer = <PasswordView datasetURI={this.props.datasetURI} spec={this.props.spec} config={this.props.config}/>;
                break;
            case 'BasicDBpediaView':
                viewer = <BasicDBpediaView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'LanguageView':
                viewer = <LanguageView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'BasicOptionView':
                viewer = <BasicOptionView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'TwoLetterCountryView':
                viewer = <TwoLetterCountryView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            case 'ThreeLetterCountryView':
                viewer = <ThreeLetterCountryView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
                break;
            default:
                viewer = <BasicIndividualView spec={this.props.spec} config={this.props.config} property={this.props.property}/>;
        }
        //check if it has a blank node value config
        let hideObject = 0;
        if (this.props.config && this.props.config.hasBlankNode && extendedViewer) {
            hideObject = 1;
        }
        let viewerClasses = classNames({
            'ui': true,
            'attached message': this.props.config && !this.props.config.hidePropertyName
        });
        return (
            <div className="ui" ref="objectIViewer" onClick={this.props.onObjectClick} style={{
                'wordBreak': 'break-all',
                'wordWrap': 'break-word'
            }}>
                {hideObject
                    ? <span></span>
                    : <div className={viewerClasses}>
                        {viewer}
                    </div>}
                {extendedViewer}
            </div>
        );
    }
}

export default ObjectIViewer;
