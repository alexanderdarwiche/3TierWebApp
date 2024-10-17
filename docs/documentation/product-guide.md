# Product guide

## Product Guide <a href="#dexkj" id="dexkj"></a>

To get a foundation for how products are structured and their different features the [product structure user guide](https://developer.younium.com/guides/products) is a good place to start. This section will handle how to work with products from the API and how products are constructed as entities or objects.

#### Product type and object structure <a href="#hm9nb" id="hm9nb"></a>

The product type defines how many charge plans and charges a product has but all products contain a list of at least one charge plan which in turn contains a list of at least one charge. The four product types consist of:

* `Simple`: Can have only one charge plan with one charge
* `MultipleCharges`: Can have only one charge plan with multiple charges
* `MultipleChargePlans`: Can have multiple charge plans with only one charge each
* `Full`: Can have multiple charge plans with multiple charges

Simplified JSON Example of the structure of a `simple` product response:

```
"product": {
    "productNumber": "P-000001",
    "chargePlans": [
        {
            "chargePlanNumber": "CP-000001",
            "charges": [
                {
                     "chargeNumber": "C-000001",
                     "priceDetails": [...]
                }
            ]
        }
    ]
}
```

Simplified JSON Example of the structure of a Full product response:

```
"product": {
    "productNumber": "P-000001",
    "chargePlans": [
        {
            "chargePlanNumber": "CP-000001",
            "charges": [
                {
                     "chargeNumber": "C-000001",
                     "priceDetails": [...]
                },
                {
                     "chargeNumber": "C-000002",
                     "priceDetails": [...]
                }
            ]
        },
        {
            "chargePlanNumber": "CP-000002",
            "charges": [
                {
                     "chargeNumber": "C-000003",
                     "priceDetails": [...]
                },
                {
                     "chargeNumber": "C-000004",
                     "priceDetails": [...]
                },
                {
                     "chargeNumber": "C-000005",
                     "priceDetails": [...]
                }
            ]
        },
    ]
}
```

#### Charge plans <a href="#id-4bucz" id="id-4bucz"></a>

The charge plan as an object mainly serves as a container for charges within the product structure and contains no specifically important fields other than general ones. Nonetheless, it is an important reference for order products (products on an order) linking the order products to its initial product and charges.

#### Charges <a href="#ufmqp" id="ufmqp"></a>

Charges are the most important part of the product and hold the most important information which makes them more complex with a number of important fields.\
One way of looking at charges is by separating its fields into different categories.

“General fields”, “charge configuration fields”, and “financial fields”

In the following JSON example, the fields are sorted by each category.

```
{ 
    //"General fields" 
    "name": "string", 
    "customFields": {}, 
    "externalCRMId": "string", 
    "externalERPId": "string", 
     
    //charge configuration fields 
    "chargeType": "Recurring", 
    "model": "Quantity", 
    "unit": "units", 
    "pricePeriod": "Monthly, 
    "defaultQuantity": 0, 
    "usageRating": "Sum", 
    "measurementsRule": 0, 
    "PriceDetails": [ 
        { 
            "tier": 0, 
            "currency": "EUR", 
            "price": 10, 
            "customFields": {}, 
            "description": "string", 
            "isInfinite": false, 
            "priceBase": "Flat", 
            "toQuantity": 0 
        } 
    ], 
 
    //Financial fields 
    "billingPeriod": "Monthly", 
    "periodAlignment": "None", 
    "billingDay": "None", 
    "billingTiming" "InAdvance" 
    "specificBillingDay": 0, 
    "taxIncluded": false, 
    "revenueRecognition": "Recognized monthly over time", 
    "taxTemplate": "Sweden standard", 
    "deferredRevenueAccount": "2970", 
    "recognizedRevenueAccount": "3000" 
}
```

#### General fields <a href="#tpelm" id="tpelm"></a>

These are general fields and features for a charge. Read more about custom fields and external ids in the [developer resources section](https://developer.younium.com/guides/products)

#### Charge configuration fields <a href="#pgpep" id="pgpep"></a>

These are fields that define what type of charge and model it is, as well as fields that are connected to the type or model and its price details.

The charge type will dictate what price model can be and the combination of what type and what model a charge has and dictates what values will define the charge. The matrixes below show the relationship between the fields and what type and model a charge has.

![](https://developer.younium.com/content/charge%20matrix.png)

Most values can be set even if they have no importance for the type and model and will be ignored when the charge is used. If a value would be prohibited to be set in a specific case or required this will generally be stated in the documentation or throw a validation error on the request.

#### Financial fields <a href="#id-9gvjv" id="id-9gvjv"></a>

These fields are connected to how the charge will be billed on an order and act as default values for the order product charge (the charge of an order) when it’s created based on the charge.

#### Default charge values <a href="#rh9j4" id="rh9j4"></a>

In the Younium UI Settings > Products > Product settings default values for charges can be specified. If a field is left out or set to null in the request, will set it to the default value if one is defined. Noteworthy fields that can be null if no default value is present `revenueRecognition`, `taxTemplate`, `deferredRevenueAccount`, and `recognizedRevenueAccount`. In some use cases, this is preferred and these values are set when the order product charge is created.

#### Price details <a href="#u4cbn" id="u4cbn"></a>

At least one price detail is required on a charge (With the exception of a rated usage charge which should have none) and contains the information of the charge's price. The price model will dictate the price detail structure and relates primarily to two fields on the price detail object: `tier` and `currency`.

The tier field is a zero-bases-index for a specific currency and only one tier index can exist for each currency. If a charges model is `flat` or `quantity` there can only be one price detail per currency and the tier will always be 0. So the tier index is more important to consider if the model is `volume` or `tiered` where the price detail is grouped by currency and ordered by the tier.

When adding multiple price detail tiers to a charge there are some rules to consider to avoid validation errors:

* The tier index is required to start with 0 and increment by 1 for each tier. Skipping an index will cause a validation error.
* `toQuantity` must be larger than the `toQuantity`of the previous tier. `fromQuantity` (not settable) will be calculated based on this.
* `toQuantity` should be set for each tier with the exception of the last tier if `isInfinite` is true. if `toQuantity` is 0 or less or not set it will take the `fromQuantity` value or 0 if `tier` is 0.
* `isInfinite` will only affect the last tier and will override `toQuantity`
* If a `currency` is not specified the base currency of the legal entity will be applied by default.

#### Product category <a href="#yefnc" id="yefnc"></a>

Category for products to eg. simplify reports. also used if the product is a stock product. this field will reference the product categories found in settings > products > product categories where it’s possible to create new ones.

## Creating a product <a href="#id-0vuiu" id="id-0vuiu"></a>

The POST `/products` endpoint is used for creating products.

Example of a request creating a simple subscription of a monthly recurring flat fee:

Remarks about the request:

* Note that the tier doesn’t have to be set on the price details in this case as there can be only one per currency. Tier will get the value 0 as default.

#### Creating a full product example <a href="#s0suk" id="s0suk"></a>

Say we are offering a SaaS in which there are 3 plans: starter, professional. In each plan, there is a recurring base fee for 100, 400 and including 5, 15, and 30 seats, respectively, and above those included seats, there’s a volume-based discounted price tier.

For example, for the starter plan

![](https://developer.younium.com/content/table.png)

## Patching a product <a href="#blujk" id="blujk"></a>

The Patch `/products/{id}` are used to update a product and provide an endpoint for creating, changing, and removing charge plans, charges, and price details.

Updating charges and charge plans on framework products are not yet supported in the API, however, it is possible to patch framework products on the product level by leaving out the che `chargePlans` field.

The Patch request body is structured the same way as the request for creating a product with the addition of a few fields:

The `operation` field on charge plans, charges, and price details which defines how to handle an entity and allows one of three values: `Change`, `Create,` and `Remove`. `Change` is the default value.

Charges have the field `charge` and charge plans have the `chargePlan` field which are both lookupkey-identifiers and are used for referencing the charge or charge plan to be removed or changed.

The functionality in the API will match these two fields and may overwrite them in some cases to set the correct operations based on the logic of the action. It is there for possible to leave these fields out in the request in some combinations:

* if `operation` is set to `Create` the lookup key for that entity will be ignored as well as all child entities’ `operation` fields will be overwritten with `Create`.
* if `operation` is set to `Remove` the lookup Key is required and child entities will inherit the `Remove` value if set. In case an entity is to be removed it’s best practice to only provide the `operation` and `lookupkey` field for that entity and leave children and other fields out.
* if `operation` is set to `Change` the lookup Key is required and will not have any effect on child entities.
* Price details have no `lookupkey` field and are instead referenced by the combination of the `tier`and the `currencyCode` fields.

The validations for creating a product will be applied to updating one as well but there are some

Cases to consider when working with patching the products:

* Removing entities will not always be possible and will fail if the charge plan, charge, or price detail is in use on an order
* changing the `producType` may require charge plans and charges to explicitly be removed to fit the correct product structure
* changing the `model` may alter the existing `priceDetails` event if this isn’t specified.
  * if `model` Type is set from `volume` or `tiered` to `flat` or `qunatity` all `priceDetails` with a tier greater than 0 will be removed
  * if `model` is set to `rated` all `priceDetails` will be removed
* New entities will get the default values unless other is specified.

A WORD OF CAUTION: It is not possible to reverse a successful update. In other words, entities on a product that have been deleted can not be recovered and changes cannot be undone.

#### Patching a full product endpoint <a href="#m9koe" id="m9koe"></a>

Taking the above example request of creating a full product and updating it with:

* Adding an enterprise charge plan
* Removing the middle tiers on the Starter tiered charge.
* Updating the price on the flat recurring fee on the Professional charge plan

## Deleting a product <a href="#ow6mr" id="ow6mr"></a>

Deleting products or its child entities can be done on all levels using one of the endpoints that are found in the API references. An entity that is in use cannot be deleted. price details can be removed by updating the charge using the `PATCH` endpoints.
