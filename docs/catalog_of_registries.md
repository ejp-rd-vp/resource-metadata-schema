# Rare disease catalog Schema

```
catalog_of_registries.json
```

Schema to describe a resource that catalogs registries such as Orphanet

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                               |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [catalog_of_registries.json](catalog_of_registries.json) |

# Rare disease catalog Properties

| Property                      | Type         | Required     | Nullable | Defined by                                 |
| ----------------------------- | ------------ | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                    | `string`     | **Required** | No       | Rare disease catalog (this schema)         |
| [@type](#type)                | `enum`       | **Required** | No       | Rare disease catalog (this schema)         |
| [datasets](#datasets)         | `string[]`   | Optional     | No       | Rare disease catalog (this schema)         |
| [description](#description)   | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [homepage](#homepage)         | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [name](#name)                 | `string`     | Optional     | No       | Rare disease catalog (this schema)         |
| [organisation](#organisation) | Organisation | Optional     | No       | Rare disease catalog (this schema)         |
| `*`                           | any          | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the catalog

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: http://www.orpha.net

### @id Type

`string`

## @type

the primary type for this catalog

`@type`

- is **required**
- type: `enum`
- defined in this schema
- example: CatalogOfRegistries

The value of this property **must** be equal to one of the [known values below](#type-known-values).

### @type Known Values

| Value                 | Description |
| --------------------- | ----------- |
| `CatalogOfRegistries` |             |

## datasets

`datasets`

- is optional
- type: `string[]`
- defined in this schema
- example: http://www.orpha.net/datasests/1

### datasets Type

Array type: `string[]`

All items must be of the type: `string`

## description

A description for the catalog

`description`

- is optional
- type: `string`
- defined in this schema
- example: Orphanet is a unique resource, gathering and improving knowledge on rare diseases

### description Type

`string`

## homepage

The primary URL for the homepage of the catalog

`homepage`

- is optional
- type: `string`
- defined in this schema
- example: http://www.orpha.net

### homepage Type

`string`

## name

a name or short description for the catalog

`name`

- is optional
- type: `string`
- defined in this schema
- example: Orphanet

### name Type

`string`

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
