---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomObjectSpaceProvider
name: CreateCustomObjectSpaceProvider
type: Event
summary: Occurs when setting up the application.
syntax:
  content: public event EventHandler<CreateCustomObjectSpaceProviderEventArgs> CreateCustomObjectSpaceProvider
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider
---
Handle this event if you require the application to use a custom Object Space Provider. Use the handler's [CreateCustomObjectSpaceProviderEventArgs.Connection](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.Connection) and [CreateCustomObjectSpaceProviderEventArgs.ConnectionString](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ConnectionString) parameters to get the connection type and connection string that are set for the application. The created Object Space Provider should be set for the handler's [CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProvider](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProvider) parameter, so that the default Object Space Provider is not created.

You can also pass several Object Space Providers to the [CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProviders](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProviders) parameter. In this instance, the Object Space Provider appropriate for each particular business object type is determined automatically. However, if you want to create an Object Space manually, use an overload of the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method that takes the _objectType_ parameter.

The Object Space Providers list is assigned to the [XafApplication.ObjectSpaceProviders](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProviders) property. Created Object Space Providers are not disposed automatically, and each provider keeps an SQL connection active. You should manually dispose of them when they are not required.

[!include[MultipleOSProvidersNote](~/templates/multipleosprovidersnote11196.md)]