# Rare disease registry dataset Schema

```
catalog.json
```

A schema to describe a dataset of patients, cohorts or biomaterials from a catalog

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                     |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [catalog.json](catalog.json) |

## Schema Hierarchy

- Rare disease registry dataset `registry.json`
  - [Organisation](organisation.md) `organisation.json`

# Rare disease registry dataset Properties

| Property                        | Type                | Required     | Nullable | Defined by                                  |
| ------------------------------- | ------------------- | ------------ | -------- | ------------------------------------------- |
| [@id](#id)                      | `string`            | **Required** | No       | Rare disease registry dataset (this schema) |
| [homepage](#homepage)           | `string`            | Optional     | No       | Rare disease registry dataset (this schema) |
| [hasPart](#hasPart)             | Resource            | Optional     | No       | Rare disease registry dataset (this schema) |
| [dataset](#dataset)             | Dataset             | Optional     | No       | Rare disease registry dataset (this schema) |
| [publisher](#publisher)         | Organisation        | Optional     | No       | Rare disease registry dataset (this schema) |
| [catalog](#catalog)             | Catalog             | Optional     | No       | Rare disease registry dataset (this schema) |
| [resource](#resource)           | Resource            | Optional     | No       | Rare disease registry dataset (this schema) |
| `*`                             | any                 | Additional   | Yes      | this schema _allows_ additional properties  |

## @id

a primary identifier for the catalog

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: https://www.pcdregistry.eu/


## homepage

The primary URL for the homepage of the catalog

`homepage`

- is optional
- type: `string`
- defined in this schema
- example: https://www.pcdregistry.eu/

### homepage Type

`string`

## hasPart

An item that is listed in the cataloged resources

`hasPart`

- is optional
- type: resource
- defined in this schema
- example:

### hasPart Type

- [catalog_of_resources](catalog_of_resources.md) – `catalog_of_resources.json`



## publisher

The primary organisation responsible for publishing and maintaining the registry

`publisher`

- is optional
- type: Organisation
- defined in this schema
- example:

### publisher Type

- [Organisation](organisation.md) – `organisation.json`


## dataset

An item that is listed in the cataloged resources

`dataset`

- is optional
- type: dataset
- defined in this schema
- example:

### dataset Type

- [dataset](dataset.md) – `dataset.json`




## resource

An item that is listed in the cataloged resources

`resource`

- is optional
- type: dataset
- defined in this schema
- example:

### resource Type

- [catalog_of_resources](catalog_of_resources.md) – `catalog_of_resources.json`
