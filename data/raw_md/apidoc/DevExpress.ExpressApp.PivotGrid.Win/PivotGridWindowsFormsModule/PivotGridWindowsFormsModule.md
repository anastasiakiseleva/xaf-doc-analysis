---
uid: DevExpress.ExpressApp.PivotGrid.Win.PivotGridWindowsFormsModule
name: PivotGridWindowsFormsModule
type: Class
summary: The module contained in the _DevExpress.ExpressApp.PivotGrid.Win.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class PivotGridWindowsFormsModule : ModuleBase'
seealso:
- linkId: DevExpress.ExpressApp.PivotGrid.Win.PivotGridWindowsFormsModule._members
  altText: PivotGridWindowsFormsModule Members
- linkId: "113303"
---
The [Pivot Grid Module](xref:113303) comprises two assemblies:

* _DevExpress.ExpressApp.PivotGrid.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by the **DevExpress.ExpressApp.PivotGrid.Win** assembly.
    
    This assembly contains the `PivotGrid` class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.PivotGrid.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly represents a module, since it contains the `PivotGridWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `PivotGridWindowsFormsModule` class exposes properties that determine the behavior of Windows Forms specific pivot grid functionality.