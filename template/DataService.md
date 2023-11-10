# Data Service
Data services are resources that provide access to data or analytical tools via some
interface. The interface may be machine-readable (I.e., an Application Programming
Interface – API) or via a Web page for humans to interact manually. There are different
conventions for data services on the VP Portal, depending on the “nature” of the service.
Resources that serve via a Web page, must have a landingPage property, while those
that serve via an API must have both an endpointURL and endpointDescription. On the
EJP VP, a service that serves a DCAT Dataset must be connected to a DCAT Distribution
of that Dataset via the dcat:accessService property. A service not serving a dataset (e.g.,
a statistical analysis service, or an ontology lookup service) must be connected to the
top-level DCAT Catalog via the dcat:service property.

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
[https://w3id.org/ejp-rd/resources/licenses/v1.0/](https://w3id.org/ejp-rd/resources/licenses/v1.0/). Other licenses are:   
[https://creativecommons.org/licenses/](https://creativecommons.org/licenses/),
e.g. [http://creativecommons.org/licenses/by-nc-nd/4.0](http://creativecommons.org/licenses/by-nc-nd/4.0).

> **Warning** This field is `required`


## Type 
In the context of a Data Service, if the service
is a Beacon, the range is either dcterms:type
[http://purl.org/ejp-rd/vocabulary/VPBeacon2_individuals](http://purl.org/ejp-rd/vocabulary/VPBeacon2_individuals) or
[http://purl.org/ejp-rd/vocabulary/VPBeacon2_catalog](http://purl.org/ejp-rd/vocabulary/VPBeacon2_catalog).
If the service is anything besides a Beacon, use
one of the children of [EDAM Operation](http://edamontology.org/operation_0004).

> **Warning** This field is `required`

## Title
The name of the Data Service. This is a
required field and needs to be unique.

> **Warning** This field is `required`, and should be `unique`.

## Description
A description of the Data Service.

> **Warning** This field is `required`.

## Personal Data
Set to "true" if the resource onboarded to
the Virtual Platform contains personal
data, personal data meaning data
related to identified or identifiable
persons (as per GDPR definition),
otherwise "false". The range is string.

> **Warning** This field is `required`

## Publisher
Pointer to the Organisation that published the
resource. The range is foaf:Organisation.

> **Warning** This field is `required`

## Theme
Points to an URL that specifies relevant ontology concepts that classify the Biobank. Typically, these can be looked
up using the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/index)  or [Bioportal](https://bioportal.bioontology.org/).

> **Warning** This field is `required`

## Language
An ISO 639-1 two-letter code for the
languages this patient registry is provided
in. Example: en indicates that this patient
registry is available in English. The range is
an xsd:string. The ISO language codes
can be found at:
[https://id.loc.gov/vocabulary/iso639-1.html](https://id.loc.gov/vocabulary/iso639-1.html) and an example:
[en](http://id.loc.gov/vocabulary/iso639-1/en).

> **Warning** This field is `required`

## Contact Point
Pointer to a Contact Point, Range, vCard

> **Warning** This field is `required`

## Access Rights
Information about who can access the
resource or an indication of its security status.
This should point to a URL where this
information can be found. We strongly
recommend that access rights are described
as [DUC CCE profile](https://duc.le.ac.uk/).

> **Recommendation** This field is `recommended`

## Conforms  To
The standard that the output data from
the service will conform to - e.g., JSON-
LD, or .CSV. If applicable, it should have
a URI as a value, that points to the spec
document of that data standard.

> **Recommendation** This field is `recommended`

## Endpoint Description
A machine-readable document
defining the API of the service (e.g., in
openAPI). **This field is required for
services that have an API.** This field is
optional for services that are attached
to Catalogue, or serve via a Web page.

> **Recommendation** This field is `recommended`

## Endpoint URL
The URL to which API requests are sent.
**This field is required for services that
have an API.** This field is optional for
services that are attached to
Catalogue, or serve via a Web page.

> **Recommendation** This field is `recommended`

## Landing Page
The URL to the web page that serves
the data service. **This field is required
for services that do not have an API.**

> **Recommendation** This field is `recommended`

## VPConnection
This property is attached to every
portion of your Metadata record
that you wish the VP to explore
(e.g. Dataset X, Data Service Y, but
NOT Dataset Z). If you do not add
this tag to at least the description of
your resource, you will not be
onboarded.
The range is [http://purl.org/ejp-rd/vocabulary/VPDiscoverable](http://purl.org/ejp-rd/vocabulary/VPDiscoverable).

> **Note** This field is `optional`

## ODRL Policy
An ODRL conformant policy
document (https://www.w3.org/TR/
odrl-model/) expressing the rights
and/or responsibilities associated
with access to and/or use of the
resource. This should point to a URL
where this conformant document
has been published.

> **Note** This field is `optional`

## Logo
A link to the graphic
representation of this resource.

> **Note** This field is `optional`

## Serves Dataset
Used to indicate which dataset
a DataService is serving data
from.
The URL of the dataset to which
this service provides access.
Range dcat:Dataset

> **Note** This field is `optional`


## Keyword
Keywords applicable to this
Biobank

> **Note** This field is `optional`

## Identifier
Identifier of this resource. It can be
a link. Range is an xsd:string

> **Note** This field is `optional`

## Issued
This resource publication date. The
range is xsd:date.

> **Note** This field is `optional`

## Modified
This resource last revision date. The
range is xsd:date.

> **Note** This field is `optional`

## Version
The version indicator (name or
identifier) of a resource. The range
is a rdfs:literal

> **Note** This field is `optional`

