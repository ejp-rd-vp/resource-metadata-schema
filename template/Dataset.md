# Dataset
Defines all the datasets for this EJP RD resource.

## Title
The name of the dataset. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
`Distribution`

## Logo
A graphic representation of this resource.
> **Note** This field is `optional`

*Example:*
hPSC-lines
> **Warning** This field is `required`, and should be `unique`

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
https://w3id.org/ejp-rd/resources/licenses/v1.0/.

> **Warning** This field is `required`

## PersonalData
Set to "true" if the resource onboarded to the Virtual Platform contains personal data, personal data
meaning data related to indentified or identifiable persons (as per GDPR definition), otherwise "false".

## Description
A description of the dataset. It can consist of multiple strings.

*Example:*
hPSCreg is a global registry for human pluripotent stem cell lines (hPSC-lines).
> **Note** This field is `optional`

## Theme
Defines a list of concepts that this dataset deal with. It consists of IRIs separated by commas that specifies 
relevant ontology concepts that classify the dataset. Typically these can be looked up using the 
[Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS). 

*Example:*
http://purl.obolibrary.org/obo/CLO_0037308.
> **Warning** This field is `required`

## ConformsTo
The IRI of the ontology this dataset adheres to and from which concepts are used in defining the Theme for this dataset.
> **Recommendation** Specifying a value for this field is `recommended`

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable: indicates that you are requesting to be indexed by the platform
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery: indicates that you have implemented the /individuals interface for Beacon2
> **Warning** This field is `required`

## License
This should contain a URL that provides details regarding the license that is applicable to this dataset.

*Example:*
https://creativecommons.org/licenses/by/4.0
> **Warning** This field is `required`

## PersonalData
This field is used to indicate whether this dataset deals with personal data or not. If this dataset deals with personal 
data, the value of this field should be "Yes", else "No".

> **Warning** This field is `required`.


## IsRelatedTo
When the dataset refers to a biobank or patient registry, it should contain the title of a [biobank or patient registry](Biobank.md)
as defined on BiobankPatientRegistry sheet.
> **Note** This field is `optional`

## Version (in DCAT 2 `hasVersion`)
Where applicable, it should provide the version as a string of text.

*Example:*
4.11.2
> **Warning** This field is `required`

## Keywords
The list of keywords applicable to this dataset, separated by commas.

*Example:* 
pluripotent|cell lines|stem cell
> **Note** This field is `optional`

## Publisher
The title of the organisation responsible for publishing this dataset. This should be a title of an organisation as given
on the [Organisation sheet](Organisation.md).

*Example:*
Human pluripotent stem cell registry
> **Warning** This field is `required`

## Landing page
The web page from where the dataset can be browsed. The URL has to start with http:// or https://.

*Example:*
https://hpscreg.eu/search?q
> **Note** This field is `optional`.

## Language
A comma separated list of ISO 639-1 two-letter codes for the languages this dataset is provided in.

*Example:*
en,nl the indicate that the dataset is available in English and Dutch/Flemish.

> **Warning** This field is `required`

## AccessRight
Information about who can access the resource or an indication of its security status. This should
point to a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

## ODRLPolicy (in DCAT 2 `odrl:hasPolicy`)
An ODRL conformant policy expressing the rights associated with the resource. This should point to
a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`