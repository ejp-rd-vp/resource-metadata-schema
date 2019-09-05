# Rare disease registry dataset Schema

```
registry.json
```

A schema to describe a dataset of patients, cohorts or biomaterials from a registry

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                     |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [registry.json](registry.json) |

## Schema Hierarchy

- Rare disease registry dataset `registry.json`
  - [Organisation](organisation.md) `organisation.json`

# Rare disease registry dataset Properties

| Property                        | Type                | Required     | Nullable | Defined by                                  |
| ------------------------------- | ------------------- | ------------ | -------- | ------------------------------------------- |
| [@id](#id)                      | `string`            | **Required** | No       | Rare disease registry dataset (this schema) |
| [@type](#type)                  | `enum`              | **Required** | No       | Rare disease registry dataset (this schema) |
| [description](#description)     | `string`            | Optional     | No       | Rare disease registry dataset (this schema) |
| [disease_cases](#disease_cases) | Case or observation | Optional     | No       | Rare disease registry dataset (this schema) |
| [homepage](#homepage)           | `string`            | Optional     | No       | Rare disease registry dataset (this schema) |
| [name](#name)                   | `string`            | Optional     | No       | Rare disease registry dataset (this schema) |
| [publisher](#publisher)         | Organisation        | Optional     | No       | Rare disease registry dataset (this schema) |
| [theme](#theme)                 | Code                | Optional     | No       | Rare disease registry dataset (this schema) |
| `*`                             | any                 | Additional   | Yes      | this schema _allows_ additional properties  |

## @id

a primary identifier for the registry

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: https://www.pcdregistry.eu/

### @id Type

`string`

## @type

the primary type for this registry

`@type`

- is **required**
- type: `enum`
- defined in this schema
- example: PatientRegistryDataset

The value of this property **must** be equal to one of the [known values below](#type-known-values).

### @type Known Values

| Value                    | Description |
| ------------------------ | ----------- |
| `PatientRegistryDataset` |             |
| `BiobankDataset`         |             |

## description

A description for the registry

`description`

- is optional
- type: `string`
- defined in this schema
- example: PDC registry

### description Type

`string`

## disease_cases

Information about the individual cases described in the registry

`disease_cases`

- is optional
- type: Case or observation
- defined in this schema
- example:

### disease_cases Type

Array type: Case or observation

All items must be of the type:

- [Case or observation](case.md) – `case.json`

## homepage

The primary URL for the homepage of the registry

`homepage`

- is optional
- type: `string`
- defined in this schema
- example: https://www.pcdregistry.eu/

### homepage Type

`string`

## name

a name or short description for the registry

`name`

- is optional
- type: `string`
- defined in this schema
- example: PDC registry

### name Type

`string`

## publisher

The primary organisation responsible for publishing and maintaining the registry

`publisher`

- is optional
- type: Organisation
- defined in this schema
- example:

### publisher Type

- [Organisation](organisation.md) – `organisation.json`

## theme

The primary diseases associated with the dataset

`theme`

- is optional
- type: Code
- defined in this schema
- example:

### theme Type

Array type: Code

All items must be of the type:

- [Code](vocabulary_code.md) – `vocabulary_code.json`
