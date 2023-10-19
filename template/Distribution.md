# Distribution
If applicable, it defines all the distributions for different dataset for this EJP RD resource.

## Title
The name of the distribution. This is a required field and needs to be unique in this spreadsheet.
> **Warning** This field is `required`, and should be `unique`

## DatasetTitle
The name of the dataset represented by this distribution. Choose a title of a dataset by selecting at dataset title from the 
dropdown list.
> **Warning** This field is `required`

## Description
A description of the distribution.
> **Note** This field is `optional`

## URL
The URL from where the data can be accessed or downloaded.
> **Warning** This field is `required`

## Type
Select either "Access" or "Download" depending on whether the URL will allow you to view the data without downloading it 
or whether you first need to download the data in order to be able to view the data.
> **Warning** This field is `required`

## License
This should contain a URL that provides details regarding the license that is applicable to this distribution.
> **Warning** This field is `required`


## MediaType
If applicable, use the dropdown to select a media type list in the Mediatypes sheet. 

*Example:*
json
> **Note** This field is `optional`

## Publisher
The organisation responsible for making this distribution available. Use the dropdown to select an organisation listed
on the Organisation sheet.
> **Warning** This field is `required`

## IsPartOf
Refers to related resources in which this distribution is physically or logically included. This consists of a list of URLs
separated by commas.
> **Note** This field is `optional`

## AccessRight
Information about who can access the resource or an indication of its security status. This should
point to a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

## ODRLPolicy (in DCAT 2 `odrl:hasPolicy`)
An ODRL conformant policy expressing the rights associated with the resource. This should point to
a URL where this information can be found.

> **Recommendation** Specifying a value for this field is `recommended`

