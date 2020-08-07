This directory contains the new EJPRD metadata schema version 1.0.0 which has addressed the EJPRD VP metadata using the new [DCAT2 vocabulary](https://www.w3.org/TR/vocab-dcat-2/) and the changes made can be viewed in the [CHANGEME.log](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-1.0.0/docs/CHANGELOG.md) file

# This release (Version 1.0.0)

The EJPRD VP catalog helps to discover all resources such as catalogs, biotools, registries, research paper etc in the context of rare diseases. The EJPRD metadata schema is the minimum metadata required to make the resources discoverable on the EJPRD VP which is designed for rare diseases resources discovery and interoperability.  

This revision of the EJPRD metadata schema [v.0.0.1](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-0.0.1/README.md) has extended the previous version to support use cases and requirements to **welcome the possibility of cataloging other resources in addition to registries, such as BioTools,BioBanks, research papers among [others](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-1.0.0/docs/ejprdVPMetadataSchema-1.0.0_diagrams/ejprd-resources.png) and datasets.** The revision also supports describing relationships between datasets as well as between datasets and other cataloged resources.

DCAT provides RDF classes and properties to allow datasets and data services to be described and included in a catalog. The use of a standard model and vocabulary facilitates the consumption and aggregation of metadata from multiple catalogs, which can:

* increase the discoverability of resources and datasets
* allow federated search for datasets across catalogs in multiple sites

Data described in a catalog can come in many formats, ranging from spreadsheets, through XML and RDF to various specialised formats. DCAT does not make any assumptions about these serialisation formats of the datasets but it does distinguish between the abstract dataset and its different manifestations or distributions.


Additional and specific vocabularies can be used together with DCAT to provide more detailed format-specific information. For example, semantics from the [EJP Ontology](https://github.com/EBISPOT/EJP-Ontology/releases/tag/19-11-2019) can be used within DCAT to express semantics about a dataset.


 Recommendation are marked within the text using "**Added:** new features

 * **Changed:**" sections in the [CHANGEMELOG.md](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-1.0.0/docs/CHANGELOG.md), as well as being described in the README.

![schema](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-1.0.0/docs/ejprdVPMetadataSchema-1.0.0_diagrams/VP_Model.png)
