# Coding system Schema

```
vocabulary_code_system.json
```

A code system, controlled vocabulary or ontology

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                                 |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ---------------------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [vocabulary_code_system.json](vocabulary_code_system.json) |

# Coding system Properties

| Property      | Type     | Required     | Nullable | Defined by                                 |
| ------------- | -------- | ------------ | -------- | ------------------------------------------ |
| [@id](#id)    | `string` | **Required** | No       | Coding system (this schema)                |
| [name](#name) | `string` | Optional     | No       | Coding system (this schema)                |
| `*`           | any      | Additional   | Yes      | this schema _allows_ additional properties |

## @id

a primary identifier for the coding system

`@id`

- is **required**
- type: `string`
- defined in this schema
- example: http://www.orpha.net/ontology/ORDO.owl

### @id Type

`string`

## name

A human-readable name for coding system

`name`

- is optional
- type: `string`
- defined in this schema
- example: The Orphanet Rare Disease ontology (ORDO) is jointly developed by Orphanet and the EBI to provide a
  structured vocabulary for rare diseases capturing relationships between diseases, genes and other relevant features
  which will form a useful resource for the computational analysis of rare diseases

### name Type

`string`
