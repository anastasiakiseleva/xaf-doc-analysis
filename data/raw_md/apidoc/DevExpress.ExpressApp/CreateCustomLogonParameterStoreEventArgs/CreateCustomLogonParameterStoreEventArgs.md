---
uid: DevExpress.ExpressApp.CreateCustomLogonParameterStoreEventArgs
name: CreateCustomLogonParameterStoreEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.CreateCustomLogonParameterStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore) event.
syntax:
  content: 'public class CreateCustomLogonParameterStoreEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CreateCustomLogonParameterStoreEventArgs._members
  altText: CreateCustomLogonParameterStoreEventArgs Members
---
The **CreateCustomLogonParameterStoreArgs** class declares the [CreateCustomLogonParameterStoreEventArgs.Storage](xref:DevExpress.ExpressApp.CreateCustomLogonParameterStoreEventArgs.Storage) property specific to the [XafApplication.CreateCustomLogonParameterStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore) event which is designed to create a custom storage. This object will be used to load and save logon parameters to a specified location (database or registry).

This class is inherited from the **HandledEventArgs** class. So, you can set the handler's **Handled** parameter to **true** to prevent creation of a default storage.