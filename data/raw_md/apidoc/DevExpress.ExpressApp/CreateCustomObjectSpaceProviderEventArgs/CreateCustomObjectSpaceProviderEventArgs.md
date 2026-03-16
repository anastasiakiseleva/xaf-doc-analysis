---
uid: DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs
name: CreateCustomObjectSpaceProviderEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.CreateCustomObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.CreateCustomObjectSpaceProvider) event.
syntax:
  content: 'public class CreateCustomObjectSpaceProviderEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs._members
  altText: CreateCustomObjectSpaceProviderEventArgs Members
---
The **CreateCustomObjectSpaceProvider** event occurs when setting up the application. Handle this event if you require the application to use a custom Object Space Provider. Use the handler's [CreateCustomObjectSpaceProviderEventArgs.Connection](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.Connection) and [CreateCustomObjectSpaceProviderEventArgs.ConnectionString](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ConnectionString) properties to get the connection type and connection string that are set for the application. The created Object Space Provider should be set for the handler's [CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProvider](xref:DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.ObjectSpaceProvider) property, so that the default Object Space Provider is not created.