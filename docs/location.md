# Rare disease patient or biosample registry Schema

```
location.json
```

A schema to describe a location, region or jurisdiction

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                     |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [location.json](location.json) |

# Rare disease patient or biosample registry Properties

| Property            | Type     | Required     | Nullable | Defined by                                               |
| ------------------- | -------- | ------------ | -------- | -------------------------------------------------------- |
| [@id](#id)          | `string` | **Required** | No       | Rare disease patient or biosample registry (this schema) |
| [city](#city)       | `string` | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [country](#country) | `string` | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| [region](#region)   | `enum`   | Optional     | No       | Rare disease patient or biosample registry (this schema) |
| `*`                 | any      | Additional   | Yes      | this schema _allows_ additional properties               |

## @id

a primary identifier for the location

`@id`

- is **required**
- type: `string`
- defined in this schema

### @id Type

`string`

## city

The name of a city

`city`

- is optional
- type: `string`
- defined in this schema

### city Type

`string`

## country

The name of a country

`country`

- is optional
- type: `string`
- defined in this schema

### country Type

`string`

## region

A broad description of a region

`region`

- is optional
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#region-known-values).

### region Known Values

| Value                   | Description |
| ----------------------- | ----------- |
| `international, europe` |             |
