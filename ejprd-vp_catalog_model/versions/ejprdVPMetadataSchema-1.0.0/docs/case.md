# Case or observation Schema

```
case.json
```

Metadata about a dataset in a patient registry or biobank

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In             |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ---------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [case.json](case.json) |

# Case or observation Properties

| Property                                                      | Type     | Required   | Nullable | Defined by                                 |
| ------------------------------------------------------------- | -------- | ---------- | -------- | ------------------------------------------ |
| [description](#description)                                   | `string` | Optional   | No       | Case or observation (this schema)          |
| [disease_code](#disease_code)                                 | Code     | Optional   | No       | Case or observation (this schema)          |
| [inclusion_exclusion_criteria](#inclusion_exclusion_criteria) | `string` | Optional   | No       | Case or observation (this schema)          |
| [number_of_cases](#number_of_cases)                           | `string` | Optional   | No       | Case or observation (this schema)          |
| [recruitment_area](#recruitment_area)                         | Location | Optional   | No       | Case or observation (this schema)          |
| `*`                                                           | any      | Additional | Yes      | this schema _allows_ additional properties |

## description

A description for the case

`description`

- is optional
- type: `string`
- defined in this schema
- example: number of patients

### description Type

`string`

## disease_code

A primary disease code associated with the case or group of patients

`disease_code`

- is optional
- type: Code
- defined in this schema
- example:

### disease_code Type

Array type: Code

All items must be of the type:

- [Code](vocabulary_code.md) – `vocabulary_code.json`

## inclusion_exclusion_criteria

A description of the inclusion or exclusion criteria

`inclusion_exclusion_criteria`

- is optional
- type: `string`
- defined in this schema
- example: none

### inclusion_exclusion_criteria Type

`string`

## number_of_cases

A number of patients registered for this case

`number_of_cases`

- is optional
- type: `string`
- defined in this schema
- example: 12

### number_of_cases Type

`string`

## recruitment_area

The region or local covered by the registry

`recruitment_area`

- is optional
- type: Location
- defined in this schema
- example:

### recruitment_area Type

Array type: Location

All items must be of the type:

- [Location](location.md) – `location.json`
