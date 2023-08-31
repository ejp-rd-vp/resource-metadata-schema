# Data Service
If applicable, it defines all the data services responsible for providing access to the datasets for this EJP RD resource.

## Title
The name of the data service. This is a required field and needs to be unique in this spreadsheet.
> **Warning** This field is `required`, and should be `unique` or when this service serves multiple data
> sets the combinations of data service with datasets needs to be unique.

## Logo
A graphic representation of this resource.
> **Note** This field is `optional`

## PersonalData
Set to "true" if the resource onboarded to the Virtual Platform contains personal data, personal data
meaning data related to indentified or identifiable persons (as per GDPR definition), otherwise "false".

## Description
A human-readable (narrative) description of the functionality and features of the Servie
A description of the services available via the end-points, including their operations, parameters etc.
> **Recommendation** Specifying a value for this field is `recommended`

## EndpointDescription
A machine-readable document defining the API of the service (e.g. in openAPI)
> **Warning** This field is `required` for services that are attached to [Dataset](Dataset.md)
> 
> **Note** This field is `optional` for services that are attached to [Catalog](Catalog.md)
> 
> (this is regulated at the level of policy, not at the level of schema)

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used: 
https://w3id.org/ejp-rd/resources/licenses/v1.0/.

> **Warning** This field is `required`

## PersonalData
This field is used to indicate whether this dataset deals with personal data or not. If this dataset deals with personal
data, the value of this field should be "Yes", else "No".

> **Warning** This field is `required`.

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable: indicates that you are requesting to be indexed by the platform
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery: indicates that you have implemented the /individuals interface for Beacon2
> **Warning** This field is `required`

## EndpointURL
This is the URL that can be used to access this data service. The URL has to start with http:// or https://.
> **Note** This field is `optional`

## DatasetTitle (dcat:servesData)
The name of the dataset to which this service provide access, or, when this service serves multiple datasets,
the list of dataset titles should be provided, separated by commas.

> **Note** This field is `optional`
 
## AccessService
A data service that gives access to the distribution of the dataset

> **Note** This field is `optional`


## Version
If applicable, it should provide the version of the data service (not the version of the data it serves) as a string of text. 
> **Note** This field is `optional`

## Publisher
This is the organisation responsible for this data service. Choose an organisation title from the organisation sheet by
select the title from the dropdown list.
> **Warning** This field is `required`

## ConformsTo
The standard that the output data from the service will conform to - e.g. JSON-LD, or .CSV.
If applicable, it should have a URI as a value, that points to the spec document of that data standard.
> **Recommendation** Specifying a value for this field is `recommended`

## AccessRight
Information about who can access the resource or an indication of its security status. This should
point to a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

## ODRLPolicy (in DCAT 2 `odrl:hasPolicy`)
An ODRL conformant policy expressing the rights associated with the resource. This should point to
a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`


## Identifier
A unique identifier of the item. Recommended practice is to identify the resource by means of a string
conforming to an identification system. Examples include International Standard Book Number (ISBN),
Digital Object Identifier (DOI), and Uniform Resource Name (URN). Persistent identifiers should be
provided as HTTP URIs.
> **Warning** This field is `required`

## ContactPoint
Relevant [contact information](ContactPoint.md) for this dataset.
> **Warning** This field is `required`

## Issued
The date on which this dataset was created
> **Warning** This field is `required`

## Modified
The date on which this dataset was updated or same as issue date if it has not been modified.
> **Warning** This field is `required`