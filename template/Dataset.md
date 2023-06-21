# Dataset
Defines all the datasets for this EJP RD resource.

## Title
The name of the dataset. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
`Distribution`

*Example:*
hPSC-lines
> **Warning** This field is `required`, and should be `unique`

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

## ConformTo
The IRI of the ontology this dataset adheres to and from which concepts are used in defining the Theme for this dataset.
> **Recommendation** Specifying a value for this field is `recommended`

## VPConnection
This property tells the EJP RD Virtual Platform whether this dataset is queryable or only discoverable. If the dataset is
queryable, it is assumed to be discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery
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
When the dataset refers to a biobank or patient registry, it should contain the title of a [biobank or patient registry](BiobankOrPatientRegistry.md)
as defined on BiobankPatientRegistry sheet.
> **Note** This field is `optional`

## Version
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

## Access
A URL where information regarding who is allowed to access this resource is provided.

> **Recommendation** Specifying a value for this field is `recommended`

## AccessType
Select either "ODRL Policy" if the access to this resource is defined compliant to ODRL policy or "Access Information" if
this URL provides access information.

> **Recommendation** Specifying a value for this field is `recommended`