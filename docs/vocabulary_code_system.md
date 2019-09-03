# Schema

```
vocabulary_code_system.json
```

A code system, controlled vocabulary or ontology

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                                 |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ---------------------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [vocabulary_code_system.json](vocabulary_code_system.json) |

# Properties

| Property      | Type     | Required     | Nullable | Defined by                                 |
| ------------- | -------- | ------------ | -------- | ------------------------------------------ |
| [@id](#id)    | `string` | **Required** | No       | (this schema)                              |
| [name](#name) | `string` | Optional     | No       | (this schema)                              |
| `*`           | any      | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the coding system

`@id`

- is **required**
- type: `string`
- defined in this schema

### @id Type

`string`

## name

A human-readable name for coding system

`name`

- is optional
- type: `string`
- defined in this schema

### name Type

`string`
