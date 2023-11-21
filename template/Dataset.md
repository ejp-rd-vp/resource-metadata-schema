# Dataset
DCAT vocabulary already has a concept dcat:Dataset which is a sub-class of
dcat:Resource. We use this concept to describe any rare disease-related dataset.
When a dataset is about the content of rare disease resources such as biobank and
patient registry then we recommend using sio:isrelatedto property to connect the
dataset to its rare disease resource.

## License 
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
[https://w3id.org/ejp-rd/resources/licenses/](https://w3id.org/ejp-rd/resources/licenses/). Other licenses are:   
[https://creativecommons.org/licenses/](https://creativecommons.org/licenses/),
e.g. [http://creativecommons.org/licenses/by-nc-nd/4.0](http://creativecommons.org/licenses/by-nc-nd/4.0).

> **Warning** This field is `required`

## Title
The name of the dataset. This is a required field and needs to be unique in this spreadsheet.

*Example:*
hPSC-lines

> **Warning** This field is `required`, and should be `unique`


## Description
A description of the Dataset.

*Example:*
hPSCreg is a global registry for human pluripotent stem cell lines (hPSC-lines).

> **Warning** This field is `required`

## Theme
Points to an URL that specifies relevant ontology concepts that classify the Biobank. Typically, these can be looked
up using the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/index)  or [Bioportal](https://bioportal.bioontology.org/).

*Example:*
http://purl.obolibrary.org/obo/CLO_0037308.

> **Warning** This field is `required`

## Publisher
Pointer to the Organisation that published the
resource. The range is foaf:Organisation

> **Warning** This field is `required`


## PersonalData
Set to "true" if the resource onboarded to the Virtual Platform contains personal data, personal data
meaning data related to indentified or identifiable persons (as per GDPR definition), otherwise "false".

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


## Landing Page
This a URL to a web page with more
information regarding the Biobank. Any URL
must start with http:// or https://.

*Example:*
https://hpscreg.eu/search?q

> **Recommendation** This field is `recommended`

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

## Keyword
Keywords applicable to this Dataset

> **Note** This field is `optional`

## Logo
A link to the graphic representation
of this resource.

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

*Example:*
4.11.2

> **Note** This field is `optional`

## Conforms To
If applicable, it should point to the
URL, an established standard to
which the data within the
described resource conforms (e.g.
MAGE-ML for Microarray data).

> **Note** This field is `optional`

