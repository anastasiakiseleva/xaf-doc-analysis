---
uid: DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute
name: FriendlyKeyPropertyAttribute
type: Class
summary: Specifies the property which is considered an analog of the **GUID** property, to allow use of more suitable values.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface)]
    public class FriendlyKeyPropertyAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute._members
  altText: FriendlyKeyPropertyAttribute Members
- linkId: "112701"
- linkId: "113285"
---
Normally, business classes have a persistent property which represents an identifier. This identifier is usually more suitable than a GUID. To inform the system of these identifier-like properties, apply the **FriendlyKeyProperty** attribute to a business class, and pass the identifier-like property as the [FriendlyKeyPropertyAttribute.MemberName](xref:DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute.MemberName) parameter. In XAF applications, the properties that use that attribute are involved in the following:

* Used in object caption format (see [](xref:DevExpress.Persistent.Base.ObjectCaptionFormatAttribute)).
* Displayed in List Views of Lookup Property Editors.
* Considered as the default property if there are no properties decorated with the [DefaultProperty](xref:112701) attribute (including inherited properties), or the business class does not declare a property that contains **Name** as its part (excluding inherited properties).

The name of the property passed as the **FriendlyKeyProperty** attribute's parameter is set for the [IModelClass.FriendlyKeyProperty](xref:DevExpress.ExpressApp.Model.IModelClass.FriendlyKeyProperty) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node.

> [!NOTE]
> To add a column that corresponds to an identifier-like property to a Lookup List View, apply the **FriendlyKey** attribute in code.

In the example below, the **FriendlyKeyProperty** attribute is applied to the Contact class. As a result, the FullName property is considered as an identifier by the system.

# [C#](#tab/tabid-csharp)

```csharp
[FriendlyKeyProperty(nameof(FullName))]
public class Contact : Person {
   //...
}
```
***