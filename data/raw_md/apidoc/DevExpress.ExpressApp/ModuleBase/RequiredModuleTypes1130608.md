---
uid: DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes
name: RequiredModuleTypes
type: Property
summary: Provides access to the collection of modules that are added to the current module.
syntax:
  content: |-
    [Browsable(false)]
    public ModuleTypeList RequiredModuleTypes { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ModuleTypeList
    description: A **ModuleTypeList** collection of modules used by the current module.
seealso: []
---
Use this property to access the collection of the modules that are used by the current module. Use the **Add** method of the returned collection, to add a module to the current module directly. The following code demonstrates how to do this:

# [C#](#tab/tabid-csharp)

```csharp
public sealed class MySolutionModule : ModuleBase {
   //...
   public MySolutionModule() {
      InitializeComponent();
      this.RequiredModuleTypes.Add(typeof(MyCustomModule.CustomModule));
   }
}
```
***

The added module(s) must also be referenced in the current module project.