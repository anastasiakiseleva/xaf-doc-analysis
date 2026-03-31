---
uid: "113665"
seealso:
- linkId: "402188"
title: Key Properties
---
# Key Properties

One of XAF's functions is managing a database using an ORM tool. Dealing with the database assumes that each object has a property that allows you to distinguish an object among other objects of the same type. In [relational databases](https://en.wikipedia.org/wiki/Relational_model), this property is called a [Unique key](https://en.wikipedia.org/wiki/Unique_key) (_primary key_ or a _key_). Each business class you create with an ORM tool must have a **key property** that will be used as a database's unique key. Key property implementation differs depending on the specific data access technology you use.

## Entity Framework (EF)
When using EF, you can implement a key property in one of the following ways:

* Inherit your class from the [DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) class that has the Guid key property (recommended).
* Implement a property named "Id".
* Implement a property that combines the class name and "Id", such as "ContactId" (assuming that your class name is "Contact").
* Decorate any property with the [Key Attribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.keyattribute).

For detailed information, refer to the [Keys](https://learn.microsoft.com/en-us/ef/core/modeling/keys?tabs=data-annotations) Microsoft article.

> [!IMPORTANT]
> [!include[composite-key-properties-template](~/templates/composite-key-properties-template.md)]

## XPO
In most XPO cases, you do not need to create the key property because it is usually already implemented in a class used as the base for your own XPO business class. Refer to the [Base Persistent Classes](xref:113146) help topic for more information about different base classes to inherit from and their key properties.

If you need to implement your own key property, inherit your new class from one of the [Base Persistent Classes](xref:113146) without a key ([](xref:DevExpress.Xpo.XPLiteObject), [](xref:DevExpress.Xpo.XPBaseObject) or [](xref:DevExpress.Xpo.XPCustomObject)), implement a key property manually, then decorate it with the [](xref:DevExpress.Xpo.KeyAttribute).

## Primary Key (PK) Type Considerations (Guid vs Integer)

For more information about business object implementation, overall usability, performance and module design considerations for object identifiers, or PK in your data models/database tables, review the following Support Center ticket: [Unique Identifiers/Guid (uniqueidentifier, uuid) or sequential/integer Int32/Int64 (int, bigint, IDENTITY) type as a primary key in database tables](https://supportcenter.devexpress.com/ticket/details/t1032674/xaf-unique-identifiers-guid-uniqueidentifier-uuid-or-sequential-integer-int32-int64-int).