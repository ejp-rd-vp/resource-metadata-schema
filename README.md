# Metadata for EJP rare disease registries, biobanks and catalogs

We are developing minimal schemas for rare disease resources to expose metadata to the EJP virtual platform (VP).
The schemas will be published as JSON schemas with a semantic mapping to standard vocabularies provided using JSON-LD.

The core model is designed to represent data about a rare disease resource, these include rare disease registries, biobanks, expert networks and catalog of rare disease resources. The model is based on and builds from the
the W3C DCAT vocabulary for describing a data catalogs and datasets.

## Resource level JSON schema

The primary JSON schema for a resource is described in [rd_resource_metadata.json](rd_resource_metadata.json).

A simplified representation of the same data in CSV format is in [rd_resource_metadata.csv](rd_resource_metadata.csv).


### Example data

An example instance of a resource level metadata [taken from Orphanet](https://www.orpha.net/consor4.01/www/cgi-bin/Directory_Institutions.php?lng=EN&data_id=24435&title=Selbsthilfegruppe%20Ektodermale%20Dysplasie&data_type=Test) can be seen in [orphanet_24435.json](examples/orphanet_24435.json).

### RDF + JSON-LD

You can apply the JSON-LD context from [rd_resource_metadata.jsonld](rd_resource_metadata.jsonld) to any JSON document to generate an RDF representation. An example of a resource entry in
RDF turtle format is in [orphanet_24435.ttl](examples/orphanet_24435.ttl)

## Use cases



* Provide minimal metadata to describe a rare disease registry or biobank, or a catalog of registries or biobanks. The metadata should
be sufficent to expose data aboutthese resource through the virtual platform
* Provide a uniform way for resources to expose the primary disease using a Orphanet code so that resources can be searched by disease in the virtual platform
* Provide a mechanism to identify resources and harmonise duplicate resources across catalogs
* Provide geographical infomation so resources can be filtered by country in the VP
* Expose if resources contain data about individuals with a rare disease e.g. a patient registry
* Expose if resources provide metrics about individuals, such as number of cases
* Expose if a resource has access to biological samples, such as tissue or cell ines.
* Expose if the resource has further contact information
* ...
