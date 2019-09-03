# Schema

```
vocabulary_code.json
```

A code from a coding system, controlled vocabulary or ontology

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                   |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [vocabulary_code.json](vocabulary_code.json) |

## Schema Hierarchy

- `vocabulary_code.json`
- [vocabulary_code_system](vocabulary_code_system.md) `vocabulary_code_system.json`

# Properties

| Property                    | Type                   | Required     | Nullable | Defined by                                 |
| --------------------------- | ---------------------- | ------------ | -------- | ------------------------------------------ |
| [@id](#id)                  | `string`               | **Required** | No       | (this schema)                              |
| [code_system](#code_system) | vocabulary_code_system | Optional     | No       | (this schema)                              |
| [name](#name)               | `string`               | Optional     | No       | (this schema)                              |
| `*`                         | any                    | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the code

`@id`

- is **required**
- type: `string`
- defined in this schema

### @id Type

`string`

## code_system

A coding system that defines the code

`code_system`

- is optional
- type: vocabulary_code_system
- defined in this schema

### code_system Type

- [vocabulary_code_system](vocabulary_code_system.md) – `vocabulary_code_system.json`

## name

A human-readable name for code

`name`

- is optional
- type: `string`
- defined in this schema

### name Type

`string`
