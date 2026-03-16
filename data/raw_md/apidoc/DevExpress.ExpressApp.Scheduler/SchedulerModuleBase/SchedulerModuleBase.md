---
uid: DevExpress.ExpressApp.Scheduler.SchedulerModuleBase
name: SchedulerModuleBase
type: Class
summary: The module contained in the _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public class SchedulerModuleBase : ModuleBase, IModelXmlConverter'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.SchedulerModuleBase._members
  altText: SchedulerModuleBase Members
- linkId: "112811"
---
The [Scheduler Module](xref:112811) comprises the following assemblies:

* _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by the **DevExpress.ExpressApp.Scheduler.Blazor** and **DevExpress.ExpressApp.Scheduler.Win** assemblies.
    
    This assembly contains the `SchedulerModuleBase` class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_
    
    Contains classes that are required in ASP.NET Core Blazor applications only.
    
    This assembly represents a module, since it contains the `SchedulerBlazorModule` class - a descendant of the `ModuleBase` class.

* _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly represents a module, since it contains the `SchedulerWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `SchedulerModuleBase` class exposes properties that determine the general behavior of scheduling functionality.