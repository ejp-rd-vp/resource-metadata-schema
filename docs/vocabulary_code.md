# Code Schema

```
vocabulary_code.json
```

A code from a coding system, controlled vocabulary or ontology

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                   |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [vocabulary_code.json](vocabulary_code.json) |

## Schema Hierarchy

- Code `vocabulary_code.json`
  - [Coding system](vocabulary_code_system.md) `vocabulary_code_system.json`

# Code Properties

| Property                    | Type          | Required     | Nullable | Defined by                                 |
| --------------------------- | ------------- | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                  | `string`      | **Required** | No       | Code (this schema)                         |
| [code_system](#code_system) | Coding system | Optional     | No       | Code (this schema)                         |
| [name](#name)               | `string`      | Optional     | No       | Code (this schema)                         |
| `*`                         | any           | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the code

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: http://www.orpha.net/ORDO/Orphanet_137628

### @id Type

`string`

## code_system

A coding system that defines the code

`code_system`

- is optional
- type: Coding system
- defined in this schema
- example:

### code_system Type

- [Coding system](vocabulary_code_system.md) – `vocabulary_code_system.json`

## name

A human-readable name for code

`name`

- is optional
- type: `string`
- defined in this schema
- example: Cardiac anomalies-heterotaxy syndrome

### name Type

`string`
