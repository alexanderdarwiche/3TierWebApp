# Developer resources

### API environment base URLs <a href="#o4cp8" id="o4cp8"></a>

Sandbox: [https://api.sandbox.younium.com](https://developer.younium.com/developer-resources)

Production: [https://api.younium.com](https://developer.younium.com/developer-resources)

US-Sandbox. [api.sandbox.us.younium.com](https://developer.younium.com/developer-resources)

US-Production: [api.us.younium.com](https://developer.younium.com/developer-resources)

### Using the API <a href="#kgxos" id="kgxos"></a>

The Younium API is a rest API using json data. In general, the following Http verbs are used:

* GET: Read
* POST: Create
* PATCH: Update
* DELETE: Delete

#### Patching data <a href="#hk1os" id="hk1os"></a>

Updates to data in Younium are made using the concept of patching. This means that only the data (fields) provided in the patch request are updated in the target entity, all other fields on the entity remains as they were (except when a change of a field triggers changes to other fields, such as calculated/aggregated values, statuses, etc.).

#### NULL values <a href="#zlqpf" id="zlqpf"></a>

Each endpoint have a schema with fields that will populate the response if there is a value. However when the response data is created there may be fields that have no value, which are null. These Fields are excluded from the JSON response. In other words only fields containing values are present in the response.

### API versioning <a href="#jjk1f" id="jjk1f"></a>

The API have two versions with some differences.

#### Features of version 2.0 <a href="#id-9b9p0" id="id-9b9p0"></a>

* All records of en entity are fetched.
* Responses containing multiple records are returned as a List and as an empty list if no records was found.

#### Features of version 2.1 <a href="#id-90pex" id="id-90pex"></a>

* Responses containing multiple records are returned and wrapped in a paginated response providing 1 -100 entries per page.
* If no entries are found a 400 Bad Request response is returned.
* Query parameter functionality.
  * Pagination
  * Filter
  * OrderBy

To specify the version in your API request header:

```
api-version: 2.1
```

### Query Parameters (for version 2.1) <a href="#srhem" id="srhem"></a>

#### Pagination <a href="#jzjhl" id="jzjhl"></a>

Pagination can be set with pageNumber and pageSize (number of records on each page). The pageSize have a limit of 100 records per page.

Example:

```
https://api.sandbox.younium.com/Subscriptions?pageSize=25&pageNumber=2
```

#### OrderBy <a href="#uikdr" id="uikdr"></a>

The request can be ordered either ascending or descending by one or more field names.

Example of ordering a GET subscriptions request by descending order number:

```
https://api.sandbox.younium.com/Subscriptions?orderby=orderNumber desc
```

Example of the same request but ordering first by ascending effective start date, and then after descending order number:&#x20;

```
https://api.sandbox.younium.com/Subscriptions?orderby=effectiveStartDate asc, orderNumber desc
```

#### Filter <a href="#nktqd" id="nktqd"></a>

A filter can be added to a request returning only records that pass certain tests.

```
?filter=[fieldName] [operator] [value]
```

The following operators can be used to test records.

Equality operators:

* `eq:` ( == ) Test if a field is equal to a value.
* `ne:` ( != ) Test if a field is not equal to a value.

Range operators:

* `gt`: ( > ) Test if a field is greater than a value.
* `lt:` ( < ) Test if a field is  less than a value.
* `ge:` ( >= ) Test if a field is greater than or equal to a value.
* `le:` ( <= ) Test if a field is less than or equal to a value.

Logical operators

* `and`: Test if two statements are true.
* `or:` Test if one of two statements are true.

String value

Single quotation marks ( `'string'` ) must be used when passing a string as a constant

Example:

```
https://api.sandbox.younium.com/Subscriptions?filter=status eq 'Active'
```

Datetime and guid values

Fields that are guids/uuid or datetimes will need to specified by type like in the following examples. Important to note the lower casing on the type.

Example for DateTimes:

```
https://api.sandbox.younium.com/Subscriptions?filter=modified gt datetime'2023-04-01'
```

Example for Guid:

```
https://api.sandbox.younium.com/Accounts?filter=invoiceBatchGroupId eq guid'f68a9sa3-ff43-4f95-44b4-08f84be1dda4'
```

Nested objects

It is possible to test nested objects of a request by using `'[fieldName]/[nested fieldName]'. Important to note is that this will not work for calculated field, if field name is null and for filtering lists. This includes filtering on custom fields that is not possible.`

Example of only returning subscriptions with a CMRR amount between 100 and 1000:

```
https://api.sandbox.younium.com/Subscriptions?filter=cmrr/amount ge 100 and cmrr/amount le 1000
```

Multiple conditions

The logical operators can be used to chain multiple conditions in a query like in the example above. The parentheses "( )" can also be used to nest conditions to ensure the logic is applied in the correct order.

Example:

```
https://api.sandbox.younium.com/Accounts?filter=inactive eq false and (defaultDeliveryAddress/country eq 'Norway' or defaultDeliveryAddress/country eq 'Sweden') 
```

String Functions

For string values it is possible to use some extended functionality to filter on strings that starts with, ends with or contains (substringof) a string segment. These functions replace the condition pattern \[fieldName] \[operator] \[value]. Important to use lower casing on the function names.

Examples:

```
https://api.sandbox.younium.com/ChartOfAccounts?filter=startswith(code, '3')

https://api.sandbox.younium.com/Accounts?filter=endswith(invoiceEmailAddress, 'company.com')

//Filter for products include 'service' in its name. Note the value is the first argument and the field name the second 
https://api.sandbox.younium.com/Products??filter=substringof('service', name)
```

#### Modified after and modified before <a href="#id-5cfru" id="id-5cfru"></a>

As the filter is only applied to the top level of the entity structure, querying entities that has been modified before or after a specific data may not always be accurate. Eg a subscription may have a charge or a custom field which have been modified after the subscription. In these cases the `modifiedAfter` and `modifiedBefore` parameters can be used as they apply the modified filter on all sub levels of the entity. each filter is applied as an `or` statement returning any entity where a modified match is found returning only results where at least one of the entity or sub entities have been modified withing the specified date time.

Which sub-entities that are affected by these filters will be specified in the parameter description on the API reference. Worth noting that even though the filter is applied on all specified objects, some like custom fields and price details don’t have the modified field mapped.

Examples:

```
https://api.sandbox.younium.com/Subscriptions?modifiedAfter=2023-11-01

https://api.sandbox.younium.com/Subscriptions?modifiedBefore=2023-01-01

https://api.sandbox.younium.com/Subscriptions?modifiedAfter=2023-06-01&modifiedBefore=2023-12-01
```

### LookupKey Identifier <a href="#vq4um" id="vq4um"></a>

In the request body of POST and PATCH there is sometimes a need identify or reference relating entities, eg. when creating a Subscription we want to define what Account it belongs to or what Currency to use. Fields like this are of the type `LookupKey`and can accept both a `uuid/Guid, a String and a key-value-pair-object`.

Examples of lookupKey-value as a string to set the field account:

```
{
  "account": "A-000001", //using a string to identify by accountNumber
//or
  "account": "8621d3c5-473e-41f1-f394-08d9dfc48d99" //identifying by uuid/guid
  "description": "New Subscription",
  "effectiveStartDate": "2022-07-15", 
  ...
}
```

By setting the field with `key-value-pair-object`and in the`key`specifying what property to identify against it is possible to match with a wider range of properties.\
The following example is using key-value-pair matching with the name of the Account:

```
{
  "account": {
    "key": "name",
    "value": "ExampleAccount"
  }
  "description": "New Subscription",
  "effectiveStartDate": "2022-07-15", 
  ...
}
```

The LookupKey will try to match the values that are set against the field entity. If no matches are found or if there are multiple matches found a Bad Request will be returned.

If a custom field is used as a key it is simply specified by its key property.

```
{
  "account": {
    "key": "customFieldKey",
    "value": "custom value 1"
  }
  ...
}
```
