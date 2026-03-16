---
uid: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem
name: CustomProcessSelectedItem
type: Event
summary: Occurs before the **ListViewShowObject** Action ([ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction)) is executed in List Views with @DevExpress.ExpressApp.ListView.MasterDetailMode set to `ListViewOnly`.
syntax:
  content: public event EventHandler<CustomProcessListViewSelectedItemEventArgs> CustomProcessSelectedItem
seealso: []
---
When a user clicks an object in the current List View (double click in Windows Forms) or selects an object and presses Enter, XAF executes the **ListViewShowObject** Action. This Action invokes a Detail View for the selected object.

Handle the `CustomProcessSelectedItem` event to execute a custom Action instead of the **ListViewShowObject** Action in specific List Views. For example, the Windows Forms **`ReportsController`** invokes the Report Designer, while the ASP.NET Core Blazor `ReportsController` invokes the Report Viewer instead of a Detail View.

When you handle the `CustomProcessSelectedItem` event, set the `CustomProcessListViewSelectedItemEventArgs.Handled` parameter to `true` to prevent execution of the default Action. To access the currently selected object, use the `CustomProcessListViewSelectedItemEventArgs.InnerArgs.CurrentObject` parameter.

The example below demonstrates a [Controller](xref:112621) that handles the `CustomProcessSelectedItem` event to show a custom Detail View:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class ProcessContactListViewRowController : ViewController {
    public ProcessContactListViewRowController() {
        TargetViewId = "Contact_ListView";
    }
    protected override void OnActivated() {
        base.OnActivated();
        ListViewProcessCurrentObjectController listProcessController = Frame.GetController<ListViewProcessCurrentObjectController>();
        if(listProcessController != null)
            listProcessController.CustomProcessSelectedItem += ProcessContactListViewRowController_CustomProcessSelectedItem;        
    }
    void ProcessContactListViewRowController_CustomProcessSelectedItem(
        object sender, CustomProcessListViewSelectedItemEventArgs e) {
        Contact currentContact = (Contact)e.InnerArgs.CurrentObject;
        if (currentContact.Position != null && currentContact.Position.Title == "Manager") {
            IObjectSpace objectSpace = Application.CreateObjectSpace(currentContact.GetType());
            e.InnerArgs.ShowViewParameters.CreatedView = Application.CreateDetailView(objectSpace, "Contact_DetailView_Manager", true, objectSpace.GetObject(currentContact));
            e.Handled = true;
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        Frame.GetController<ListViewProcessCurrentObjectController>().CustomProcessSelectedItem -= ProcessContactListViewRowController_CustomProcessSelectedItem;
    }
}
```
***

> [!NOTE]
> * When a List View's `MasterDetailMode` is set to `ListAndDetailView`, handle the @DevExpress.ExpressApp.ListView.CreateCustomCurrentObjectDetailView event to specify or customize the Detail View created after the List View's current object is changed.

For more examples, refer to the following topic: [How to: Replace a List View's Default Action](xref:112820).

To disable double-click processing in a [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor), set the [GridListEditor.ProcessSelectedItemByDoubleClick](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.ProcessSelectedItemByDoubleClick) property to `false`.
