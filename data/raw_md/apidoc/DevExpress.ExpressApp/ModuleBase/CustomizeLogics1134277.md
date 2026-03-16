---
uid: DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)
name: CustomizeLogics(CustomLogics)
type: Method
summary: Allows you to override domain logic classes registered for [Application Model](xref:112580) interfaces.
syntax:
  content: public virtual void CustomizeLogics(CustomLogics customLogics)
  parameters:
  - id: customLogics
    type: DevExpress.ExpressApp.DC.CustomLogics
    description: A [](xref:DevExpress.ExpressApp.DC.CustomLogics) object exposing methods to manage domain logic classes registered for Application Model interfaces.
seealso:
- linkId: "112580"
---
This method allows you to replace the default domain logic implementations used for the Application Model interfaces with custom ones. For this purpose, a [](xref:DevExpress.ExpressApp.DC.CustomLogics) object exposed by the _customLogics_ parameter supplies the [CustomLogics.RegisterLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.RegisterLogic(System.Type,System.Type)) and [CustomLogics.UnregisterLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.UnregisterLogic(System.Type,System.Type)) methods. The following code snippet illustrates their use. The [](xref:DevExpress.ExpressApp.Model.IModelDetailView) interface's **ModelDetailViewDomainLogic** is replaced by a custom **MyLogic** domain logic class. The custom logic class changes the default value of the [IModelView.AllowEdit](xref:DevExpress.ExpressApp.Model.IModelView.AllowEdit) property for all the [Detail Views](xref:112611) to **false**.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.DC.Xpo;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Model.DomainLogics;
//...
public sealed partial class MyModule : ModuleBase {
    //...
    public override void CustomizeLogics(CustomLogics customLogics) {
        base.CustomizeLogics(customLogics);
        customLogics.UnregisterLogic(typeof(IModelDetailView), typeof(ModelDetailViewDomainLogic));
        customLogics.RegisterLogic(typeof(IModelDetailView), typeof(MyLogic));        
    }
}
[DomainLogic(typeof(IModelDetailView))]
public static class MyLogic {
    public static bool Get_AllowEdit(IModelDetailView modelView) {
        return false;
    }
}
```
***