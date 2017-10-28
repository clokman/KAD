import {appFullTitle} from '../configs/general';

export default function loadDatasets(context, payload, done) {
    context.dispatch('LOADING_DATA', {});
    let pageTitle = 'Datasets';
    if(payload.pageTitle){
        pageTitle = payload.pageTitle;
    }
    context.service.read('dataset.datasetsList', payload, {timeout: 20 * 1000}, function (err, res) {
        if (err) {
            context.dispatch('LOAD_DATASETS_FAILURE', err);
        } else {
            context.dispatch('LOAD_DATASETS_SUCCESS', res);
        }
        context.dispatch('UPDATE_PAGE_TITLE', {
            pageTitle: (appFullTitle + ' | '+ pageTitle) || ''
        });
        context.dispatch('LOADED_DATA', {});
        done();
    });
}
