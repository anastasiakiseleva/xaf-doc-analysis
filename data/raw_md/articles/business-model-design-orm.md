---
uid: "113664"
seealso:
- linkId: "112600"
- linkId: "401886"
- linkType: HRef
  linkId: https://www.youtube.com/watch?v=vKivMXbsukc
  altText: "Cross-Platform .NET App UI: Desktop & Web Business Apps in Hours (DevExpress XAF Introduction)"
title: Storage, ORM, and Business Model Design
---
# Storage, ORM, and Business Model Design

XAF allows you to build a Business Model with the following ORM tools:

{|
|-
! ORM
! Modeling Approaches
|-
| [Entity Framework Core by Microsoft](https://learn.microsoft.com/en-us/ef/core/) ([Documentation](https://learn.microsoft.com/en-us/ef/core/get-started/))
| - Code First
- Model First
- Database First
|-
| [XPO ORM by DevExpress](https://www.devexpress.com/Products/NET/ORM/) ([Documentation](xref:1998))
| - Code First
- Model First
- Database First
|}

Refer to the following topic for an ORM comparison table: [](xref:404186)

> [!TIP]
> 
> To manage and display data not obtained from ORM, use [non-persistent objects](xref:116516).


## Business Classes

A business class is a model of a real-world object your application operates with (for example, Contact, Address, Task, etc.) Each class that takes part in an XAF UI construction process is a business class, and can be a class mapped to a database table -- Entity Framework **Entity** or XPO **Persistent Object**. 

XAF collects your business classes and generates [UI elements](xref:112607) for them. 

If you do not need to persist an object state to the database, you can declare a regular class and apply the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) attribute to it -- such a class also takes part in UI construction. Refer to the following topic for more details: [Non-Persistent Objects](xref:116516).

> [!NOTE]
> Refer to the following documentation section for information on _Data Types_ for which XAF can automatically generate a UI: [Data Types Supported by built-in Editors](xref:113014).
> 
> If the type you need to use can be displayed in the UI but the ORM tool you use cannot store this type in a database, refer to the following article: [Mapping Complex Types to the Database](xref:113655).
