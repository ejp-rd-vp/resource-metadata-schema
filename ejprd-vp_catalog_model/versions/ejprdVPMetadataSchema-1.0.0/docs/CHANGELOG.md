# Changelog for EJPRD Resources MetadataSchema

Description of changes are grouped as follows:

* **Added:** new features

* **Changed:** changes to existing functionality

* **Deprecated:** a once-stable feature that has been removed

* **Removed:** a deprecated feature that has been removed

* **Fixed:** a bug fix

* **Misc:** some miscellaneous other change



# Released
Status: This release is in complaint with DCAT2 based around **five main classes** as the core classes for all EJPRD VP resources [Figure 1](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-1.0.0/diagrams/VP_Model.png):

dcat:Catalog represents a catalog, which is a dataset in which each individual item is a metadata record describing some resource; the scope of dcat:Catalog is collections of metadata about datasets.

dcat:Resource represents a dataset, or other resource that may be described by a metadata record in a catalog. This class is not intended to be used directly, but is the parent class of dcat:Dataset and dcat:Catalog. Member items in a catalog should be members of one of the sub-classes, or of a sub-class of these, or of a sub-class of dcat:Resource defined in a DCAT profile or other DCAT application. dcat:Resource is effectively an extension point for defining a catalog of any kind of resource.

dcat:Dataset represents a dataset which is the collection of data, published or curated by a single organisation. Data comes in many forms including numbers, words, pixels, imagery, sound and other multi-media, and potentially other types, any of which might be collected into a dataset.

Organisation: government agencies or other entities that are responsible for the catalog publication and maintenance

Location: A spatial region or named place.


* **Class: Catalog**
    * 1.1 Property: homepage
    * 1.2 Property: themes
    * 1.3 Property: haspart
    * 1.4 Property: dataset
    * 1.6 Property: catalog



* **Class: Cataloged Resource**
    * 2.1 Property: resource creator
    * 2.2 Property: description
    * 2.3 Property: title
    * 2.4 Property: language
    * 2.5 Property: publisher
    * 2.6 Property: identifier
    * 2.7 Property: theme/category
    * 2.8 Property: type/genre
    * 2.9 Property: landing page


* **Class: Dataset**
    * 3.1 Property: spatial/geographical coverage



* **Class: Organization**


* Class: Location



## Added
This release is focused on the core model designed to represent **data about the EJPRD VP catalogs covering : a rare disease patients, biosample registries, biotools, and research projects**, which are some of the major resources the EJPRD VP catalogs covers.

## Misc

This is compliance with the  (DCAT1 standard)[https://www.w3.org/TR/2014/REC-vocab-dcat-20140116/] for catalogs descriptions.
