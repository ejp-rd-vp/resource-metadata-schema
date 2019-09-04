# Organisation Schema

```
organisation.json
```

A schema to describe an organisation

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                             |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [organisation.json](organisation.json) |

## Schema Hierarchy

- Organisation `organisation.json`
  - [Location](location.md) `location.json`

# Organisation Properties

| Property                    | Type     | Required     | Nullable | Defined by                                 |
| --------------------------- | -------- | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                  | `string` | Optional     | No       | Organisation (this schema)                 |
| [description](#description) | `string` | Optional     | No       | Organisation (this schema)                 |
| [homepage](#homepage)       | `string` | Optional     | No       | Organisation (this schema)                 |
| [location](#location)       | Location | Optional     | No       | Organisation (this schema)                 |
| [name](#name)               | `string` | **Required** | No       | Organisation (this schema)                 |
| `*`                         | any      | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the organisation

`@id`

- is optional
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
- type: Location
- defined in this schema

### location Type

- [Location](location.md) – `location.json`

## name

a name or short description for the organisation

`name`

- is **required**
- type: `string`
- defined in this schema

### name Type

`string`
