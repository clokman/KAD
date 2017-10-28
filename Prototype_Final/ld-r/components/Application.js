/*globals document*/

import React from 'react';
import PropTypes from 'prop-types';
import Nav from './Nav';
import HelpModal from './HelpModal';
import Home from './Home';
import About from './About';
import ApplicationStore from '../stores/ApplicationStore';
import {connectToStores, provideContext} from 'fluxible-addons-react';
import {handleHistory} from 'fluxible-router';

class Application extends React.Component {
    constructor(props, context) {
        super(props, context);
    }
    componentDidUpdate(prevProps) {
        let newProps = this.props;
        if (newProps.ApplicationStore.pageTitle === prevProps.ApplicationStore.pageTitle) {
            return;
        }
        document.title = newProps.ApplicationStore.pageTitle;
    }
    render() {
        var Handler = this.props.currentRoute.handler;
        //render content
        return (
            <div>
                <Nav loading={this.props.ApplicationStore.loading} />
                <Handler />
                <HelpModal />
            </div>
        );
    }
}

Application.contextTypes = {
    getStore: PropTypes.func,
    executeAction: PropTypes.func,
    getUser: PropTypes.func
};

Application = connectToStores(Application, [ApplicationStore], function (context, props) {
    return {
        ApplicationStore: context.getStore(ApplicationStore).getState()
    };
});

Application = handleHistory(Application, {enableScroll: false});

Application = provideContext(Application, { //jshint ignore:line
    getUser: PropTypes.func
});

export default Application;
