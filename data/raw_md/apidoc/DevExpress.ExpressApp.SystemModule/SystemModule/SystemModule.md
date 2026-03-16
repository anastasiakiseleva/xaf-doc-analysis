---
uid: DevExpress.ExpressApp.SystemModule.SystemModule
name: SystemModule
type: Class
summary: The module contained in the _DevExpress.ExpressApp.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class SystemModule : ModuleBase, IModelXmlConverter, IModelNodeUpdater<IModelOptions>, IModelNodeUpdater<IModelListView>, IModelNodeUpdater<IModelLayoutManagerOptions>'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.SystemModule._members
  altText: SystemModule Members
- linkId: "118046"
---
The [System Module](xref:118046) comprises the following assemblies:

DevExpress.ExpressApp.v<:xx.x:>.dll
:   Contains base classes and services that are used by **DevExpress.ExpressApp.Blazor** and **DevExpress.ExpressApp.Win** assemblies.
DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll
:   Contains classes that are required in Blazor applications.
DevExpress.ExpressApp.Win.v<:xx.x:>.dll
:   Contains classes that are required in Windows Forms applications.

The **`SystemModule`** class exposes properties that determine the behavior of system functionality.