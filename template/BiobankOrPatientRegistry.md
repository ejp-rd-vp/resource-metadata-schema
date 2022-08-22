# Biobank or patient registries
Defines all the biobanks and/or patient registries for this EJP RD resource in the case where datasets are about content 
of a rare disease resources such as biobanks and patient registries.

## Title `required`, `unique`
The name of the biobank or patient registry. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
[Dataset](Dataset.md)`Distribution`


## Description `optional`
A description of this biobank or patient registry. This field is optional.

## PopulationCoverage `optional`
Gives an indication of the part of the population covered by this biobank/patient registry. This field is optional. When 
supplied it must consist of one or more of the following values: National, International, Regional. When more than one
value is applicable, it should be separated by pipes (|).

*Example:*
National|International

## Theme `required`
It consists of 1 or more IRIs separated by pipes (|). When set, it specifies relevant ontology concepts
that classify the biobank or patient registry. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).

## Publisher `required`
The title of an organisation that has been specified on the [Organisation](Organisation.md) sheet.

## Webpages `optional`
This is a pipe (|) separated list of the URLs to webpages with more information regarding the organisation. Each URL has to
start with http:// or https://.

## Type `required`
Select either "Biobank" or "Patient registry" depeding on whether this describes a biobank or a patient registry.