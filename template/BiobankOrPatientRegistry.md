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
Gives an indication of the part of the population covered by this biobank/patient registry. This field is optional. When 
supplied it must consist of one or more of the following values: National, International, Regional. When more than one
value is applicable, it should be separated by commas.

*Example:*
National|International
> **Note** This field is `optional`

## Theme
It consists of 1 or more IRIs separated by commas. When set, it specifies relevant ontology concepts
that classify the biobank or patient registry. Typically these can be looked up using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) (OLS).
> **Warning** This field is `required`

## Publisher
The title of an organisation that has been specified on the [Organisation](Organisation.md) sheet.
> **Warning** This field is `required`


## PersonalData
This field is used to indicate whether this biobank or patient registry deals with personal data or not. If this
biobank or patient registry deals with personal data, the value of this field should be "Yes", else "No".

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
