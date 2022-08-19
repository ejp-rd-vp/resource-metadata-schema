# Dataset
Defines all the datasets for this EJP RD resource.

## Title* `Required`, `Unique`
The name of the dataset. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
`Distribution`

*Example:*
hPSC-lines

## Description* `Required`
A description of the dataset.

*Example:*
hPSCreg is a global registry for human pluripotent stem cell lines (hPSC-lines).

## Theme `Optional`
This property is optional. It consists of IRIs separated by commas. When set, it specifies relevant ontology concepts
that classify the dataset. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).

*Example:*
http://purl.obolibrary.org/obo/CLO_0037308.

## License* `Required`
This should contain a URL that provides details regarding the license that is applicable to this dataset.

*Example:*
https://creativecommons.org/licenses/by/4.0

## Is related to `Optional`
When the dataset refers to a biobank or patient registry, it should contain the title of a [biobank or patient registry](BiobankOrPatientRegistry.md)
as defined on BiobankPatientRegistry sheet.

## Version `optional`
Where applicable, it should provide the version as a string of text.

*Example:*
4.11.2

## Keywords
The list of keywords applicable to this dataset, separated by commas.

*Exmaple:* 
pluripotent, cell lines, stem cell

## Publisher
## Landing page
https://hpscreg.eu/search?q
