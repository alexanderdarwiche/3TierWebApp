---
icon: bullhorn
---

# News and updates

#### <mark style="color:orange;">2024-04-10 - Release updates for API version 2.1</mark> <a href="#unuii" id="unuii"></a>

* New endpoints
  * POST /Invoices/{id}/ProcessStripePayment - processes stripe payment for an invoice
  * GET /Invoices/{id}/OnlinePaymentLogs - get online payment logs (stripe payment logs)
  * POST /Payments/CreateAndPost - create and post for an invoice
* Changes
  * latestOnlinePaymentLog and onlinePaymentStatus added to invoice response
  * added fields to QuoteResponse and QuoteChargeResponse
* Webhooks
  * Added ‘Quote edited’ webhook event
* Performance improvements for GET subscription endpoints
* New documentation for SSO/MFA login

#### <mark style="color:orange;">2024-01-12 - Release updates for API version 2.1</mark> <a href="#xb7pn" id="xb7pn"></a>

**New features**

* New endpoints
  * POST /InvoiceBatches - Generate invoice batch job
  * GET /InvoiceBatches/{batchIdentifier}/BatchLog - get invoice batch log
  * GET /InvoiceBatches, /InvoiceBatches/{id} - get invoice batches and batch by id
  * GET /InvoiceBatches/BatchJobStatus/{batchReference} - check invoice batch job status
  * GET /InvoiceBatches/{batchIdentifier}/BatchLog - Get invoice batch log
* New query filters `modifiedBefore`, `modifiedAfter` for paged endpoints - allows filtering on modified date on sub-entities, such as custom fields and eg. order product charges on get subscriptions. API reference contains more details on where the filter is applied on specific endpoints
* Added Webhook events
  * Invoice batch posted
  * invoice batch created
  * invoice batch cancelled
* Fixes and changes
  * creating, deleting, and editing addresses on an account now triggers account updated webhook
  * Field `quoteEsignings` added to quote response

#### <mark style="color:orange;">2023-11-16 - Release updates for API version 2.1</mark> <a href="#m7ve6" id="m7ve6"></a>

**New Features**

* New Endpoints
  * POST /Payments - Create payments
  * PATCH /Payments/Settlements - Add, delete and update Payments and write-offs
  * POST /Orders/Charges/{id}/InvoicedTo - set invoiced to date on order product charge
  * GET /Products/FromCharge/{id} - get product from charge id
  * GET /Products/FromChargePlan/{id} - get product from chargePlanId
* Added Webhook events
  * Create Payments
  * Post Payments
* Added field `chargeId` on OrderProductChargeResponse
* Performance improvements for GET single subscription endpoints

#### <mark style="color:orange;">2023-08-17 - Release updates for API version 2.1</mark> <a href="#rspht" id="rspht"></a>

**New features**

* Invoice endpoints:
  * POST /Invoices/{id}/Cancel - Cancel Invoice
  * POST /Invoices/{id}/Post - Post Invoice
  * POST /Invoices/Orders/{id} - Generate Invoice from Order
  * POST /Invoices/{id}/Credit - Generate Credit Invoice
* Payment endpoints
  * GET /Payments
  * GET /Payments/{id}
* New Journal Endpoints for fetching accounting transactions (vouchers)
  * GET /Journals/{id}/AccountingTransactions - Get accounting transactions by journal id
  * GET /Journals/AccountingTransactions/{fiscalYear} - Get accounting transactions by fiscal year
  * GET /Journals/AccountingTransactions/{year}/FiscalQuarter/{quarter} - Get accounting transactions by fiscal year and quarter
  * GET /Journals/AccountingTransactions/{year}/FiscalPeriod/{period} - Get accounting transactions by fiscal year and period
  * GET /Journals/AccountingTransactions/{year}/FinancialAccount/{financialAccount}- Get accounting transactions by financial account (code or id)
* Order endpoints for fetching order product charges
  * GET /Orders/Products/{id}/Charges
  * GET /Orders/{id}/Charges
* Added Webhook events
  * Subscription deleted
  * Sales order deleted
  * Sales order updated
  * Sales order activated
  * Invoice updated

**Fixes and improvements**

