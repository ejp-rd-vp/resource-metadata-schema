[![Build Status](https://travis-ci.org/ejp-rd-vp/resource-metadata-schema.svg?branch=master)](https://travis-ci.org/ejp-rd-vp/resource-metadata-schema)

# Metadata for EJP rare disease patient registries, biobanks and catalogs

As part of the [European Joint Programme (EJP) for Rare Disease](http://www.ejprarediseases.org), we are developing standards for rare disease registries to describe their metadata that will imporve the FAIR-ness of these resources.

The core model is designed to represent data about a rare disease patient and biosample registries. The model is based on and builds on existing standards, such as the [European Rare Disease Registry Infrastructure](https://eu-rd-platform.jrc.ec.europa.eu) and the [Common Data Elements](http://www.erare.eu/sites/default/files/SetCommonData-EU%20RD%20Platform_CDS%20_final.pdf) from the rare disease community and other more generalised standards for data sharing such as the W3C [DCAT vocabulary](https://www.w3.org/TR/vocab-dcat/). We are also working to align with similar schema standarisation efforts such as [RD connect semantic model](https://github.com/LUMC-BioSemantics/Rare-Disease-Semantic-Model), [schema.org](https://schema.org), [bioschemas](https://bioschemas.org), [MIABIS](https://github.com/MIABIS/miabis/wiki) and [GA4GH](https://www.ga4gh.org) (see also [schema blocks](https://schemablocks.org) and [phenopackets](http://phenopackets.org). A proposed semantic model for the Common Data Elements can be found [here](https://github.com/LUMC-BioSemantics/ERN-common-data-elements).


> Status: DRAFT - 16th July, 2019. This is currently a strawman proposal intended to generate discussion and help in developing an early demonstrator.

## JSON Schema overview

You can browse the published schema files at https://ejp-rd-vp.github.io/resource-metadata-schema/.

All the raw JSON schema files can also be found in the [json_schema](json_schema/) directory. The core schema types are:

* [registry.json](json_schema/registry.json) - describes a patient or biosample registry dataset
* [catalog_of_registries.json](json_schema/catalog_of_registries.json) - describes a catalog or registries that links to individual registry datasets

There are also a number of reusable schema modules

* [organisation.json](json_schema/organisation.json) - describes an organisation assoicated to the registry
* [location.json](json_schema/location.json) - describes a location or region that could be associated to an organisation or may be used to describe a recruitment region
* [case.json](json_schema/case.json) - describes a set of patient/cohort cases. This will include information about the number of cases for a given disease and information about the recruitment and inclusiojn criteria
* [vocabulay_code.json](json_schema/vocabulay_code.json) - Used to capture a standard vocabulary code such as Orpha code or ICD code
* [vocabulary_code_system.json](json_schema/vocabulary_code_system.json) - describes a entire coding system such as Orpha or ICD


This diagram illustrates the basic idea of a schema block. Blocks are reusable components and new blocks can be defined that inherit from parent blocks.

![schema](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/master/diagrams/EJP%20schema%20blocks.png?raw=true)

### Example data

An example of the "PCD Registry" entry from the [ERDRI directory of registries](https://eu-rd-platform.jrc.ec.europa.eu/erdridor/) can be seen in [registry-1.json](examples/registry-1.json). Our schema captures the identifier, type and name of the registry. A registry can contain a number of cases that should describe the disease using a fully qualified Orphat code for the disease. Additional information about the organisation who publish and/or maintain the registry can also be caotured.


```
{
  "@id": "https://www.pcdregistry.eu/",
  "@type": "PatientRegistryDataset",
  "name": "PCD Registry",
  "disease_cases": [
    {
      "disease_code": [
        {"@id": "http://www.orpha.net/ORDO/Orphanet_137628"},
        {"@id": "http://www.orpha.net/ORDO/Orphanet_363250"},
        {"@id": "http://www.orpha.net/ORDO/Orphanet_275742"},
        {"@id": "http://www.orpha.net/ORDO/Orphanet_244"},
        {"@id": "http://www.orpha.net/ORDO/Orphanet_98861"}
      ]
    }
  ],
  "publisher": [
    {
      "name": "University Hospital Muenster of the Westfalian University of Muenster (WWU)",
      "location": {
        "city": "D-48149 Muenster",
        "country": "Germany"
      }
    }
   ]
}
```


We dan also describe a catalog of registries like the [ERDRI directory of registries](https://eu-rd-platform.jrc.ec.europa.eu/erdridor/) that links down to individual patient registry records using the `datasets` property.

```
{
  "@id": "https://eu-rd-platform.jrc.ec.europa.eu/erdridor/",
  "@type": "CatalogOfRegistries",
  "name": "European Directory of Registries",
  "publisher": [
    {
      "name": "European Platform on Rare Disease Registration",
      "location": {
        "country": "Germany"
      }
    }
  ],
  "datasets" : [
    "https://www.pcdregistry.eu/", "http://www.reseau-htap.fr/"
  ]
}
```


### RDF + JSON-LD

You can apply the JSON-LD context from [ejp_vocabulary.jsonld](ejp_vocabulary_context.jsonld) to any JSON document to generate an RDF representation. An example of a resource entry in
RDF turtle format is in [erdri_registry_1.ttl](examples/rdf/erdri_registry_1.ttl)

## Use cases

* Provide minimal metadata to describe a rare disease registry or biobank, or a catalog of registries or biobanks. The metadata should
be sufficient to expose data about these resource through the virtual platform
* Provide a uniform way for resources to expose the primary disease using a Orphanet code so that resources can be searched by disease in the virtual platform
* Provide a mechanism to identify resources and harmonise duplicate resources across catalogs
* Provide geographical information so resources can be filtered by country in the VP
* Expose if resources provide metrics about individuals, such as number of cases
* Expose if a resource has access to biological samples, such as tissue or cell ines.
* Expose if the resource has further contact information
* ...
