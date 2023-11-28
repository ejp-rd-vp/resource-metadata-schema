`ejp:PatientRegistry` concept is a custom extension we added to the DCAT2 vocabulary. In our extension we defined `ejp:PatientRegistry` is a subclass of `dcat:Resource`.

### Metadata model figure

<p align="center"> 
    <a href="../images/turtle/patientRegistry.png" target="_blank">
        <img src="../images/turtle/patientRegistry.png"> 
    </a>
</p>


***

### Example rdf (turtle)

```ttl
@prefix : <http://purl.org/ejp-rd/metadata-model/v1/example-rdf/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix ejp:   <https://w3id.org/ejp-rd/vocabulary#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix sio:  <http://semanticscience.org/resource/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ordo: <http://www.orpha.net/ORDO/> .

:patientRegistry a ejp:PatientRegistry ;
  dct:publisher :organisation ;        
  dct:title "Von Hippel-Lindau registry" ;
  ejp:populationCoverage  :population_coverage ;
  dcat:theme  ordo:Orphanet_892 ;
  foaf:page <https://www.uniklinik-freiburg.de/medizin4.html> .

:organisation a foaf:Organisation ;
  dct:title "EKlinik für Innere Medizin IV" ;
  dct:spatial  :location .

:population_coverage  a sio:SIO_001166 ;
  rdfs:label  "Regional" .

:location a dct:Location ;
  dct:title  "Germany" .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="../images/shex/patientRegistry.svg" target="_blank">
        <img src="../images/shex/patientRegistry.svg"> 
    </a>
</p>

***
##### ShEx

``` ShEx
PREFIX : <http://purl.org/ejp-rd/metadata-model/v1/shex/>
PREFIX dcat:  <http://www.w3.org/ns/dcat#>
PREFIX dct:   <http://purl.org/dc/terms/>
PREFIX ejp:   <https://w3id.org/ejp-rd/vocabulary#>
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sio:  <http://semanticscience.org/resource/>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>

:patientRegistryShape IRI {
  a [ejp:PatientRegistry];
  dct:title xsd:string;
  dct:description xsd:string*;
  ejp:populationCoverage @:populationCoverageShape*;
  dcat:theme IRI+;
  dct:publisher @:organisationShape;
  foaf:page IRI*
}

:locationShape IRI {
  a [dct:Location];
  dct:title xsd:string;
  dct:description xsd:string*;
}

:organisationShape IRI {
  a [foaf:Organisation];
  dct:title xsd:string;
  dct:description xsd:string*;
  dct:spatial @:locationShape*;
  foaf:page IRI*
}

:populationCoverageShape IRI {
  a [sio:SIO_001166];
  rdfs:label ["National" "International" "Regional"]
}
```
