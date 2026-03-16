---
uid: DevExpress.ExpressApp.Frame.GetController``1
name: GetController<ControllerType>()
type: Method
summary: Returns a specified [Controller](xref:112621) from the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection.
syntax:
  content: |-
    public ControllerType GetController<ControllerType>()
        where ControllerType : Controller
  typeParameters:
  - id: ControllerType
    description: ''
  return:
    type: '{ControllerType}'
    description: A specified Controller found in the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection.
seealso:
- linkId: "112621"
---
Use the **GetController\<ControllerType>** method to access a particular Controller from the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection. The **ControllerType** generic type argument specifies the required Controller type. In this argument, you can specify any class which is a descendant of the [](xref:DevExpress.ExpressApp.Controller) class.

The code below demonstrates how to access the @DevExpress.ExpressApp.SystemModule.NewObjectViewController and add its **NewObjectAction** to the [Quick Access Toolbar](xref:2496).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

// ...
public class NewObjectActionController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        NewObjectViewController newObjectViewController = Window.GetController<NewObjectViewController>();
        if(newObjectViewController != null) {
            newObjectViewController.NewObjectAction.QuickAccess = true;
        }
    }
}
```
***

If there is no Controller of the specified type in the [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection, this method returns the first Controller which is assignable to this type.