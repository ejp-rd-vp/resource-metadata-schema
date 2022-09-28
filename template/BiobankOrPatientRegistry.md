# Biobank or patient registries
Defines all the biobanks and/or patient registries for this EJP RD resource in the case where datasets are about content 
of a rare disease resources such as biobanks and patient registries.

## Title
The name of the biobank or patient registry. This is a required field and needs to be unique in this spreadsheet.

*Used by:*
[Dataset](Dataset.md)`Distribution`
> **Warning** This field is `required`, and should be `unique`

## Description
A description of this biobank or patient registry.
> **Note** This field is `optional`

## PopulationCoverage
Gives an indication of the part of the population covered by this biobank/patient registry. This field is optional. When 
supplied it must consist of one or more of the following values: National, International, Regional. When more than one
value is applicable, it should be separated by pipes (|).

*Example:*
National|International
> **Note** This field is `optional`

## Theme
It consists of 1 or more IRIs separated by pipes (|). When set, it specifies relevant ontology concepts
that classify the biobank or patient registry. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).
> **Warning** This field is `required`

## Publisher
The title of an organisation that has been specified on the [Organisation](Organisation.md) sheet.
> **Warning** This field is `required`

## Webpages
This is a pipe (|) separated list of the URLs to webpages with more information regarding the organisation. Each URL has to
start with http:// or https://.
> **Note** This field is `optional`

## Type
Select either "Biobank" or "Patient registry" depeding on whether this describes a biobank or a patient registry.
> **Warning** This field is `required`

# Example
<table>
  <tr>
   <td><strong>Title</strong></td>
   <td><strong>Description</strong></td>
   <td><strong>PopulationCoverage</strong></td>
   <td><strong>Theme</strong></td>
   <td><strong>Publisher</strong></td>
   <td><strong>Webpages</strong></td>
   <td><strong>Type</strong></td>
  </tr>
  <tr>
   <td>ECEMC: Registry of the Spanish Collaborative Study of Congenital Malformations</td>
   <td>The ECEMC investigates the causes of congenital defects and malformations that are observed in newborn children.</td>
   <td>National</td>
   <td>http://www.orpha.net/ORDO/Orphanet_558|http://purl.obolibrary.org/obo/OMIABIS_0001002</td>
   <td>Unidad de Investigación sobre Anomalías Congénitas</td>
   <td>http://www.fundacion1000.es/ecemc</td>
   <td>ejp:PatientRegistry</td>
  </tr>
</table>
