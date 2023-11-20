// configuration for Nuxt

export const SOLR_SELECT_URI='http://flask.datenadler.lan/solr_search';
export const SOLR_SUGGEST_URI='http://flask.datenadler.lan/solr_suggest';
export const SOLR_PICK_URI='http://flask.datenadler.lan/solr_pick';
export const SOLR_ROULETTE_URI='http://flask.datenadler.lan/solr_roulette'

export const MY_URL = 'https://datenadler.lan'
export const FLASK_URL_MESSAGE = 'http://flask.datenadler.lan/send_email'
export const FLASK_URL_PLONE = 'http://flask.datenadler.lan/request_plone'


export const PLONE_UNREACHABLE_MESSAGE = 'Teile des dargestellten Inhalts werden aus dem Plone Backend geladen. ' +
    'Leider scheint das Plone Backend gerade nicht erreichbar zu sein. ' +
    'Bitte versuchen Sie die Seite neu zu laden oder wenden Sie sich an den Admin.';

export const FLASK_UNREACHABLE_MESSAGE = 'Teile des dargestellten Inhalts werden aus dem Flask Backend geladen. ' +
    'Leider scheint das Flask Backend gerade nicht erreichbar zu sein. ' +
    'Bitte versuchen Sie die Seite neu zu laden oder wenden Sie sich an den Admin.';

export const DEFAULT_DISPLAY_AMOUNT_FACET = 10;
