# Guidelines
Defines all the guidelines described by this EJP RD resource.

## Title
The name of the guideline. This is a required field and needs to be unique.

> **Warning** This field is `required`, and should be `unique`.

## Description
A description of this guideline.

> **Warning** This field is `required`

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
[https://w3id.org/ejp-rd/resources/licenses/v1.0/](https://w3id.org/ejp-rd/resources/licenses/v1.0/). Other licenses are:   
[https://creativecommons.org/licenses/](https://creativecommons.org/licenses/),
e.g. [http://creativecommons.org/licenses/by-nc-nd/4.0](http://creativecommons.org/licenses/by-nc-nd/4.0).

> **Warning** This field is `required`

## Theme
Points to an URL that specifies relevant ontology concepts that classify the Biobank. Typically, these can be looked
up using the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4/index)  or [Bioportal](https://bioportal.bioontology.org/).

> **Warning** This field is `required`

## Publisher
Pointer to the Organisation that published
the resource. The range is
foaf:Organisation.

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

## Personal Data
Set to "true" if the resource onboarded to
the Virtual Platform contains personal
data, personal data meaning data
related to identified or identifiable
persons (as per GDPR definition),
otherwise "false". The range is string.

> **Warning** This field is `required`

## Contact Point
Pointer to a Contact Point, Range, vCard

> **Warning** This field is `required`

## Issued
This resource publication date. The
range is xsd:date.

> **Warning** This field is `required`

## Modified
This resource last revision date. The
range is xsd:date.

> **Warning** This field is `required`

## Access Rights
Information about who can access the
resource or an indication of its security status.
This should point to a URL where this
information can be found. We strongly
recommend that access rights are described
as [DUC CCE profile](https://duc.le.ac.uk/).

> **Recommendation** This field is `recommended`

## Logo
A link to the graphic representation
of this resource.

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

## Version
The version indicator (name or
identifier) of a resource. The range
is a rdfs:literal

> **Note** This field is `optional`

## Conforms To
If applicable, it should point to the
URL, an established standard to
which the data within the
described resource conforms (e.g.
MAGE-ML for Microarray data).

> **Note** This field is `optional`

## Keyword
Keywords applicable to this
Biobank

> **Note** This field is `optional`

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

## Identifier
Identifier of this resource. It can be
a link. Range is an xsd:string

> **Note** This field is `optional`





## Logo
A graphic representation of this resource.
> **Note** This field is `optional`

## Description
A description of this guideline.
> **Warning** This field is `required`

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
https://w3id.org/ejp-rd/resources/licenses/v1.0/.

> **Warning** This field is `required`

## PersonalData
Set to "true" if the resource onboarded to the Virtual Platform contains personal data, personal data
meaning data related to indentified or identifiable persons (as per GDPR definition), otherwise "false".

## Theme
It consists of 1 or more IRIs separated by commas. When set, it specifies relevant ontology concepts
that classifies the guideline. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).
> **Warning** This field is `required`

## ConformsTo
If applicable, it should point to the IRI an established standard to which the described resource conforms
> **Recommendation** Specifying a value for this field is `recommended`

## Type
Defines the type of this resource which for the EJP RD Virtual Platform can be one of the following:

- http://purl.org/ejp-rd/vocabulary/VPBeacon2_individuals:  the annotated resource (always a DataService) provides the Beacon2 /individuals interface
- http://purl.org/ejp-rd/vocabulary/VPBeacon2_catalog: the annotated resource (always a DataService) provides the Beacon2 /catalog interface
> **Warning** This field is `required`> **Warning** This field is `required`

## Publisher
The title of an organisation that has been specified on the [Organisation](Organisation.md) sheet.
> **Warning** This field is `required`

## Webpages
This is a comma separated list of the URLs to webpages with more information regarding the organisation. Each URL has to
start with http:// or https://.
> **Note** This field is `optional`

## Language
A comma separated list of ISO 639-1 two-letter codes for the languages this guideline is provided in.

*Example:*
en,nl indicates that this guideline is available in English and Dutch/Flemish.

> **Warning** This field is `required`

## AccessRight
Information about who can access the resource or an indication of its security status. This should
point to a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

## ODRLPolicy (in DCAT 2 `odrl:hasPolicy`)
An ODRL conformant policy expressing the rights associated with the resource. This should point to
a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

## Identifier
A unique identifier of the item. Recommended practice is to identify the resource by means of a string
conforming to an identification system. Examples include International Standard Book Number (ISBN),
Digital Object Identifier (DOI), and Uniform Resource Name (URN). Persistent identifiers should be
provided as HTTP URIs.
> **Warning** This field is `required`

## ContactPoint
Relevant [contact information](ContactPoint.md) for this guideline.
> **Warning** This field is `required`

## Issued
The date on which this guideline was created
> **Warning** This field is `required`

## Modified
The date on which this guideline was updated or same as issue date if it has not been modified.
> **Warning** This field is `required`

## Version
If applicable, it should provide the version of the guideline as a string of text.
> **Note** This field is `optional`