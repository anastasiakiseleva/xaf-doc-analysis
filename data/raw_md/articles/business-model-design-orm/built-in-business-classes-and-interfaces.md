---
uid: "112571"
seealso:
- linkId: "113173"
title: Built-in Business Classes & Interfaces
---
# Built-in Business Classes & Interfaces

The **XAF** features the **Business Class Library** with interfaces for XAF modules and the interface implementations for supported ORMs (XPO and EF Core).

The Business Class Library consists of the following assemblies:

DevExpress.Persistent.BaseImpl.Xpo[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]
:   Contains ready-to-use XPO persistent classes.
DevExpress.Persistent.BaseImpl.EFCore[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]
:   Contains ready-to-use Entity Framework Core classes.
DevExpress.Persistent.Base[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]
:   Contains interfaces and helper classes used in XAF [Additional Modules](xref:118046). Classes implementing these interfaces are available in the _DevExpress.Persistent.BaseImpl.*_ assemblies listed above.

> [!note]
> You can use XAF module-specific or service business classes that implement XAF module interfaces as is, like `ReportDataV2`, `FileData`, and `DashboardData`.

## Interfaces for XAF Modules

**Assembly:** _DevExpress.Persistent.Base[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_

Use service interfaces from the _DevExpress.Persistent.Base[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ assembly to integrate your business classes to XAF modules like [Security System](xref:113366).

**Examples:**

- [](xref:113452)
- [](xref:113384)
- [How to: Store file attachments in the file system instead of the database (XPO)
](https://supportcenter.devexpress.com/ticket/details/e965/how-to-store-file-attachments-in-the-file-system-instead-of-the-database-xpo-and-ef-core)
- [](xref:403288)
- [](xref:113672)
- [](xref:112837)
- [](xref:112839)
- [](xref:113689)
- [](xref:113051)

## Interface Implementations for Supported ORMs

**Assemblies:** 
- _DevExpress.Persistent.BaseImpl.Xpo[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ 
- _DevExpress.Persistent.BaseImpl.EFCore[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_

The Business Class Library allows you to do the following:

* Use classes from the _DevExpress.Persistent.BaseImpl\*\*\*.<:xx.x:>.dll_ assemblies.
* Extend persistent classes from the _DevExpress.Persistent.BaseImpl\*\*\*.<:xx.x:>.dll_ assemblies to add custom functionality.
* Use the _DevExpress.Persistent.BaseImpl\*\*\*.<:xx.x:>.dll_ assembly sources (shipped with the **XAF** installation) as an example when developing your own business class library.
* The Business Class Library assemblies do not have references to other XAF assemblies. This allows you to use services defined there (like validation, audit trail, etc.) in non-XAF applications.

To add a class from the Business Class Library to the UI construction process, use the [ModuleBase.AdditionalExportedTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes) property.

## Create Custom Classes with Class Names that Business Class Library Contains

 If your custom business classes are named the same way as classes from the **Business Class Library** (for example, `Event`), you receive the following errors:
 * _DuplicateModelNodeIdException_ at runtime or in the Model Editor.
 * _View layout collisions_ in the Model Editor.

To avoid these errors, use the `ModelNodesGeneratorSettings.SetIdPrefix` method as follows:
# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Updating;
using DevExpress.ExpressApp.Model.NodeGenerators;

namespace MySolution.Module {
    public sealed partial class SolutionNameModule : ModuleBase {
        public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
            base.CustomizeTypesInfo(typesInfo);
            ModelNodesGeneratorSettings.SetIdPrefix(
                typeof(MySolution.Module.BusinessObjects.Event),
                "EventEx"
            );
        }
    }
}
```
***
