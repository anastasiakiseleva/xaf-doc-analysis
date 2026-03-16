---
uid: '113146'
seealso:
  - linkId: '113596'
  - linkId: '113141'
  - linkId: '3311'
  - linkId: '2026'
  - linkId: '2028'
  - linkType: HRef
    linkId: 'https://supportcenter.devexpress.com/ticket/details/t639653/web-how-to-avoid-issues-with-data-bound-controls-due-to-missing-or-non-unique-key-values'
    altText: Web - How to avoid issues with data-bound controls due to missing or non-unique key values
title: Base Persistent Classes
owner: Ekaterina Kiseleva
---
# Base Persistent Classes

This topic describes the base persistent classes that can be used in XAF applications when creating a data model with XPO.

The following table lists the base persistent classes you can inherit from when you define persistent business classes:

| Persistent Class | Namespace | Supported Concurrency Control | Contains the Auto-Generated Primary Key Property | Supports Deferred Deletion |
|---|---|---|---|---|
| [](xref:DevExpress.Xpo.XPLiteObject) | [](xref:DevExpress.Xpo) | None ("Last in wins") | No | No |
| [](xref:DevExpress.Xpo.XPBaseObject) | [](xref:DevExpress.Xpo) | Optimistic | No | No |
| [](xref:DevExpress.Xpo.XPCustomObject) | [](xref:DevExpress.Xpo) | Optimistic | No | Yes |
| [](xref:DevExpress.Xpo.XPObject) | [](xref:DevExpress.Xpo) | Optimistic | Yes. Integer type. | Yes |
| [](xref:DevExpress.Persistent.BaseImpl.BaseObject) | [](xref:DevExpress.Persistent.BaseImpl) | Optimistic | Yes. Guid type. | Yes |

The **BaseObject** class is used when creating business classes from the **XPO Business Object** template. It is a feature-rich persistent class that supports the optimistic concurrency control (optimistic locking mechanism).

We recommend using the **XPObject** class if your business class should use the integer type primary key. This class also supports optimistic concurrency control.

You need to define the primary key property in the business class declaration if you are using classes which do not have the auto-generated primary key property. The following code snippet illustrates this:

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel;
using DevExpress.Persistent.Base;
using DevExpress.Xpo;
//...
[DefaultClassOptions]
public class MyClass : XPLiteObject {
    public MyClass(Session session) : base(session) { }
    [Key(AutoGenerate = true), Browsable(false)]
    public int Oid { get; set; }
    string fMyProperty;
    public string MyProperty {
        get { return fMyProperty; }
        set { SetPropertyValue(nameof(MyProperty), ref fMyProperty, value); }
    }
}
```
***

[`DefaultClassOptions`]: xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute
[`XPLiteObject`]: xref:DevExpress.Xpo.XPLiteObject
[`Key`]: xref:DevExpress.Xpo.KeyAttribute
[`Browsable`]: xref:System.ComponentModel.BrowsableAttribute
[`Session`]: xref:DevExpress.Xpo.Session

If you need to consider whether to use a base class that supports the deferred deletion feature, refer to the XPO documentation: [Deleting Persistent Objects](xref:2026).

You can implement a custom base persistent class. To learn more, refer to the [How to: Implement a Custom Base Persistent Class](xref:113325) help topic.
