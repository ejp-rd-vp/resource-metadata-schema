### Metadata model figure

<p align="center"> 
    <a href="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/turtle/location.png" target="_blank">
        <img src="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/turtle/location.png"> 
    </a>
</p>


***

### Example rdf (turtle)

```ttl
@prefix : <http://purl.org/ejp-rd/metadata-model/v1/example-rdf/> .
@prefix dct:   <http://purl.org/dc/terms/> .
  
:ErdriDORLocation a dct:Location ;
  dct:title  "Italy" .
```

***

### Validation artifacts 

##### ShEx figure

<p align="center"> 
    <a href="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/shex/location.png" target="_blank">
        <img src="https://github.com/rajaram5/resource-metadata-schema/blob/develop/images/shex/location.png"> 
    </a>
</p>

***
##### ShEx

``` ShEx
PREFIX : <http://purl.org/ejp-rd/metadata-model/v1/shex/>
PREFIX dct:   <http://purl.org/dc/terms/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

:locationShape IRI {
  a [dct:Location];
  dct:title xsd:string;
}
```
