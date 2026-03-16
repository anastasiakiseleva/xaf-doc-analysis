---
uid: DevExpress.ExpressApp.ShowViewParameters.Controllers
name: Controllers
type: Property
summary: A collection of [Controllers](xref:112621) that should be activated for the target [View](xref:112611) or its [Window](xref:112608).
syntax:
  content: public List<Controller> Controllers { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.Controller}
    description: A collection of Controllers.
seealso: []
---
When you display a View, the following Controllers are created:
* All Controllers from the [Application Model](xref:112580) that relate to your View or its Window. You can use the @DevExpress.ExpressApp.ShowViewParameters.CreateAllControllers option to disable this behavior.
* Controllers specified in the `Controllers` collection.

Use the `Controllers` property to create Controllers for the Frame or Window. You can also replace the default Controllers.

Your Controllers are active only if constraints like @DevExpress.ExpressApp.ViewController.TargetViewType or @DevExpress.ExpressApp.ViewController.TargetObjectType match. These constraints apply to your Controller's [Actions](xref:112622) as well. The [Action Containers](xref:112610) that display these Actions must exist in the Template for the target Window. Set the correct [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property for each Action.

> [!NOTE]
> Deactivate your Controllers when they are not needed. Use [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) for this purpose.


The following code sample adds @DevExpress.ExpressApp.SystemModule.DialogController to the `Controllers` collection. This controller is intended for use in popup Windows and you should manually add it to a popup Window's Controllers.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
// ...
void myAction_Execute(Object sender, SimpleActionExecuteEventArgs e) {
   IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(MyBusinessClass));
   string listViewId = Application.FindListViewId(typeof(MyBusinessClass));
   e.ShowViewParameters.CreatedView = Application.CreateListView(listViewId,
      Application.CreateCollectionSource(objectSpace,typeof(MyBusinessClass),listViewId),true);
   e.ShowViewParameters.TargetWindow = TargetWindow.NewWindow;
   e.ShowViewParameters.Controllers.Add(Application.CreateController<DialogController>());
}
```
***

If you invoke a popup Window with @DevExpress.ExpressApp.Actions.PopupWindowShowAction, the system automatically adds @DevExpress.ExpressApp.SystemModule.DialogController. You can use the [CustomizePopupWindowParamsEventArgs.DialogController](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.DialogController) parameter to replace it with your custom Controller.

> [!NOTE]
> If you display the target View in the current Window (Frame), the system does not add @DevExpress.ExpressApp.ShowViewParameters.Controllers to that Window (Frame).