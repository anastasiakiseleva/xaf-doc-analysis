---
uid: DevExpress.Persistent.BaseImpl.BaseObject
name: BaseObject
type: Class
summary: Represents a [base persistent class](xref:113146) from which [business classes](xref:112570) can be inherited.
syntax:
  content: |-
    [NonPersistent]
    public abstract class BaseObject : XPCustomObject
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject._members
  altText: BaseObject Members
- linkId: "3311"
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.OidInitializationMode
---
The **BaseObject** class is a feature-rich persistent base class. The **BaseObject** class is used as the base class when declaring business classes using the **XPO Business Object** template. The **BaseObject** class's main features are:

* A GUID-type auto-generated [BaseObject.Oid](xref:DevExpress.Persistent.BaseImpl.BaseObject.Oid) primary key property;
* Supports optimistic concurrency control;
* Supports deferred deletion.

[!include[](~/templates/baseobject_codesnippet.md)]

Business classes are inherited from a base persistent class. The [Ways to Add a Business Class](xref:112847) topic describes how to declare a business class, and the [How to: Implement a Custom Base Persistent Class](xref:113325) help topic provides details on how to implement a custom base persistent class. The [Business Classes vs Database Tables](xref:112570) topic provides a general overview of the business class concept.

> [!NOTE]
> XAF manages persistent objects via Object Spaces. Refer to the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class description for more information about the Object Space concept.