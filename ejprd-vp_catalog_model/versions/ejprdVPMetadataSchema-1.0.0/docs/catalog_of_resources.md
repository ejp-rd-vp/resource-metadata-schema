# EJPRD VP discoverable Cataloged Resources (Resource) Schema

```
catalog_of_resources.json
```

Schema to describe resource that are discoverable on the EJPRD VP e.g. Orphanet

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                               |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [catalog_of_resource.json](catalog_of_resources.json) |

# Rare disease resources Properties

| Property                      | Type         | Required     | Nullable | Defined by                                 |
| ----------------------------- | ------------ | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                    | `string`     | **Required** | No       | Rare disease catalog (this schema)         |
| [@type](#type)                | `enum`       | **Required** | No       | Rare disease catalog (this schema)         |
| [landingPage](#landingPage)   | `string[]`   | **Required** | No       | Rare disease catalog (this schema)         |
| [theme](#theme)               | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [description](#description)   | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [language](#language)         | `enum`       | **Required** | No       | Rare disease catalog (this schema)         |
| [publisher](#publisher)       |`organisation`| Optional     | No       | Rare disease catalog (this schema)         |
| [title](#title)               | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [keyword](#keyword)           | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| `*`                           | any          | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the cataloged resources

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: http://www.orpha.net

### @id Type

`string`

## @type

the primary type for this resource

`@type`

- is **required**
- type: `enum`
- defined in this schema
- example: CatalogOfRegistries

The value of this property **must** be equal to one of the [known values below](#type-known-values).

### @type Known Values

| Value                         | Description |
| ------------------------------| ----------- |
| `CatalogOfRegistries`         |             |
| `CatalogOfBioBanks`           |             |
| `CatalogOfBioTools`           |             |
| `CatalogOfResearchProjects`   |             |


## landingPage alias homepage

The primary URL for the homepage of the catalog

`landingPage`

- is optional
- type: `string`
- defined in this schema
- example: http://www.orpha.net

## landingPage Type

`string`


## theme

A main category of the resource. A resource can have multiple themes.

`theme`

- is optional
- type: `string`
- defined in this schema


## description

A description for the catalog

`description`

- is optional
- type: `string`
- defined in this schema
- example: Orphanet is a unique resource, gathering and improving knowledge on rare diseases

### description Type

`string`



## language

This refers to the natural language used for textual metadata (i.e. titles, descriptions, etc) of a cataloged resource (i.e. dataset)

`language`

- is **required**
- type: `enum`
- defined in this schema
- example: English

The value of this property **must** be equal to one of the [known values below](#type-known-values).

### @type Known Values

| Value                         | Description |
| ------------------------------| ----------- |
| `English`                     |             |
| `French`                      |             |
| `German`                      |             |



## publisher

The primary organisation responsible for publishing and maintaining the registry

`publisher`

- is optional
- type: Organisation
- defined in this schema
- example:

### publisher Type

- [Organisation](organisation.md) – `organisation.json`


## title

A name given to the cataloged resource.

`title`

- is **required**
- type: `string`
- defined in this schema
- example: Orphanet


## keyword

A keyword or tag describing the resource.

`keyword`

- is **required**
- type: `string`
- defined in this schema
- example: Orphanet - The portal for rare diseases and orphan drugs


## location

`location`

- is optional
- type: Location
- defined in this schema
- example:

### location Type

Array type: location

All items must be of the type:

- [Location](location.md) – `location.json`


## organisation

`organisation`

- is optional
- type: Organisation
- defined in this schema
- example:

### organisation Type

Array type: Organisation

All items must be of the type:

- [Organisation](organisation.md) – `organisation.json`
