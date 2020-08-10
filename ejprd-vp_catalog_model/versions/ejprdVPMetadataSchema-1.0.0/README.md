# EJPRD RESOURCES METADATA SCHEMA


Here you will find the *EJPRD Resources Metadata schema* - the JSON schema version of the [EJPRD Resources Metadata schema](https://github.com/ejp-rd-vp/resource-metadata-schema) - a data model for describing EJPRD resources in the virtual platform catalog.

Production
----------
The metadata has seven major schemas for the catalog resource :
* [Catalog of Registries](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/master/docs/catalog_of_registries.json): this describes the catalogs / registries properties of the virtual platform catalogs resource. The catalog properties and description detailed [here](https://ejp-rd-vp.github.io/resource-metadata-schema/catalog_of_registries.html).


* [Location](https://ejp-rd-vp.github.io/resource-metadata-schema/location.html).

* [Organisation](https://ejp-rd-vp.github.io/resource-metadata-schema/organisation.html).

* [Code](https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code.html).

* [Coding System](https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code_system.html).

* [Case or observation](https://ejp-rd-vp.github.io/resource-metadata-schema/case.html).

* [Rare disease registry dataset](https://ejp-rd-vp.github.io/resource-metadata-schema/registry.html).


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
   <td> Registries schema in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/registry.json)
   </td>
   <td> This gives detailed description of the Registries that are discoverable through the EJPRD VP catalogs or resources.
   </td>
  </tr>
  <tr>
   <td> Code schema in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code.html
   </td>
   <td> Code in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code.json)
   </td>
   <td> This gives detailed description of a code from a coding system, controlled vocabulary or ontology that are discoverable through the EJPRD VP catalogs or resources.
   </td>
  </tr>
  <tr>
   <td> Coding system schema in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code_system.html
   </td>
   <td> Coding system schema in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/vocabulary_code_system.json)
   </td>
   <td> This gives detailed description of the systems for coding, controlled vocabulary or ontology that are discoverable through the EJPRD VP catalogs or resources.
   </td>
  </tr>
  <tr>
   <td> Case or observation Schema schema in EJPRD metadata resources
   </td>
   <td>Full description https://ejp-rd-vp.github.io/resource-metadata-schema/case.html
   </td>
   <td> Case or observation Schema schema in JSON [here](https://ejp-rd-vp.github.io/resource-metadata-schema/case.json)
   </td>
   <td> This gives detailed description of the systems for coding, controlled vocabulary or ontology that are discoverable through the EJPRD VP catalogs or resources.
   </td>
  </tr>
</table>



# Examples

<table>
  <tr>
   <td><strong>Type of Schema</strong>
   </td>
   <td><strong>Schema</strong>
   </td>
   <td><strong>Example</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td> ERDRI Catalogs
   </td>
   <td> https://ejp-rd-vp.github.io/resource-metadata-schema/registry.json
   </td>
   <td> https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/examples/erdri_catalog.json
   </td>
   <td> This schema decribes the properties of the ERDRI registries : **ID** , **Type**, **name**, **publisher -- (name of the publisher, location of the publisher, country where the publisher is located)**, **dataset**.
   </td>
  </tr>
  <tr>
   <td> Registry
   </td>
   <td> https://ejp-rd-vp.github.io/resource-metadata-schema/registry.json
   </td>
   <td> https://github.com/ejp-rd-vp/resource-metadata-schema/blob/dev-branch/ejprd-vp_catalog_model/versions/ejprdVPMetadataSchema-0.0.1/examples/registry-1.json
   </td>
   <td> This schema describes the properties of the ERDRI registries : **ID** , **Type**, **name**, **publisher -- (name of the publisher, location of the publisher, country where the publisher is located)**.
   </td>
  </tr>
 </table>

# Validating your metadata against the schema

Validation of RDF can be done using the W3C validator: https://www.w3.org/RDF/Validator/

**Note**: This is for validation of data about registries and registry catalogues.


The main schema diagram [here](https://raw.githubusercontent.com/ejp-rd-vp/resource-metadata-schema/master/diagrams/vp_model.gif).

* The ShEx file for validation :

```ShEx
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sh: <http://www.w3.org/ns/shacl#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ejp-s: <http://purl.org/ejp-rd/metadata/shapes/>
prefix ejp: <http://purl.org/ejp-rd/vocabulary/>
prefix dct: <http://purl.org/dc/terms/>
prefix dcat: <http://www.w3.org/ns/dcat#>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix umbel: <http://umbel.org/umbel#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix vcard: <http://www.w3.org/2006/vcard/ns#>

ejp-s:CatalogOfRegistriesShape IRI
// rdfs:label "CatalogOfRegistries Shape"
{
    rdf:type [ejp:CatalogOfRegistries] ? ;
    dct:title xsd:string ?
         // rdfs:label "name"
         // rdfs:comment "a name or short description for the catalog"@en
         ;
    dct:description xsd:string ?
        // rdfs:label "description"
        // rdfs:comment "A description for the catalog"@en
        ;
    foaf:homepage xsd:string ?
         // rdfs:label "homepage"
         // rdfs:comment "The primary URL for the homepage of the catalog"@en
         ;
    dct:publisher @ejp-s:OrganisationShape *
         // rdfs:label "Organization"
         // rdfs:comment "The organisation that published a catalog of registries."@en
         ;
    dcat:dataset @ejp-s:RegistryDatasetShape *
         // rdfs:label "datasets"
         // rdfs:comment "Link to the patient registry datasets."@en
         ;
}


ejp-s:RegistryDatasetShape IRI
// rdfs:label "Patient or biobank Registry Dataset"
{
  rdf:type [ejp:PatientRegistryDataset ejp:BiobankRegistryDataset] ?
    // rdfs:label "@type"
    // rdfs:comment "the primary type for this registry"
    ;
  dct:title xsd:string ?
       // rdfs:label "name"
       // rdfs:comment "a name or short description for the registry"@en
       ;
  dct:description xsd:string ?
      // rdfs:label "description"
      // rdfs:comment "A description for the registry"@en
      ;
  foaf:homepage xsd:string ?
       // rdfs:label "homepage"
       // rdfs:comment "The primary URL for the homepage of the registry"@en
       ;
  ejp:population_coverage @ejp-s:LocationShape *
    // rdfs:label "PopulationCoverage"
    // rdfs:comment "The country from which the patients in the dataset come from."@en;
  dcat:theme @ejp-s:DiseaseCodeShape *
    // rdfs:label "DiseaseCode"
    // rdfs:comment "The disease code."@en ;
  dct:publisher @ejp-s:OrganisationShape *
    // rdfs:label "Organisation"
    // rdfs:comment "The organisation that published a catalog of registries."@en ;
}

ejp-s:DiseaseCase
{
  ejp:numberOfCases xsd:int ?;
  ejp:inclusion_exclusion_criteria xsd:string ? ;
  ejp:recruitment_area @ejp-s:LocationShape ? ;
  umbel:relatesToDisease @ejp-s:DiseaseCodeShape *
    // rdfs:label "DiseaseCode"
    // rdfs:comment "The disease code."@en ;
}


ejp-s:DiseaseCodeShape IRI
// rdfs:label "DiseaseCode"
{
  rdf:type [skos:Concept] ? ;
  dct:title xsd:string ?
       // rdfs:label "name"
       // rdfs:comment "a name for the disease concept"@en
       ;
 skos:inConceptSchema @ejp-s:DiseaseCodeSystem ?
    // rdfs:label "PopulationCoverage"
    // rdfs:comment "The country from which the patients in the dataset come from."@en
    ;
}

ejp-s:DiseaseCodeSystem IRI
// rdfs:label "DiseaseCodeSystem"
{
  rdf:type [skos:ConceptScheme] ?;
  dct:title xsd:string ?
       // rdfs:label "name"
       // rdfs:comment "a name or short description for the coding system"@en
       ;

}


ejp-s:OrganisationShape
{
  dct:title xsd:string
       // rdfs:label "name"
       // rdfs:comment "a name or short description for the registry"@en
       ;
  dct:description xsd:string ?
      // rdfs:label "description"
      // rdfs:comment "A description for the registry"@en
      ;
  foaf:homepage xsd:string ?
       // rdfs:label "homepage"
       // rdfs:comment "The primary URL for the homepage of the registry"@en
       ;

  dct:spatial @ejp-s:LocationShape ?
        // rdfs:label "Location"
        // rdfs:comment "The country where the organisation is situated."@en
        ;
}

ejp-s:LocationShape
{
  vcard:country-name xsd:string ?
    // rdfs:label "country"
    // rdfs:comment "The name of a country"
    ;
  vcard:locality xsd:string ?
    // rdfs:label "city"
    // rdfs:comment "The locality (e.g. city or town) associated with the address of the object "
    ;
  vcard:region xsd:string ?
    // rdfs:label "region"
    // rdfs:comment "The region (e.g. state or province) associated"
    ;
}

```

* The Shex Constrains

* [Here](https://github.com/ejp-rd-vp/resource-metadata-schema/blob/master/validation_vp_model/metadata_model.shex).


```ShEx

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ejp-s: <http://purl.org/ejp-rd/metadata/shapes/> .
@prefix ejp: <http://purl.org/ejp-rd/vocabulary/> .
@prefix dct: <http://purl.org/dc/terms#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ejp-s:CatalogOfRegistriesShape
    a rdfs:Class, sh:NodeShape ;
    sh:nodeKind sh:IRI;
    sh:targetClass ejp:CatalogOfRegistries ;
    rdfs:label "CatalogOfRegistries" ;
    rdfs:subClassOf rdfs:Resource ;

    sh:property [
        sh:path dct:publisher ;
        sh:name "Organisation" ;
        sh:description "The organisation that published a catalog of registries." ;
        sh:class ejp:Organisation;
        sh:node ejp-s:OrganisationShape ;
        sh:maxCount 1 ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcat:dataset ;
        sh:name "patientRegistryDataset" ;
        sh:description "A patient registry dataset." ;
        sh:class ejp:PatientRegistryDataset;
        sh:node ejp-s:PatientRegistryDatasetShape;
        sh:minCount 1 ;
    ] .

ejp-s:OrganisationShape
    a rdfs:Class, sh:NodeShape ;
    sh:nodeKind sh:IRI;
    sh:targetClass ejp:Organisation ;
    rdfs:label "Organisation" ;
    rdfs:subClassOf rdfs:Resource ;

    sh:property [
        sh:path dct:spatial ;
        sh:name "Location" ;
        sh:description "The country where the organisation is situated." ;
        sh:class ejp:Location;
        sh:node ejp-s:LocationShape ;
        sh:maxCount 1 ;
        sh:minCount 1 ;
    ] .

ejp-s:PatientRegistryDatasetShape
    a rdfs:Class, sh:NodeShape ;
    sh:nodeKind sh:IRI;
    sh:targetClass ejp:PatientRegistryDataset ;
    rdfs:label "PatientRegistryDataset" ;
    rdfs:subClassOf rdfs:Resource ;

    sh:property [
        sh:path ejp:populationCoverage ;
        sh:name "PopulationCoverage" ;
        sh:description "The country from which the patients in the dataset come from." ;
        sh:class ejp:Location;
        sh:node ejp-s:LocationShape ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcat:theme ;
        sh:name "DiseaseCode" ;
        sh:description "The disease code." ;
        sh:node ejp-s:DiseaseCodeShape ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dct:publisher ;
        sh:name "Organisation" ;
        sh:description "The organisation that published a catalog of registries." ;
        sh:class ejp:Organisation;
        sh:node ejp-s:OrganisationShape ;
        sh:maxCount 1 ;
        sh:minCount 1 ;
    ] .

ejp-s:DiseaseCodeShape
    a rdfs:Class, sh:NodeShape ;
    sh:nodeKind sh:IRI;
    sh:targetClass ejp:DiseaseCode ;
    rdfs:label "DiseaseCode" ;
    rdfs:subClassOf rdfs:Resource ;

    sh:property [
        sh:path skos:inConceptSchema ;
        sh:name "PopulationCoverage" ;
        sh:description "The country from which the patients in the dataset come from." ;
        sh:node ejp:DiseaseCodeSystem ;
        sh:maxCount 1 ;
        sh:minCount 1 ;
    ] .


ejp-s:LocationShape
    a rdfs:Class, sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ejp:Location ;
    rdfs:label "Localtion" ;
    rdfs:subClassOf rdfs:Resource .

```
