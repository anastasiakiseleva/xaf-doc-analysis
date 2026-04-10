The following features should not be used together:

* XPO [Object Space Provider](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders) registered with the [XPObjectSpaceProviderOptions.ThreadSafe](xref:DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.ThreadSafe) option set to `true` (this parameter enables [](xref:DevExpress.Xpo.ThreadSafeDataLayer)).

* An Administrator's Model Differences [stored in the database](xref:113698) using the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) event (you can still store the User's differences in the database using the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event).

* [Custom Persistent Fields](xref:113583) declared in the Administrator's Model Differences.

With this configuration, your application loads information on custom persistent fields from the database and then updates the database schema. However, a thread-safe data layer does not support altering the data model after the database connection is established.