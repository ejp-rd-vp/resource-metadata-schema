# EJPRD VP discoverable Catalogs Schema


```
dataset.json
```

A schema to describe a dataset of patients, cohorts or biomaterials from a catalog

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                     |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [dataset.json](dataset.json) |

## Schema Hierarchy

- Rare disease registry dataset `dataset.json`
  - [Location](location.md) `location.json`

# Rare disease catalogs dataset Properties

| Property                        | Type                | Required     | Nullable | Defined by                                  |
| ------------------------------- | ------------------- | ------------ | -------- | ------------------------------------------- |
| [@id](#id)                      | `string`            | **Required** | No       | Rare disease registry dataset (this schema) |
| [spatial](#spatial)             | Location            | **Required** | No       | Rare disease registry dataset (this schema) |
| [resource](#resource)           | Resource            | Optional     | No       | Rare disease registry dataset (this schema) |
| `*`                             | any                 | Additional   | Yes      | this schema _allows_ additional properties  |

## @id

a primary identifier for the catalog

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: https://www.pcdregistry.eu/


## spatial

The geographical area covered by the dataset.

`spatial`

- is optional
- type: `location`
- defined in this schema


### spatial Type


- [Location](location.md) – `location.json`


## resource

An item that is listed in the cataloged resources

`resource`

- is optional
- type: resource
- defined in this schema
- example:

### resource Type

- [catalog_of_resources](catalog_of_resources.md) – `catalog_of_resources.json`
