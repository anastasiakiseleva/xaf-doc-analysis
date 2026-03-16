---
uid: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction
name: ProcessCurrentObjectAction
type: Property
summary: Provides access to the **ListViewShowObject** Action.
syntax:
  content: public SimpleAction ProcessCurrentObjectAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Open** Action.
seealso: []
---
This Action invokes a Detail View representing the object that is double-clicked in the current List View, or for which ENTER is pressed (the [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController) class description contains details on this).

The **Open** Action's [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property is set to **ListView**. This means that the Action must be displayed by the **ListView** [ActionContainer](xref:112610). However, this Action Contianer is not included into built-in [Templates](xref:112609). So, the Action is not visualized.

If you want to customize the process of executing the Action, inherit from the **ListViewProcessCurrentObjectController** and override its **ExecuteProcessCurrentObject** method. Currently, this method calls the [ListViewProcessCurrentObjectController.ShowObject](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ShowObject(System.Object,DevExpress.ExpressApp.ShowViewParameters,DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.View)) method, which invokes a Detail View.

By default, the **ListViewShowObject** Action is active when the **ListViewProcessCurrentObjectController** is active, and when a single object is selected in the current List View. To ascertain why the Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

namespace YourSolutionName.Module.Controllers;
public class CustomControllerReport : ObjectViewController<ListView, Contact> {
    ListViewProcessCurrentObjectController processObjectController;
    protected override void OnActivated() {
        base.OnActivated();
        processObjectController = Frame.GetController<ListViewProcessCurrentObjectController>();
        if(processObjectController != null) {
            processObjectController.ProcessCurrentObjectAction.Active["myreason"] = false;
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(processObjectController != null) {
            processObjectController.ProcessCurrentObjectAction.Active.RemoveItem("myreason");
        }
    }
}
```

Information on the **ListViewShowObject** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).

If you require that another Action is executed instead of the **Open** Action, handle the [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event.
