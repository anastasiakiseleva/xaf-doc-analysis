XAF uses the first registered Object Space Provider for the following purposes:
* To get [XafApplication.ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider) and [XafApplication.ConnectionString](xref:DevExpress.ExpressApp.XafApplication.ConnectionString) property values.
* To pass this Provider as the [CustomCheckCompatibilityEventArgs](xref:DevExpress.ExpressApp.CustomCheckCompatibilityEventArgs) `ObjectSpaceProvider` argument.
* To [update an application](xref:113239).

Ensure that `NonPersistentObjectSpaceProvider` is not the first registered Provider in your application.
