# Distribution
If applicable, it defines all the distributions for different dataset for this EJP RD resource.

## Title `required`, `unique`
The name of the distribution. This is a required field and needs to be unique in this spreadsheet.

## DatasetTitle `required`,
The name of the dataset represented by this distribution. Choose a title of a dataset by selecting at dataset title from the 
dropdown list.

## Description `required`
A description of the distribution.

## URL `required`
The URL from where the data can be accessed or downloaded.

## Type `required`
Select either "Access" or "Download" depending on whether the URL will allow you to view the data without downloading it 
or whether you first need to download the data in order to be able to view the data.

## License `required`
This should contain a URL that provides details regarding the license that is applicable to this distribution.

## Version `required`
It should provide the version of the distribution as a string of text.

## MediaType `optional`
If applicable, use the dropdown to select a media type list in the Mediatypes sheet. 

*Example:*
json

## Publisher `required`
The organisation responsible for making this distribution available. Use the dropdown to select an organisation listed
on the Organisation sheet.

## IsPartOf `optional`
Refers to related resources in which this distribution is physically or logically included. This consists of a list of URLs
separated by pipes (|).