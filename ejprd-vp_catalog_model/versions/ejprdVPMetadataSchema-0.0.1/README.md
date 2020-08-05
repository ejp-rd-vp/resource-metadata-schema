# EJPRD RESOURCES METADATA SCHEMA


Here you will find the *EJPRD Resources Metadata schema* - the JSON schema version of the [EJPRD Resources Metadata schema](https://github.com/ejp-rd-vp/resource-metadata-schema) - a data model for describing EJPRD resources in the virtual platform catalog.

Production
----------
The metadata has six major modules for the catalog resource :
* [catalog_of_registries.json](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/master/docs/catalog_of_registries.json): this describes the catalogs / registries properties of the virtual platform catalogs resource. The catalog properties and description detailed [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.html).


* [Location](https://ejp-rd-vp.github.io/resource-metadata-schema/location.html)

* [Organisation](https://ejp-rd-vp.github.io/resource-metadata-schema/organisation.html)

* [PatientRegistryDataset]()

* [DiseaseCode]()

* [DiseaseCodeSystem]()


# Structure
---------


<table>
  <tr>
   <td><strong>Schema modules</strong>
   </td>
   <td><strong>Description EJPRD resources link</strong>
   </td>
   <td><strong>JSON Schema</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td> catalogs as describe in EJPRD Virtual Platform
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.html)
   </td>
   <td> Catalogs of registries [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.json)
   </td>
   <td> This gives detailed description of the catalogs or registries as one of the resources that are discoverable in the EJPRD VP
   </td>
  </tr>
  <tr>
   <td> Location in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/location.html
   </td>
   <td> Location in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/location.json)
   </td>
   <td> This gives detailed description of the location where EJPRD catalogs or resources are created from e.g. country - Italy
   </td>
  </tr>
  <tr>
   <td> Organisation in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/organisation.html
   </td>
   <td> Organisation in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/organisation.json)
   </td>
   <td> This gives detailed description of the Organisation that is responsible for the EJPRD catalogs or resources e.g. ERDRI
   </td>
  </tr>
  <tr>
   <td> Registries in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/registry.html
   </td>
   <td> Organisation in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/registry.json)
   </td>
   <td> This gives detailed description of the Registries that are discoverable through the EJPRD VP catalogs or resources.
   </td>
  </tr>
</table>
