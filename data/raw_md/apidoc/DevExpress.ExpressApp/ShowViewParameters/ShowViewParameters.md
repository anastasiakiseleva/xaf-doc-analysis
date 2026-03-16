---
uid: DevExpress.ExpressApp.ShowViewParameters
name: ShowViewParameters
type: Class
summary: A set of parameters used to display a new [View](xref:112611).
syntax:
  content: public class ShowViewParameters
seealso:
- linkId: DevExpress.ExpressApp.ShowViewParameters._members
  altText: ShowViewParameters Members
- linkId: "112805"
- linkId: "112803"
- linkId: "112804"
- linkId: "403731"
---
Use the `ShowViewParameters` object to specify view settings for the View.

The following example demonstrates how to use a `ShowViewParameters` object in an Action's `Execute` event handler. The code customizes the **Accept** Action:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.SystemModule;
using MainDemo.Module.BusinessObjects;

namespace YourApplicationName.Blazor.Server.Controllers {
    public class ShowViewController : ViewController {
        SimpleAction showViewAction;

        public ShowViewController() {
            showViewAction = new SimpleAction(this, "ShowEmployeesList", 
                DevExpress.Persistent.Base.PredefinedCategory.Edit);
            showViewAction.Execute += ShowViewAction_Execute;
        }

        private void ShowViewAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Employee));
            string listViewId = Application.FindListViewId(typeof(Employee));
            e.ShowViewParameters.CreatedView = Application.CreateListView(
               listViewId, 
               Application.CreateCollectionSource(objectSpace, typeof(Employee), listViewId),
               true);
            e.ShowViewParameters.TargetWindow = TargetWindow.NewModalWindow;
            var dlgCnt = Application.CreateController<DialogController>();
            dlgCnt.Accepting += DlgCnt_Accepting;
            e.ShowViewParameters.Controllers.Add(dlgCnt);
        }

        private void DlgCnt_Accepting(object sender, DialogControllerAcceptingEventArgs e) {
            // Add your custom code here.
        }
    }
}
```

***

> [!NOTE]
> XAF creates a [](xref:DevExpress.ExpressApp.SystemModule.DialogController) for Pop-up Windows by default.

[XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) manages Window and View visibility. This strategy may use properties of a @DevExpress.ExpressApp.ShowViewParameters object.