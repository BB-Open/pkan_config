from rdflib.namespace import Namespace
from rdflib.namespace import FOAF, RDF, DCTERMS, SKOS, XSD, RDFS

NAMESPACES = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'csw': 'http://www.opengis.net/cat/csw/2.0.2',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'gco': 'http://www.isotc211.org/2005/gco',
    'gml': 'http://www.opengis.net/gml/3.2',
    'gmx': 'http://www.isotc211.org/2005/gmx',
    'gts': 'http://www.isotc211.org/2005/gts',
    'ogc': 'http://www.opengis.net/ogc',
    'ows': 'http://www.opengis.net/ows',
    'srv': 'http://www.isotc211.org/2005/srv',
    'dcatde': 'http://dcat-ap.de/def/dcatde/',
    'vcard': 'http://www.w3.org/2006/vcard/ns#',
    'adms': 'http://www.w3.org/ns/adms#',
    'locn': 'https://www.w3.org/ns/locn',
    'dct': 'http://purl.org/dc/terms/',
    'inq': 'http://inqbus.de/ns',
    'dcat': 'http://www.w3.org/ns/dcat#',
    'xlink': 'http://www.w3.org/1999/xlink',
    'euvoc': 'http://publications.europa.eu/ontology/euvoc#',
    'sh': 'http://www.w3.org/ns/shacl#',
    'foaf': 'http://xmlns.com/foaf/0.1/',
    'gsp': 'http://www.opengis.net/ont/geosparql#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
}

DCATDE = Namespace('http://dcat-ap.de/def/dcatde/')
LOCN = Namespace('https://www.w3.org/ns/locn')
DCAT = Namespace('http://www.w3.org/ns/dcat#')
ADMS = Namespace('http://www.w3.org/ns/adms#')
VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
GSP = Namespace('http://www.opengis.net/ont/geosparql#')
INQ = Namespace('http://inqbus.de/ns')
EUVOC = Namespace('http://publications.europa.eu/ontology/euvoc#')
DC = Namespace('http://purl.org/dc/elements/1.1/')
SH = Namespace('http://www.w3.org/ns/shacl#')
DCT = DCTERMS