* Validations on creating measurements now allow recurring charges to be added.
* Custom fields added on journal.voucher.transactions to include financial dimensions.
* Fields Created and Modified added to all relevant response models.
* Webhooks are now triggered when doing a delivery/partial delivery of stock products
* Improved input for invoice batch group on Post and Patch on Subscriptions, SalesOrders and Account endpoints
* Improved filtering for get endpoints

Documentation

* Added documentation to query filtering.
* Webhooks section has been updated and moved to a separate page
* Section about Invoice operation added

#### <mark style="color:orange;">2023-06-09 - Release updates for API version 2.1</mark> <a href="#ptpqw" id="ptpqw"></a>

**New features**

* New endpoints:
  * PATCH /product/{id}
  * PATCH /Product/Charge/{id}
  * DELETE /Product/{id}
  * DELETE /Product/ChargePlans/{id}
  * DELETE /Product/Charges/{id}
* Added InvoiceSettingGroup field to all account endpoints
* Added orderedQuantity and remainingQuantity fields to all subscription and sales order endpoints

**Documentation**

* Added product guide for creating, patching, and deleting Products.

#### <mark style="color:orange;">2023-04-26 - Release updates for API 2.1</mark> <a href="#iz5wz" id="iz5wz"></a>

**New features**

* New endpoints:
  * GET /Reports
  * GET /Reports/{id}
  * GET Reports/{id}/Data - Get report data by report id
  * GET RevenueSchedule/Charge/{id}
  * GET RevenueSchedule/InvoiceLine/{id}
  * POST Subscriptions/Activate/{id}
  * POST SalesOrders/Activate/{id}
* Fixes
  * For change subscription: Adding quantity to a charge with price model volume or rated will no longer return a validation error

#### <mark style="color:orange;">2023-03-08 - Release updates for API versions 2.0 and 2.1</mark> <a href="#ihh1z" id="ihh1z"></a>

**New features**

* Notifications were added for failed webhooks and failed jobs. (settings in UI)

#### <mark style="color:orange;">2023-02-22 - Release updates for API versions 2.0 and 2.1</mark> <a href="#e81cx" id="e81cx"></a>

**New features**

* Automatic retries for failing webhooks

**Documentation**

* New page with more detailed information about webhooks.

**Fixes**

* Improved webhook performance

#### <mark style="color:orange;">2022-12-17 - Release updates for API versions 2.0 and 2.1</mark> <a href="#swzdz" id="swzdz"></a>

**New features:**

* Authentication to a legal entity is possible with both id and Name
* OrderBillingPeriod on order level added to Post Subscription endpoints
* AccountParentId added to account response

**Fixes**

* Default custom fields values are added upon entity creation
* PeriodAlignmentDate added for priodAlignment: “align to date” on OrderProductCharge

#### <mark style="color:orange;">2022-12-17 - Release updates for API versions 2.0 and 2.1</mark> <a href="#id-3ewnn" id="id-3ewnn"></a>

**New features:**

* New Endpoints:
  * POST /Subscription/revert/{id}
  * POST /Invoices/onAccountInvoices
  * PATCH /Invoices
* Webhooks for revert order
* Added full quote on quoteConvertedResponse.
* Added chargePlanId and orderProductId fields to invoiceLine
* Improved error handling on LookupKey

**Fixes**

* Lookupkey serialization improved with error messages and null handling.
* GET and DELETE Webhooks/{id} return 400 instead of 404 on errors
* PricesDetails discount calculation

#### <mark style="color:orange;">2022-10-19 - Release updates for API versions 2.0 and 2.1</mark> <a href="#jinvi" id="jinvi"></a>

**New Features:**

* New endpoints:
  * GET /CustomFieldConfigurations
  * GET /CustomFieldConfigurations by Key and entity
  * GET /CustomFieldConfigurations by Id
  * Create CustomFieldsconfigurations
  * Update CustomFieldConfigurations
* Create Subscriptions and Create SalesOrders supports Adding OrderDiscounts.
* Change Subscriptions supports adding, removing and changing OrderDiscounts.
* BuyersReference added to SubscriptionsResponse
* Improved Errorhandling messages

#### <mark style="color:orange;">2022-08-24 - Release updates for API versions 2.0 and 2.1</mark> <a href="#b7ftv" id="b7ftv"></a>

**New endpoints**

* POST /Products - Create product
* GET /TaxTemplates
* GET /Countries

**Bugs and Issues fixed:**

