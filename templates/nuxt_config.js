// configuration for Nuxt

export const SOLR_SELECT_URI='http://flask.datenadler.de/solr_search';
export const SOLR_SUGGEST_URI='http://flask.datenadler.de/solr_suggest';
export const BASE_URL = 'https://backend.datenadler.de/@search?fullobjects=1';
export const MY_URL = 'https://datenadler.de'
export const FLASK_URL_MESSAGE = 'http://flask.datenadler.de/send_email'

export const PLONE_UNREACHABLE_MESSAGE = 'Teile des dargestellten Inhalts werden aus dem Plone Backend geladen. ' +
    'Leider scheint das Plone Backend gerade nicht erreichbar zu sein. ' +
    'Bitte versuchen Sie die Seite neu zu laden oder wenden Sie sich an den Admin.';

export const FLASK_UNREACHABLE_MESSAGE = 'Teile des dargestellten Inhalts werden aus dem Flask Backend geladen. ' +
    'Leider scheint das Flask Backend gerade nicht erreichbar zu sein. ' +
    'Bitte versuchen Sie die Seite neu zu laden oder wenden Sie sich an den Admin.';