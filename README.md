# Metadata for EJP rare disease registries and catalogs

We are developing minimal schemas for rare disease resources to expose metadata to the EJP virtual platform.
The schemas will be published as JSON schemas with a semantic mapping to standard vocabularies provided using JSON-LD.

The core model is designed to represent data about a rare disease resource, these include rare disease registries, biobanks, expert networks and catalog of rare disease resources. The model is based on and builds from the
the W3C DCAT vocabulary for describing a data catalogs and datasets.

## Resource level schema

The primary JSON schema for a resource is described in [resource_level_metadata.json].
A simplified representation of the same data in CSV format is in [resource_level_metadata.csv].


### Example

An example instance of a resource level metadata taken from Orphanet can be seen in [examples/orphanet_24435.json].

### JSON-LD

You can apply the JSON-LD context from [resource_level_metadata.jsonld] to any JSON document to generate an RDF representation. An example of a resource entry in
RDF turtle format is in [examples/orphanet_24435.ttl]
