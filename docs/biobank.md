### Metadata model figure

<p align="center"> 
    <a href="https://github.com/EBISPOT/ejprd-metadata-models/blob/master/images/vp_model.gif" target="_blank">
        <img src="images/turtle/biobank.png"> 
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

:biobank a ejp:Biobank ;
  dct:publisher :organisation ;        
  dct:title "Austrian Bone Marrow Donor Registry" ;
  ejp:populationCoverage  :population_coverage ;
  dcat:theme  ordo:Orphanet_171895 ;
  foaf:page <http://www.stammzellspende.at> .

:organisation a foaf:Organisation ;
  dct:title "Fonds Österreichisches Stammzellregister" ;
  dct:spatial  :location .

:population_coverage  a sio:SIO_001166 ;
  rdfs:label  "National" .

:location a dct:Location ;
  dct:title  "Austria" .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="https://github.com/EBISPOT/ejprd-metadata-models/blob/master/images/vp_model.gif" target="_blank">
        <img src="images/shex/biobank.png"> 
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

:biobankShape IRI {
  a [ejp:Biobank];
  dct:title xsd:string;
  ejp:populationCoverage @:populationCoverageShape*;
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
  rdfs:label ["National" "International" "Regional"]
}
```
