---
uid: "112847"
seealso:
- linkId: "113325"
- linkId: "118557"
title: Ways to Add a Business Class
owner: Alexey Kazakov
---
# Ways to Add a Business Class

This topic describes how to add a business class to your application's data model.


## Code First

You can implement business classes from scratch or import them from external modules.


### Implement a Business Class from Scratch

Refer to the following help topics for information on how to implement business model with your ORM:

- [Implement Custom Business Classes (EF Core)](xref:402981).

### Import Classes from a Business Class Library or Module

> [!NOTE]
> **XPO**: When you add a class to the data model, all the referenced classes are also added.  
> **EF Core**: When you add a class to the data model, you should register all the business class' ancestors and referenced classes.

You can use existing classes from a Business Class Library or module. For this purpose, reference the assembly with these classes in a MySolution.Module project. 

[`AdditionalExportedTypes`]:xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes
[`ModuleBase`]:DevExpress.ExpressApp.ModuleBase
    
#### Import All Classes from an Assembly (In Code)


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
//...
public sealed class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        //...
        AdditionalExportedTypes.AddRange(
            ModuleHelper.CollectExportedTypesFromAssembly(
            typeof(MyNamespace.MyModule).Assembly, ExportedTypeHelpers.IsExportedType));
    }
}
```
***

#### Import Select Classes from an Assembly (In Code)
    
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
//...
public sealed class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        //...
        AdditionalExportedTypes.AddRange(
            new Type[] { typeof(Address), typeof(Note) });
    }
}
```
***

If you use EF Core, add all the new classes and their ancestors to the solution's DbContext.

# [C#](#tab/tabid-csharp-efonly)

```csharp
using MySolutionModule.BusinessObjects;

namespace  MySolutionModule.BusinessObjects {
    public class MySolutionDbContext : DbContext {
        //...
        public DbSet<Address> Addresses { get; set; }
        public DbSet<Note> Notes { get; set; }
    }
}
``` 

***

### Modify a Class from a Business Class Library or Module
    
You can modify a class from a Business Class Library or module in one of the following ways:

* Inherit from the class. 

    **Step-by-step instructions:**
	- [Implement Custom Business Classes (EF Core)](xref:402981).
* Modify the information on the class loaded to the [Application Model](xref:112580). For this purpose, invoke the [Model Editor](xref:112582) and navigate to the corresponding **BOModel** | **_\<Class\>_** node.


## Model First (XPO)

You can use the **XPO Data Model Designer** to build your application data model in a visual designer and generate the code of underlying business classes. 

**Step-by-step instructions:** [How to: Create a Business Model in the XPO Data Model Designer](xref:113450).


## Database First

If you already have a database with a set of tables, you can generate business classes that correspond to these tables.

**Step-by-step instructions:** 

- **XPO**: [How to: Generate XPO Business Classes for Existing Data Tables](xref:113451).
- **EF Core**: [](xref:402971)

