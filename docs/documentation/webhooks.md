---
description: >-
  Build near real-time integrations with API's and other Saas services. When a
  business event happens in Younium, a webhook event is placed in a queue that
  when executed will notify
---

# Webhooks

Webhooks are used to build near real-time integrations with API's and other Saas services. When a business event happens in Younium, a webhook event is placed in a queue that when executed will notify subscribers with an HTTP POST request. The request contains relevant information about the business event for the subscriber to use in the receiving system or platform.

An alternative to Webhooks is to make scheduled API requests on a frequent basis, using Webhooks is more efficient and normally provides a much better user experience.

The events that trigger a webhook may come from any source, meaning that that calls to the API, users actions in the UI as well as integrations will trigger the webhook.

## Available webhooks

### Subscribing to webhook event

Subscribing to webhook events can be done in the Younium app in settings>webhooks or using the [API webhook endpoint](https://developer.younium.com/guide/webhooks).\
The endpoint takes two parameters in the body: URL and Events. Events is a list of Event Tags, see Event tags in the table above.

Example (Sandbox):

```
POST <https://apisandbox.younium.com/Webhooks> 
```

Headers:

```
Authorization: Bearer [JWT token] Content-Type: application/json
```

Body:

```
{ 
  "url": "<https://your-service-url.com>", 
  "events": [ "AccountChanged" ] 
}
```

Response:

```
{ 
   "id": "49d5c950-925c-4863-f731-08dabe4f3d15", 
   "url": "<https://your-service-url.com>", 
   "events": [ 
      "AccountChanged", 
      ... //List of events that the webhook will listen to. 
   ], 
   "token": "g67g5fd7-s7d0-32a5-bd7e-df0dwas67c6", //All triggered webhook requests will contain this token. 
   "webhookStatus": "Enabled" 
}
```

### Webhook request body

Example of a webhook request body:

```
{ 
  "token": "g67g5fd7-s7d0-32a5-bd7e-df0dwas67c6", //Token to verify the request. 
  "eventId": "evt_sRzF5t6yO5DUdaDTM7da7s8EA", 
  "eventType": "AccountChanged", 
  "legalEntityName": "Legal-Entity-Name", 
  "legalEntityId": "rw8710de-5327-41a8-s32c-032s71db86ac", 
  "timestamp": "2022-11-03T14:00:55Z", 
  "triggeredBy": "et0771b7-3wr6-3s6a-a75e-7650910e6787", 
  "data": {...} //Entity-specific data, see requestBody links in the availabel webhooks list for reference. 
}
```

### Webhook request attempts and delivery

When a webhook event is executed a webhook attempt is created and a POST request is sent to the subscribing URL. In order for the attempt to be successful this request will require a successful response (response code 2xx). Any other response will be handled as a failed attempt. In the table below statuses for a failed webhook attempt are listed with descriptions.

```
Client error 4xx
The request has failed due to a client error on the client's side.
This can be due to access restrictions (401, 403), validation errors, BadRequest (400) or that the url is not found (404).

Client server error 5xx
Some errors have occurred on the client side, eg internal server error (500) or a service is unavailable (503). This will error may also indicate error has occurred in Younium causing the attempt to fail. If this is the case it will be stated in the error message.

RequestTimeout 500
This happens when the client takes too long to respond to the request causing the request to be canceled after 60 seconds.
When receiving and processing a webhook request on the client side it is important to return a successful response prior to executing any complex logic triggered by the webhook request.
```

The logs for webhook attempts can be found in settings>webhooks in the Younium app and will show all attempted requests over the past 15 days.

## Automatic and manual retries

If a webhook request fails it will automatically be resent every third hour until attempted retries reach 10 times. After that, it will need to be resent manually from the app.

## Error notifications

Notifications can be enabled in settings > notifications if a webhook request fails, notifying a user via the app notifications.

## Webhooks list

**Subscriptions:**

1. **SubscriptionUpdated** - Triggered when information is edited or when a stock product delivery is made, that doesn't require a change Subscription. Equivalent to patch Subscription.
2. **SubscriptionCancelled** - Triggered when a Subscription is cancelled.
3. **SubscriptionRenewed** - Triggered when a Subscription is renewed.
4. **SubscriptionReverted** - Triggered when a Subscription is reverted.
5. **SubscriptionDeleted** - Triggered when a Subscription is deleted.

Try it: [https://younium.gitbook.io/younium/api/subscriptions](https://younium.gitbook.io/younium/api/subscriptions)

#### SalesOrders:

1. **SalesOrderActivated** - Triggered when a new sales order is activated.
2. **SalesOrderUpdated** - Triggered when information is edited or when a stock product delivery is made.
3. **SalesOrderDeleted** - Triggered when a sales order is deleted.

Try it:&#x20;

#### Invoices:

1. **InvoicePosted** - Triggered when an Invoice is posted.
2. **InvoiceUpdated** - Triggered when an Invoice is updated.

Try it: [https://younium.gitbook.io/younium/api/invoices](https://younium.gitbook.io/younium/api/invoices)

#### Journals:

1. **JournalPosted** - Triggered when a Journal is posted.

Try it: [https://younium.gitbook.io/younium/api/journals](https://younium.gitbook.io/younium/api/journals)

#### Accounts:

1. **AccountsCreated** - Triggered when an Account is created.
2. **AccountsChanged** - Triggered when an Account is edited.

Try it: [https://younium.gitbook.io/younium/api/accounts](https://younium.gitbook.io/younium/api/accounts)

#### Quotes:

1. **QuoteCreated** - Triggered when a Quote is created.
2. **QuoteEdited** - Triggered when a Quote is edited.
3. **QuoteConverted** - Triggered when a Quote is converted to an Order.

Try it:  [https://younium.gitbook.io/younium/api/quotes](https://younium.gitbook.io/younium/api/quotes)

#### Payments:

1. **PaymentsCreated** - Triggered when a payment is created.
2. **PaymentsPosted** - Triggered when a payment is posted.

Try it: -

#### InvoiceBatches:

1. **InvoiceBatchCreated** - Triggered when an invoice batch is created.
2. **InvoiceBatchPosted** - Triggered when an invoice batch is posted.
3. **InvoiceBatchCancelled** - Triggered when an invoice batch is cancelled.

Try it: -

#### Products:

1. **ProductsCreated** - Triggered when a product is created.
2. **ProductsUpdated** - Triggered when a product is updated.
3. **ProductsDeleted -** Triggered when a Product is deleted. Body: Id and confirmation message.

Try it: [https://younium.gitbook.io/younium/api/products](https://younium.gitbook.io/younium/api/products)

