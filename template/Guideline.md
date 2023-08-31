# Guidelines
Defines all the guidelines described by this EJP RD resource.

## Title
The name of the guideline. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
[Catalog](Catalog.md)
> **Warning** This field is `required`, and should be `unique`

## Logo
A graphic representation of this resource.
> **Note** This field is `optional`

## Description
A description of this guideline.
> **Note** This field is `optional`

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

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable: indicates that you are requesting to be indexed by the platform
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery: indicates that you have implemented the /individuals interface for Beacon2
> **Warning** This field is `required`

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