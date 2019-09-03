# Schema

```
case.json
```

A schema block to describe cases or entries in a patient registry or biobank

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In             |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ---------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [case.json](case.json) |

# Properties

| Property                                                      | Type                                       | Required   | Nullable | Defined by                                 |
| ------------------------------------------------------------- | ------------------------------------------ | ---------- | -------- | ------------------------------------------ |
| [description](#description)                                   | `string`                                   | Optional   | No       | (this schema)                              |
| [disease_code](#disease_code)                                 | vocabulary_code                            | Optional   | No       | (this schema)                              |
| [inclusion_exclusion_criteria](#inclusion_exclusion_criteria) | `string`                                   | Optional   | No       | (this schema)                              |
| [number_of_cases](#number_of_cases)                           | `string`                                   | Optional   | No       | (this schema)                              |
| [recruitment_area](#recruitment_area)                         | Rare disease patient or biosample registry | Optional   | No       | (this schema)                              |
| `*`                                                           | any                                        | Additional | Yes      | this schema _allows_ additional properties |

## description

A description for the case

`description`

- is optional
- type: `string`
- defined in this schema

### description Type

`string`

## disease_code

A primary disease code associated with the case or group of patients

`disease_code`

- is optional
- type: vocabulary_code
- defined in this schema

### disease_code Type

Array type: vocabulary_code

All items must be of the type:

- [vocabulary_code](vocabulary_code.md) – `vocabulary_code.json`

## inclusion_exclusion_criteria

A description of the inclusion or exclusion criteria

`inclusion_exclusion_criteria`

- is optional
- type: `string`
- defined in this schema

### inclusion_exclusion_criteria Type

`string`

## number_of_cases

A number of patients registered for this case

`number_of_cases`

- is optional
- type: `string`
- defined in this schema

### number_of_cases Type

`string`

## recruitment_area

The region or local covered by the registry

`recruitment_area`

- is optional
- type: Rare disease patient or biosample registry
- defined in this schema

### recruitment_area Type

Array type: Rare disease patient or biosample registry

All items must be of the type:

- [Rare disease patient or biosample registry](location.md) – `location.json`
