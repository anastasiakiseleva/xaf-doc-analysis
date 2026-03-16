---
uid: DevExpress.ExpressApp.PivotGrid.PivotGridModule
name: PivotGridModule
type: Class
summary: The module contained in the _DevExpress.ExpressApp.PivotGrid.v<:xx.x:>.dll_ assembly.
syntax:
  content: |-
    [Browsable(true)]
    public sealed class PivotGridModule : ModuleBase
seealso:
- linkId: DevExpress.ExpressApp.PivotGrid.PivotGridModule._members
  altText: PivotGridModule Members
- linkId: "113303"
---
The [Pivot Grid Module](xref:113303) comprises two assemblies:

* _DevExpress.ExpressApp.PivotGrid.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by the **DevExpress.ExpressApp.PivotGrid.Win** assembly.
    
    This assembly contains the `PivotGridModule` class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.PivotGrid.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly represents a module, since it contains the `PivotGridWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `PivotGridModule` class exposes properties that determine the general behavior of pivot grid functionality.