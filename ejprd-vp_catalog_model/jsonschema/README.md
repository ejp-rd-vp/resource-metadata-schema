# EJPRD RESOURCES METADATA SCHEMA


Here you will find the *EJPRD Resources Metadata schema* - the JSON schema version of the [EJPRD Resources Metadata schema](https://github.com/ejp-rd-vp/resource-metadata-schema) - a data model for describing EJPRD resources in the virtual platform catalog.

Production
----------
The metadata has three major modules
* [catalog_of_registries.json](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/master/docs/catalog_of_registries.json): this describes the catalogs / registries properties of the virtual platform catalogs resource. The catalog properties and description detailed [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.html).


* [Location]()

* [Organisation]()

* [PatientRegistryDataset]()

* [DiseaseCode]()

* [DiseaseCodeSystem]()


# Structure
---------
To make catalog_of_registries.json  easy to understand and maintain, it uses JSON schema [definitions and references](https://cswr.github.io/JsonSchema/spec/definitions_references/) for objects, and properties with regex patterns, which are re-used in the schema:  
<p align="center">

Document Schema                 | Description EJPRD resources                                                                               | JSON Schema
----                            | -----------                                                                                               |
1. | catalogs                   | Full description [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.html)  | Catalogs of registries [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.json)
2. | EJPRDdata           |                                                                                                                  |
3. | EJPRDFormat                |  assets                                                                                                   |
4. | EJPRDCatlogsIdType         |                                                                                                           |
5. |  EJPRDdataType             |                                                                                                           |
6. |                            |                                                                                                           |
7. |                            |                                                                                                           |
</p>

Of these, **catalog_of_registries** is the top-level object. **dataType** and **ontologyConcept** are defined but not actually used (they're retained for now in case they find future use).  All the others are definitions that are refered to in multiple places within the schema.
