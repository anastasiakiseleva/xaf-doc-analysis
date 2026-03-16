---
uid: DevExpress.Persistent.Base.ValueManager
name: ValueManager
type: Class
summary: An auxiliary class used to initialize value managers.
syntax:
  content: public class ValueManager
seealso:
- linkId: DevExpress.Persistent.Base.ValueManager._members
  altText: ValueManager Members
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/k18240/how-and-where-to-store-global-application-settings-and-user-data
  altText: How to save an application's settings at runtime and then access them via a common interface from Windows Forms module
---
A common task in a business application is to store temporary data accessible from any part of the application on a per-user basis. This task is solved differently under different platforms. For example, in a Windows Forms application, static properties may be suitable, while in Blazor values need to be stored separately for each user. In the context of the XAF, this means that you would have to implement the business logic in two platform-specific ways, for instance, via two platform-specific [Controllers](xref:112621). The concept of value managers allows you to overcome this limitation, and have only one platform-independent Controller.

Value managers are instantiated via the `ValueManager.``GetValueManager\<ValueType>` method. This method initializes platform-specific value managers. The type of a value manager initialized via this method will be different in ASP.NET Core Blazor and Windows Forms applications. A value manager is an object which implements the [](xref:DevExpress.Persistent.Base.IValueManager`1) interface, and so has the [](xref:DevExpress.Persistent.Base.IValueManager`1.Value) property. This property returns a previously assigned value if it is available (use the [](xref:DevExpress.Persistent.Base.IValueManager`1.CanManageValue) property to check if a value is available). 

The following example demonstrates how to store a `string` value separately for each user in a Module, ViewController, or another appropriate class:

[!include[ValueManager-example](~/templates/ValueManager-example.md)]


