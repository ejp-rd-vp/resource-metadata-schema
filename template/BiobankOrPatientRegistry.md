# Biobank or patient registries
Defines all the biobanks and/or patient registries for this EJP RD resource in the case where datasets are about content 
of a rare disease resources such as biobanks and patient registries.

## Title
The name of the biobank or patient registry. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
[Catalog](Catalog.md)
> **Warning** This field is `required`, and should be `unique`

## Logo
A graphic representation of this resource.
> **Note** This field is `optional`

## Description
A description of this biobank or patient registry.
> **Note** This field is `optional`

## PopulationCoverage
Gives an indication of the part of the population covered by this biobank/patient registry. This field must have 1 of 
the following values: "National", "International", "Regional" or "European". 
> **Warning** This field is `required`


## Theme
It consists of 1 or more IRIs separated by commas. When set, it specifies relevant ontology concepts
that classify the biobank or patient registry. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).
> **Warning** This field is `required`

## Publisher
The title of an organisation that has been specified on the [Organisation](Organisation.md) sheet.
> **Warning** This field is `required`

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
https://w3id.org/ejp-rd/resources/licenses/v1.0/.

> **Warning** This field is `required`


## PersonalData
Set to "true" if the resource onboarded to the Virtual Platform contains personal data, personal data 
meaning data related to indentified or identifiable persons (as per GDPR definition), otherwise "false".


> **Warning** This field is `required`.

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether 
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable: indicates that you are requesting to be indexed by the platform
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery: indicates that you have implemented the /individuals interface for Beacon2
> **Warning** This field is `required`


## Webpages
This is a commas separated list of the URLs to webpages with more information regarding the organisation. Each URL has to
start with http:// or https://.
> **Note** This field is `optional`

## Type
Select either "Biobank" or "Patient registry" depending on whether this describes a biobank or a patient registry.
> **Warning** This field is `required`

## Keywords
The list of keywords applicable to this biobank or patient registry, separated by commas.

> **Note** This field is `optional`

## Language
A comma separated list of ISO 639-1 two-letter codes for the languages this biobank or patient registry is provided in.

*Example:*
en,nl indicates that this biobank or patient registry is available in English and Dutch/Flemish.

> **Warning** This field is `required`

## Access
A URL where information regarding who is allowed to access this resource is provided.

> **Recommendation** Specifying a value for this field is `recommended`

## AccessType
Select either "ODRL Policy" if the access to this resource is defined compliant to ODRL policy or "Access Information" if
this URL provides access information.

> **Recommendation** Specifying a value for this field is `recommended`

