---
uid: "113655"
seealso: []
title: Mapping Complex Types to the Database
owner: Ekaterina Kiseleva
---
# Mapping Complex Types to the Database

XAF application supports the following ORMs: 
- [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)
- [XPO](https://www.devexpress.com/Products/NET/ORM/). 

Depending on ORM used in your application, you can store a number of data types in the database. Data Types that can be persisted directly are listed in the [Entity Data Model: Primitive Data Types](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/entity-data-model-primitive-data-types) and [Data Types Supported by XPO](xref:2003) articles.

To store an unsupported type in the database, you need to convert it to a supported one.

You can find code examples in the following articles:

* [Color Properties in XPO](xref:113659)
* [Color Properties in EF Core](xref:113660)

> [!NOTE]
> XPO provides the [](xref:DevExpress.Xpo.ValueConverterAttribute) used to persist types that are not supported by default.
