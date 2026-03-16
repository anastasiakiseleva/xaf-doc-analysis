---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerWindowsFormsModule
name: SchedulerWindowsFormsModule
type: Class
summary: The module contained in the _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class SchedulerWindowsFormsModule : SchedulerModuleBase'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.Win.SchedulerWindowsFormsModule._members
  altText: SchedulerWindowsFormsModule Members
- linkId: "112811"
---
The [Scheduler Module](xref:112811) comprises two assemblies:

* _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by the **DevExpress.ExpressApp.Scheduler.Win** assembly.
    
    This assembly contains the **`SchedulerModuleBase`** class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly contains the `SchedulerWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `SchedulerWindowsFormsModule` class exposes properties that determine the behavior of Windows Forms specific scheduling functionality.