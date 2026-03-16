---
uid: DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.CompatibilityError
name: CompatibilityError
type: Property
summary: Returns the database and application compatibility error.
syntax:
  content: public CompatibilityError CompatibilityError { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Updating.CompatibilityError
    description: '`CompatibilityDatabaseIsOldError`, `CompatibilityUnableToOpenDatabaseError`, or `null` if there is no errors.'
seealso: []
---
Use this property to identify the error that occurred while checking the compatibility of the application and its database. The error can be of the following types:
* `CompatibilityDatabaseIsOldError`
* `CompatibilityUnableToOpenDatabaseError`