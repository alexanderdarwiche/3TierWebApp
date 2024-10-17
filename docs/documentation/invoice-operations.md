# Invoice operations

## Invoice operations <a href="#dy1q4" id="dy1q4"></a>

Some Invoice endpoints return an operation response that deals with the outcome in a different manner. Where most endpoints return a status code of 400 “Bad Request” if the call was not successful, the operation response returns a successful 2xx with a `message` or `successful` field indicating the result of the operation. Validation errors or similar errors in the request will still return a 400 bad request.

The operation response contains the following fields in its basic form

```
{ 
  id: "3078377a-f369-4176-acf9-08d751485f0b", 
  message: "Invoice was successfully cancelled",  
  successful: true 
}
```

The `id` contains the affected entity eg. a generated invoice. The field may be null and excluded if no id is present to return. The `successful` field whether the operation was successful and the `message` should always be included with further details on the outcome of the operation.

## Generation invoices <a href="#cijes" id="cijes"></a>

Generating invoices provides the possibility to both generate a draft and post the invoice in a single call. This is defined in the request field `invoiceAction` with some different option values:

* `CreateDraft` (default value) will generate a draft invoice.
* `CreateDraftAndPostInvoice` will generate a draft and then try to post the invoice. A draft is created even if the invoice fails to be posted. The response field `successful` is only true if the invoice is posted successfully.
* `CancelDraftIfPostFail` will generate a draft and then try to post the invoice. If the invoice fails to be posted the draft will be cancelled. The response field `successful` is only true if the invoice is posted successfully. The message will indicate that the draft was successfully canceled and why posting the invoice failed.
