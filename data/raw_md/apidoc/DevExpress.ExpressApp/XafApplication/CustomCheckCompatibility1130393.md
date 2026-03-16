---
uid: DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility
name: CustomCheckCompatibility
type: Event
summary: Occurs when the application accesses the database.
syntax:
  content: public event EventHandler<CustomCheckCompatibilityEventArgs> CustomCheckCompatibility
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.ApplicationName
- linkId: 113239#how-database-is-updated-in-debug-mode
  altText: How Database is Updated in Debug Mode
---
When the application accesses the database, XAF checks the database and application compatibility. Handle the `CustomCheckCompatibility` event to perform a custom check of the application and database compatibility, update the database, or perform other actions. 

Set the @System.ComponentModel.HandledEventArgs.Handled parameter to `true`, to cancel the default actions.