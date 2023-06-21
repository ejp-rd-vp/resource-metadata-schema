# Catalog
Describes a catalog of datasets, data services, biobanks, patient registries and guidelines. It is possible that a 
catalog can consist of catalogs as well. To be meaningful a catalog must consist of at least 1 dataset, data service,
biobank, patient registry or guideline, or otherwise 1 or more catalogs. 

## Title
The name of the catalog. This is a required field and needs to be unique in this spreadsheet.

> **Warning** This field is `required`, and should be `unique`

## Description
A brief description of the catalog. It can consist of multiple strings.

> **Note** This field is `optional`

## DatasetTitles
A list of 0 or more dataset titles, as defined on the Dataset tab, separated by commas.

> **Note** This field is `optional

## DataServiceTitles
A list of 0 or more data service titles, as defined on the DataService tab, separated by commas.

> **Note** This field is `optional

## BiobankTitles
A list of 0 or more biobank titles, as defined on the BiobankPatientRegistry tab with type Biobank, separated by commas.

> **Note** This field is `optional

## PatientRegistryTitles
A list of 0 or more patient registry titles, as defined on the BiobankPatientRegistry tab with type Patient Registry, 
separated by commas.

> **Note** This field is `optional

## GuidelineTitles
A list of 0 or more guideline titles, as defined on the Guideline tab, separated by commas.

> **Note** This field is `optional

## CatalogTitles
Since Catalogs can be define recursively, a Catalog can consist of catalogs. If a recursive definition is required, 
this columns needs to be filled with a list of CatalogTitles from this tab, that has already been added in earlier rows,
again separated by commas.

> **Note** This field is `optional

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable: indicates that you are requesting to be indexed by the platform
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery: indicates that you have implemented the /individuals interface for Beacon2
> **Warning** This field is `required`
