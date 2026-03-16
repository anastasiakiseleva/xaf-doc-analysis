---
uid: DevExpress.ExpressApp.TreeListEditors.TreeListEditorsModuleBase
name: TreeListEditorsModuleBase
type: Class
summary: The module contained in the _DevExpress.ExpressApp.TreeListEditors.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public class TreeListEditorsModuleBase : ModuleBase'
seealso:
- linkId: DevExpress.ExpressApp.TreeListEditors.TreeListEditorsModuleBase._members
  altText: TreeListEditorsModuleBase Members
- linkId: "112841"
---
The [TreeList Editors Module](xref:112841) comprises two assemblies:

* _DevExpress.ExpressApp.TreeListEditors.v<:xx.x:>.dll_
    
    Contains base classes and services that are used by the **DevExpress.ExpressApp.TreeListEditors.Win** assembly.
    
    This assembly contains the `TreeListEditorsModuleBase` class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class.
* _DevExpress.ExpressApp.TreeListEditors.Win.v<:xx.x:>.dll_
    
    Contains classes that are required in Windows Forms applications only.
    
    This assembly contains the `TreeListEditorsWindowsFormsModule` class - a descendant of the `ModuleBase` class.

The `TreeListEditorsModuleBase` class exposes properties that determine the general behavior of tree list functionality.