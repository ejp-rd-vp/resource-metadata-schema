### Metadata model figure

<p align="center"> 
    <a href="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/turtle/catalog.png" target="_blank">
        <img src="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/turtle/catalog.png"> 
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

:ErdriDORLocation a dct:Location ;
  dct:title  "Italy" .

:ErdriDOR  a  foaf:Organisation ;
  dct:title "ErdriDOR";
  dct:spatial  :ErdriDORLocation ;
  foaf:page    <https://eu-rd-platform.jrc.ec.europa.eu/erdridor/> .

:CatalogErdriDOR a dcat:Catalog ;
  dct:publisher :ErdriDOR ;
  dct:title "European Directory of Registries" ;
  ejp:PatientRegistry :PatientRegistry_ErdriDOR_2444, :PatientRegistry_ErdriDOR_4505 .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/shex/catalog.png" target="_blank">
        <img src="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/shex/catalog.png"> 
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

:catalogShape IRI {
  a [dcat:Catalog];
  dct:title xsd:string;
  dct:publisher @:organisationShape;
  ejp:PatientRegistry IRI*
}

:locationShape IRI {
  a [dct:Location];
  dct:title xsd:string;
}

:organisationShape IRI {
  a [foaf:Organisation];
  dct:title xsd:string;
  dct:spatial @:locationShape;
  foaf:page IRI
}
```
