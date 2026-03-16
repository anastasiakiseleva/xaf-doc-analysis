---
uid: "402925"
title: Queryable Mode (Database-Level Data Processing)
owner: Yekaterina Kiseleva
seealso: []
---
# Queryable Mode (Database-Level Data Processing)

## Queryable Mode Overview

Queryable mode improves performance when working with large data sets by processing operations like filtering and sorting at the database level rather than loading all data into memory.

## When to Use Database-Level Processing

Choose Queryable mode in the following scenarios:

* **Large data sets**: When working with multiple records where performance is critical
* **Lookup scenarios**: For lookup List Views that need to display extensive reference data
* **Memory-constrained environments**: When application memory use needs optimization
* **Network optimization**: When minimizing data transfer between database and application is important

Choose [Client](xref:118449) mode instead when:

* Working with smaller data sets
* You need full support for custom properties and complex calculations
* Advanced query syntaxes like [free joins](xref:8130) or [upcasting](xref:2650) are required

> [!Note]
> The default data access mode for lookup, root, and nested List Views in ASP.NET Core Blazor applications is [Client](xref:118449).

## How Database-Level Processing Works

In this mode, the collection source exposes an `IQueryable<T>` query shaped according to List View settings. The List Editor does not load all objects immediately. Instead, the editor control extends the query to load only objects visible in the control, then iterates the query to load objects from the database.

Database-level processing is automatically enabled for lookup List Views when the corresponding List View node in the Application Model specifies any data access mode other than [Client](xref:118449).

**Supported editors:**
* `LookupPropertyEditor`
* [DxTreeListEditor](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor) (ASP.NET Core Blazor)

## Limitations and Considerations

When using database-level processing, be aware of these limitations:

### Custom Properties Not Supported
* [Custom](xref:113583) persistent properties (`IModelMember.IsCalculated = false`) created in the Model Editor and `CustomizeTypesInfo` method are not displayed
* Custom properties added at runtime
* Non-persistent properties without [PersistentAlias](xref:DevExpress.Xpo.PersistentAliasAttribute) decoration (XPO)
* Non-persistent properties in EF Core

### Query Limitations
* Filter, sort, and group operations do not work with unsupported properties listed above
* Advanced query syntaxes are not supported:
  * [Single aggregate function](xref:4928#functions)
  * [Free Joins](xref:8130)
  * [Upcasting](xref:2650)

### Database Compatibility
* Legacy databases with compound primary keys are not supported

### Collection Behavior Changes
* Queryable collection sources create new collections from queries instead of using original collections
* Custom logic in original collection getters and event handlers is not executed
* All properties are calculated on-demand based on visibility and rule requirements