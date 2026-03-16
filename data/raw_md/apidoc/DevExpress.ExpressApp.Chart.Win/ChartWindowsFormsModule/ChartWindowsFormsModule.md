---
uid: DevExpress.ExpressApp.Chart.Win.ChartWindowsFormsModule
name: ChartWindowsFormsModule
type: Class
summary: The module contained in the _DevExpress.ExpressApp.Chart.Win.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class ChartWindowsFormsModule : ModuleBase'
seealso:
- linkId: DevExpress.ExpressApp.Chart.Win.ChartWindowsFormsModule._members
  altText: ChartWindowsFormsModule Members
- linkId: "113302"
---
The [Chart Module](xref:113302) comprises three assemblies:

* _DevExpress.ExpressApp.Chart.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by both the **DevExpress.ExpressApp.Chart.Win** assembly.
    
    This assembly represents a module, since it contains the `ChartModule` class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.Chart.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly represents a module, since it contains the `ChartWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `ChartWindowsFormsModule` class exposes properties whose values determine the behavior of Windows Forms specific charting functionality.