---
uid: DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
name: AddGeneratorUpdaters(ModelNodesGeneratorUpdaters)
type: Method
summary: Registers the Generator Updaters. These are classes, used to customize the [Application Model](xref:112580)'s zero layer after it has been generated.
syntax:
  content: public virtual void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters)
  parameters:
  - id: updaters
    type: DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters
    description: A **ModelNodesGeneratorUpdaters** object providing access to the list of Generator Updaters.
seealso:
- linkId: "112810"
---
Override this method and add one or more Generator Updaters (the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) descendants) in it. The _updaters_ parameter exposes the **Add** method, allowing you to register an Updater.

# [C#](#tab/tabid-csharp)

```csharp
public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters) {
    base.AddGeneratorUpdaters(updaters);
    updaters.Add(new MyGeneratorUpdater1());
    updaters.Add(new MyGeneratorUpdater2());
    // ...
}
```
***

To see a full example for implementing the Generator Updaters classes and registering them via this method, refer to the [How to: Create Additional ListView Nodes in Code using a Generator Updater](xref:113315) topic.