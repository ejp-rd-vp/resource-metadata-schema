`dcat:Resource` is a generic concept that was added to the DCAT2 vocabulary. In our metadata model we extended `dcat:Resource` concept with Rare disease specific concepts like `Biobank`, `Patient registry`.

#### Note
Please avoid using `dcat:Resource` typing for your document. Unless the concept that your looking for is not available in our DCAT2 extension.  


### Metadata model figure

<p align="center"> 
    <a href="../images/turtle/biobank.png" target="_blank">
        <img src="../images/turtle/resource.png"> 
    </a>
</p>


***

### Example rdf (turtle)

```ttl
@prefix : <http://purl.org/ejp-rd/metadata-model/v1/example-rdf/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ordo: <http://www.orpha.net/ORDO/> .

:resource a dcat:Resource ;
  dct:publisher :organisation ;        
  dct:title "An example resource" ;
  dct:description "This is a example of a resource";
  dcat:theme  ordo:Orphanet_171895 ;
  foaf:page <http://www.stammzellspende.at> .

:organisation a foaf:Organisation ;
  dct:title "Fonds Österreichisches Stammzellregister" ;
  dct:spatial  :location .

:location a dct:Location ;
  dct:title  "Austria" .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="../images/shex/biobank.png" target="_blank">
        <img src="../images/shex/resource.png"> 
    </a>
</p>

***
##### ShEx

``` ShEx
PREFIX : <http://purl.org/ejp-rd/metadata-model/v1/shex/>
PREFIX dcat:  <http://www.w3.org/ns/dcat#>
PREFIX dct:   <http://purl.org/dc/terms/>
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>

:resourceShape IRI {
  a [dcat:Resource];
  dct:title xsd:string;
  dct:description xsd:string*;
  dcat:theme IRI+;
  dct:publisher @:organisationShape;
  foaf:page IRI*
}

:organisationShape IRI {
  a [foaf:Organisation];
  dct:title xsd:string;
  dct:description xsd:string*;
  dct:spatial @:locationShape;
  foaf:page IRI*
}

:locationShape IRI {
  a [dct:Location];
  dct:title xsd:string;
  dct:description xsd:string*;
}

```
