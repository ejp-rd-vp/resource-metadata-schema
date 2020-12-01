### Metadata model figure

<p align="center"> 
    <a href="https://github.com/EBISPOT/ejprd-metadata-models/blob/master/images/vp_model.gif" target="_blank">
        <img src="images/turtle/patientRegistry.png"> 
    </a>
</p>


***

### Example rdf (turtle)

```ttl
@prefix : <http://purl.org/ejp-rd/metadata-model/v1/example-rdf/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix ejp:   <http://purl.org/ejp-rd/vocabulary/> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix sio:  <http://semanticscience.org/resource/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ordo: <http://www.orpha.net/ORDO/> .

:patientRegistry a ejp:PatientRegistry ;
  dct:publisher :2478_organisation ;        
  dct:title "PCD Registry" ;
  ejp:populationCoverage  :population_coverage ;
  dcat:theme  ordo:Orphanet_137628 , ordo:Orphanet_244 ;
  foaf:page <https://eu-rd-platform.jrc.ec.europa.eu/erdridor/register/2478> .

:2478_organisation a foaf:Organisation ;
  dct:title "ErdriDOR_2478_Organisation" ;
  dct:spatial  :location .

:population_coverage  a sio:SIO_001166 ;
  rdfs:label  "International" .

:location a dct:Location ;
  dct:title  "Germany" .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="https://github.com/EBISPOT/ejprd-metadata-models/blob/master/images/vp_model.gif" target="_blank">
        <img src="images/shex/patientRegistry.png"> 
    </a>
</p>

***
##### ShEx

``` ShEx
PREFIX : <http://purl.org/ejp-rd/metadata-model/v1/shex/>
PREFIX dcat:  <http://www.w3.org/ns/dcat#>
PREFIX dct:   <http://purl.org/dc/terms/>
PREFIX ejp:   <http://purl.org/ejp-rd/vocabulary/>
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sio:  <http://semanticscience.org/resource/>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>

:patientRegistryShape IRI {
  a [ejp:PatientRegistry];
  dct:title xsd:string;
  ejp:populationCoverage @:populationCoverageShape;
  dcat:theme IRI+;
  dct:publisher @:organisationShape;
  foaf:page IRI*
}

:locationShape IRI {
  a [dct:Location];
  dct:title xsd:string;
}

:organisationShape IRI {
  a [foaf:Organisation];
  dct:title xsd:string;
  dct:spatial @:locationShape;
  foaf:page IRI*
}

:populationCoverageShape IRI {
  a [sio:SIO_001166];
  rdfs:label xsd:string;
}
```
