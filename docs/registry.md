# Rare disease patient or biosample registry Schema

```
registry.json
```

A schema to describe a dataset of patients, cohorts or biomaterials from a registry

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                     |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [registry.json](registry.json) |

# Rare disease patient or biosample registry Properties

| Property                        | Type                  | Required     | Nullable | Defined by                                               |
| ------------------------------- | --------------------- | ------------ | -------- | -------------------------------------------------------- |
| [@id](#id)                      | `string`              | **Required** | No       | Rare disease patient or biosample registry (this schema) |
| [@type](#type)                  | `enum`                | **Required** | No       | Rare disease patient or biosample registry (this schema) |
| [description](#description)     | `string`              | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [disease_cases](#disease_cases) | case                  | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [homepage](#homepage)           | `string`              | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [name](#name)                   | `string`              | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [publisher](#publisher)         | Rare disease resource | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [theme](#theme)                 | vocabulary_code       | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| `*`                             | any                   | Additional   | Yes      | this schema _allows_ additional properties               |

## @id

a primary identifier for the registry

`@id`

- is **required**
- type: `string`
- defined in this schema

### @id Type

`string`

## @type

the primary type for this registry

`@type`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#type-known-values).

### @type Known Values

| Value                    | Description |
| ------------------------ | ----------- |
| `PatientRegistryDataset` |             |
| `BiobankRegistryDataset` |             |

## description

A description for the registry

`description`

- is optional
- type: `string`
- defined in this schema

### description Type

`string`

## disease_cases

Information about the individual cases described in the registry

`disease_cases`

- is optional
- type: case
- defined in this schema

### disease_cases Type

Array type: case

All items must be of the type:

- [case](case.md) – `case.json`

## homepage

The primary URL for the homepage of the registry

`homepage`

- is optional
- type: `string`
- defined in this schema

### homepage Type

`string`

## name

a name or short description for the registry

`name`

- is optional
- type: `string`
- defined in this schema

### name Type

`string`

## publisher

The primary organisation responsible for publishing and maintaining the registry

`publisher`

- is optional
- type: Rare disease resource
- defined in this schema

### publisher Type

Array type: Rare disease resource

All items must be of the type:

- [Rare disease resource](organisation.md) – `organisation.json`

## theme

The primary diseases associated with the dataset

`theme`

- is optional
- type: vocabulary_code
- defined in this schema

### theme Type

Array type: vocabulary_code

All items must be of the type:

- [vocabulary_code](vocabulary_code.md) – `vocabulary_code.json`
