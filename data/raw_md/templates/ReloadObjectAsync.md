The following code uses this method in a [View Controller](xref:112621#view-controllers) to refresh a List View after a user changes an object on a Detail View and commits these changes. In this scenario, the List View should be [read-only](xref:DevExpress.ExpressApp.View.AllowEdit).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.ExpressApp.Xpo;
using System.Threading;
// ...
public class AsyncUpdateListViewController : ObjectViewController<ListView, DemoTask> {
    public AsyncUpdateListViewController() : base() {
        SimpleAction updateListViewAction = new SimpleAction(this, "Open assigned contact", "Edit");
        updateListViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        updateListViewAction.Execute += updateListViewAction_Execute;
    }
    private void updateListViewAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        object assignedContact = ViewCurrentObject.AssignedTo;
        IObjectSpace contactObjectSpace = Application.CreateObjectSpace(assignedContact.GetType());
        View contactView = Application.CreateDetailView(contactObjectSpace, contactObjectSpace.GetObject(assignedContact), true);
        e.ShowViewParameters.CreatedView = contactView;
        contactObjectSpace.Committed += async (s, args) => {
            CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
            await ((XPObjectSpace)ObjectSpace).ReloadObjectAsync(assignedContact, cancellationTokenSource.Token);
            if (View.Editor is GridListEditor) {
                GridListEditor gridListEditor = (GridListEditor)View.Editor;
                gridListEditor.GridView.LayoutChanged();
            }
        };
    }
}
```
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]