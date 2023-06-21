# Data Service
If applicable, it defines all the data services responsible for providing access to the datasets for this EJP RD resource.

## Title
The name of the data service. This is a required field and needs to be unique in this spreadsheet.
> **Warning** This field is `required`, and should be `unique` or when this service serves multiple data
> sets the combinations of data service with datasets needs to be unique.

## Description
A description of this data service.
> **Note** This field is `optional`

## Description
A description of the services available via the end-points, including their operations, parameters etc.
> **Note** This field is `optional`

## License
This should contain a URL that provides details regarding the license that is applicable to this data service.
> **Warning** This field is `required`

## PersonalData
This field is used to indicate whether this dataset deals with personal data or not. If this dataset deals with personal
data, the value of this field should be "Yes", else "No".

> **Warning** This field is `required`.

## VPConnection
This property tells the EJP RD Virtual Platform whether content of this resource is discoverable or whether
the resource is discoverable. The 2 option here are:

- http://purl.org/ejp-rd/vocabulary/VPDiscoverable
- http://purl.org/ejp-rd/vocabulary/VPContentDiscovery
> **Warning** This field is `required`

## EndpointURL
This is the URL that can be used to access this data service. The URL has to start with http:// or https://.
> **Warning** This field is `required`

## DatasetTitle
The name of the dataset to which this service provide access, or, when this service serves multiple datasets,
the list of dataset titles should be provided, separated by commas.

> **Note** This field is `optional`

## Version
If applicable, it should provide the version of the data service (not the version of the data it serves) as a string of text. 
> **Note** This field is `optional`

## Publisher
This is the organisation responsible for this data service. Choose an organisation title from the organisation sheet by
select the title from the dropdown list.
> **Warning** This field is `required`

## ConformTo
If applicable, a URL to the specification this data service implements and adheres to. The URL has to start with http:// or https://.
> **Note** This field is `optional`

## Access
A URL where information regarding who is allowed to access this resource is provided.

> **Recommendation** Specifying a value for this field is `recommended`

## AccessType
Select either "ODRL Policy" if the access to this resource is defined compliant to ODRL policy or "Access Information" if
this URL provides access information.

> **Recommendation** Specifying a value for this field is `recommended`