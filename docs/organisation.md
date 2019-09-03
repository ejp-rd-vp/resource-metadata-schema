# Rare disease resource Schema

```
organisation.json
```

A schema to describe an organisation

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                             |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [organisation.json](organisation.json) |

# Rare disease resource Properties

| Property                    | Type                                       | Required     | Nullable | Defined by                                 |
| --------------------------- | ------------------------------------------ | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                  | `string`                                   | **Required** | No       | Rare disease resource (this schema)        |
| [description](#description) | `string`                                   | Optional     | No       | Rare disease resource (this schema)        |
| [homepage](#homepage)       | `string`                                   | Optional     | No       | Rare disease resource (this schema)        |
| [location](#location)       | Rare disease patient or biosample registry | Optional     | No       | Rare disease resource (this schema)        |
| [name](#name)               | `string`                                   | Optional     | No       | Rare disease resource (this schema)        |
| `*`                         | any                                        | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the registry

`@id`

- is **required**
- type: `string`
- defined in this schema

### @id Type

`string`

## description

A description for the organiation

`description`

- is optional
- type: `string`
- defined in this schema

### description Type

`string`

## homepage

The primary URL for the homepage of the organisation

`homepage`

- is optional
- type: `string`
- defined in this schema

### homepage Type

`string`

## location

Information about the location associated with the organisation

`location`

- is optional
- type: Rare disease patient or biosample registry
- defined in this schema

### location Type

Array type: Rare disease patient or biosample registry

All items must be of the type:

- [Rare disease patient or biosample registry](location.md) – `location.json`

## name

a name or short description for the organisation

`name`

- is optional
- type: `string`
- defined in this schema

### name Type

`string`
