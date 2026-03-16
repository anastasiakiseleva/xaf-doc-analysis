---
uid: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeActionControl
name: CustomizeActionControl
type: Event
summary: Occurs when an [Action](xref:112622) control is created.
syntax:
  content: public event EventHandler<ActionControlEventArgs> CustomizeActionControl
seealso: []
---
> [!IMPORTANT]
> This event is designed to support the internal XAF infrastructure and should not be handled in your code. Use the [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event instead.

Below is an example of how to handle this event to customize the created control properties.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.XtraBars;
using DevExpress.XtraEditors.Repository;
// ...
public class CustomizeActionControlController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        Frame.GetController<ActionControlsSiteController>().CustomizeActionControl +=
            ActionControlsSiteController_CustomizeActionControl;
    }
    protected override void OnDeactivated() {
        Frame.GetController<ActionControlsSiteController>().CustomizeActionControl -=
           ActionControlsSiteController_CustomizeActionControl;
        base.OnDeactivated();
    }
    private void ActionControlsSiteController_CustomizeActionControl(object sender, ActionControlEventArgs e) {
        if (e.ActionControl.ActionId == "MyDateFilter") {
            BarEditItem barItem = (BarEditItem)e.ActionControl.NativeControl;
            barItem.Width = 170;
            RepositoryItemDateEdit repositoryItem = (RepositoryItemDateEdit)barItem.Edit;
            repositoryItem.Mask.UseMaskAsDisplayFormat = true;
            repositoryItem.Mask.EditMask = "yyyy-MMM-dd";
        }
    }
}
```
***

> [!TIP]
> If you need to create an alternate control rather than customize the default control's properties, handle the [ActionControlsSiteController.CustomAddActionControlToContainer](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomAddActionControlToContainer) and [ActionControlsSiteController.CustomBindActionControlToAction](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomBindActionControlToAction) events instead.