* Id field added to InvoiceLineResponse.
* OrderChargeId and OrderChargeNumber on Voucher are now returning their values.
* EstimatedUsage and estimatedQuantity added to charge level on Create, Change, and Get Subscription.
* InvoiceBatchGroup added to subscriptionsResponse.
* The issue with patching addresses on Accounts is fixed.

#### <mark style="color:orange;">2022-07-15 - Updates</mark> <a href="#lhq2p" id="lhq2p"></a>

**Portal updates**

* The Swagger documentation pages for sandbox and old references will no longer be accessible.
* There will be a Link in the API menu to the API references to the Sandbox environment.
* Different references for version will be accessible via the API list.

**Bugs and Issues fixed for API version 2.0 and 2.1:**

* Id field added to InvoiceLineResponse.
* OrderChargeId and OrderChargeNumber on Voucher are now returning their values.
* EstimatedUsage and estimatedQuantity added to charge level on Create, Change, and Get Subscription.
* invoiceBatchGroup added to subscriptionsResponse.
* Issue with patching addresses on Accounts fixed.
* Differences in Webhook Response body for Invoices fixed. (The displayed response in the UI is still incorrect and will be fixed, showing enums as ints and null values).

#### <mark style="color:orange;">2022-06-21 - Release updates for API versions 2.0 and 2.1</mark> <a href="#m8qcr" id="m8qcr"></a>

**New API features:**

* New Webhooks added for Quotes:
  * "quoteCreated"
  * "quoteEdited"
  * "quoteConverted"
* New endpoint: GET SalesOrders/{id}/version
* New endpoint: GET SalesOrders/{orderNumber}/versions
* New endpoint: GET SalesOrders/{orderNumber}/versions/{version}
* GET Subscription/{id}/versions/{version} removed and replaced with two new endpoints:
  * GET Subscription/{id}/version Get a Subscription version by Id
  * GET Subscription/{orderNumber}/versions/{version} Get a specific version by orderNumber.

&#x20;

**Bugs and Issues fixed:**

* GET /Orders/{id} now returns any version of a SalesOrder or a Subscription.
* Correct error message added to Get subscription versions.
* Validating data on Create Measurements and Create Usage is optional and set with the validateData property in the request body. It is advised to set it to true.
* Create Webhooks now validate that the webhook exists and is set correctly when added.
* Quotes/convertToOrder now return a QuoteConvertedResponse with further details about the converted Quote and the new order.
* Quotes/convertToOrder: Added validations to ensure there is a connected address when converting to an Active Order.
* Fixed 500-error-issue related to LineDiscountAmount on Create Subscription is now fixed.
* Fixed issue with Setting StartMilestone and EndMilestone on charges to an existing milestone.
* Fixed SettledAmount on InvoiceResponse.

#### <mark style="color:orange;">2022-05-25 - Upcoming changes</mark> <a href="#blufn" id="blufn"></a>

* The old swagger documentation will soon be removed permanently.
* Documentation for Sandbox and Version 2.0 will be added to the API List.

#### <mark style="color:orange;">2022-05-25 - Release updates for API versions 2.0 and 2.1</mark> <a href="#ufcge" id="ufcge"></a>

**New API endpoints:**

* Change Subscription - POST /Subscription/{id}/Change
* Edit and create OrderDiscounts - POST /Subscriptions/{id}/OrderDiscounts
* Import Usage - POST Usage/Import
* Import Measurements - POST Measurements/Import

**Bugs and Issues fixed:**

* Validations added for Create Usage and Create Measurements to prevent faulty data.
  * OrderCharges must be of the correct ChargeType (usage or measurements).
  * If Account, order, product, and charge don't align the request will fail. For example, if passing an order and charge where the charge doesn't exist on the order the request will fail.
* InvoiceLines on InvoiceResponse now include fields TaxCategory and TaxRate
* QuoteResponse now includes field ConvertedToOrder
* Cancel-, Create- and Renew Subscriptions now validates that the action is allowed based on OrderStatus.
* Set Subscription milestones will now return the created Milestones Id.
* InvoiceAttachent endpoints return the correct error message.
* Properties in nested objects in Patch-requests are now handled correctly and are not ignored.
* Get Usage returns charge and product correctly.
* Field ReminderEmailAddress now gets patched correctly on Edit Account
* AccountResponse now includes fields ReminderEmailAddress
