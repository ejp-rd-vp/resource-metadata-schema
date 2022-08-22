# Dataset
Defines all the datasets for this EJP RD resource.

## Title* `required`, `unique`
The name of the dataset. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
`Distribution`

*Example:*
hPSC-lines

## Description* `required`
A description of the dataset.

*Example:*
hPSCreg is a global registry for human pluripotent stem cell lines (hPSC-lines).

## Theme `optional`
This property is optional. It consists of IRIs separated by pipes (|). When set, it specifies relevant ontology concepts
that classify the dataset. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).

*Example:*
http://purl.obolibrary.org/obo/CLO_0037308.

## License* `required`
This should contain a URL that provides details regarding the license that is applicable to this dataset.

*Example:*
https://creativecommons.org/licenses/by/4.0

## IsRelatedTo `optional`
When the dataset refers to a biobank or patient registry, it should contain the title of a [biobank or patient registry](BiobankOrPatientRegistry.md)
as defined on BiobankPatientRegistry sheet.

## Version `optional`
Where applicable, it should provide the version as a string of text.

*Example:*
4.11.2

## Keywords `optional`
The list of keywords applicable to this dataset, separated by pipes (|).

*Example:* 
pluripotent|cell lines|stem cell

## Publisher `required`
The title of the organisation responsible for publishing this dataset. This should be a title of an organisation as given
on the [Organisation sheet](Organisation.md).

*Example:*
Human pluripotent stem cell registry

## Landing page `required`
The web page from where the dataset can be browsed. The URL has to start with http:// or https://.

*Example:*
https://hpscreg.eu/search?q
