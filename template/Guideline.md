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


## Theme
It consists of 1 or more IRIs separated by commas. When set, it specifies relevant ontology concepts
that classifies the guideline. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).
> **Warning** This field is `required`

## ConformTo
The IRI of the ontology this dataset adheres to and from which concepts are used in defining the Theme for this dataset.
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

## Access
A URL where information regarding who is allowed to access this resource is provided.

> **Recommendation** Specifying a value for this field is `recommended`

## AccessType
Select either "ODRL Policy" if the access to this resource is defined compliant to ODRL policy or "Access Information" if
this URL provides access information.

> **Recommendation** Specifying a value for this field is `recommended`