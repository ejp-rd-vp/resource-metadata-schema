# Distribution
A distribution is a representation of your data. You can have as many distributions as
needed of a dataset. For example, one distribution in .csv, another one in .json, etc.

## License
This should contain a URL that provides details regarding the license that is applicable to this resource.
If no suitable license can be provided, then the default license should be used:
[https://w3id.org/ejp-rd/resources/licenses/v1.0/](https://w3id.org/ejp-rd/resources/licenses/v1.0/). Other licenses are:   
[https://creativecommons.org/licenses/](https://creativecommons.org/licenses/),
e.g. [http://creativecommons.org/licenses/by-nc-nd/4.0](http://creativecommons.org/licenses/by-nc-nd/4.0).

> **Warning** This field is `required`


## Title
The name of the Distribution. This is a required
field and needs to be unique.

> **Warning** This field is `required`, and should be `unique`

## Description
A description of the Distribution.

> **Warning** This field is `required`

## Publisher
Pointer to the Organisation that published the
resource. The range is foaf:Organisation.

> **Warning** This field is `required`

## Version 
The version indicator (name or identifier) of a
resource. The range is a rdfs:literal.

> **Warning** This field is `required`

## Access Rights
Information about who can access the
resource or an indication of its security status.
This should point to a URL where this
information can be found. We strongly
recommend that access rights are described
as [DUC CCE profile](https://duc.le.ac.uk/).

> **Recommendation** This field is `recommended`

## ODRL Policy
An ODRL conformant policy
document (https://www.w3.org/TR/
odrl-model/) expressing the rights
and/or responsibilities associated
with access to and/or use of the
resource. This should point to a URL
where this conformant document
has been published.

> **Note** This field is `optional`

## Media Type
If you have more than one media type
available for your resource and you wish to
make them all accessible, you need to add
another “Distribution”. Example: json.

> **Note** This field is `optional`

## Is Part Of
Refers to related resources in which this
distribution is physically or logically included.
The range is a URL.

> **Note** This field is `optional`

## Access URL or Download URL
The URL from where the data can be
accessed or downloaded.

> **Note** This field is `optional`

## Access Service
Pointer to the dcat:DataService if available

> **Note** This field is `optional`