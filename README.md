1. No Transaction Management (Major Issue)

The product is committed to the database first.

Inventory is committed in a separate operation.

If inventory creation fails, the product remains saved.

Impact:

Leads to data inconsistency

Orphan product records without inventory

2. Multiple Commits

Two separate db.session.commit() calls are used.

Impact:

Partial data persistence

Increased risk of inconsistent state

Poor performance due to multiple database commits

3. No Error Handling

No try/except block is implemented.

Any runtime or database error results in an unhandled 500 response.

Impact:

Application crashes

No graceful error response to clients

4. No Rollback on Failure

Database session is not rolled back if an error occurs.

Impact:

Corrupted or incomplete data remains in the database

Manual cleanup may be required

5. No Input Validation

Required fields are not validated.

Missing fields cause KeyError.

Negative values for price or quantity are allowed.

Impact:

Invalid business data stored

Runtime exceptions during request handling

6. Unsafe request.json Usage

Uses request.json directly without validation.

If request body is empty or invalid, request.json becomes None.

Impact:

Causes runtime errors such as TypeError: 'NoneType' object is not subscriptable
