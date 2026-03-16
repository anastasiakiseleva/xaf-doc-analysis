---
uid: DevExpress.ExpressApp.ShowViewStrategyBase.ShowViewFromCommonView(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.Actions.ActionBase)
name: ShowViewFromCommonView(View, Frame, ActionBase)
type: Method
summary: Shows a specific View in the same window in Single Document Interface mode, and in a new window or tab in Multiple Document Interface mode.
syntax:
  content: public void ShowViewFromCommonView(View view, Frame sourceFrame = null, ActionBase sourceAction = null)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A [View](xref:112611).
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    defaultValue: "null"
    description: A [Frame](xref:112608) object used by XAF to display a View.
  - id: sourceAction
    type: DevExpress.ExpressApp.Actions.ActionBase
    defaultValue: "null"
    description: If XAF displays a View as a result of an Action, this property contains a reference to the Action's instance.
seealso: []
---
The `ShowViewFromCommonView` method opens the specified View. 
* In [Single Document Interface](xref:DevExpress.ExpressApp.UIType.SingleWindowSDI) mode, XAF displays the View in the same window.
* In [Multiple Document Interface](xref:DevExpress.ExpressApp.UIType.TabbedMDI) mode, XAF displays the View in a new Frame (window or tab).

The following code sample creates a controller with action that opens a new ListView in the same window (in `SingleWindowSDI` mode) or in a separate tab (in `TabbedMDI` mode).

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MySolution.Module.BusinessObjects;

namespace MySolution.Blazor.Server.Controllers;

public class CustomBlazorController : ObjectViewController<DetailView, Contact> {
    public CustomBlazorController() {
        var myAction = new SimpleAction(this, "MyBlazorAction", PredefinedCategory.Edit);
        myAction.Execute += MyAction_Execute;
    }
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var objectSpace = Application.CreateObjectSpace(typeof(Contact));
        var listView = Application.CreateListView(typeof(Contact), true);
        Application.ShowViewStrategy.ShowViewFromCommonView(listView, this.Frame, (ActionBase)sender);
    }
}
```