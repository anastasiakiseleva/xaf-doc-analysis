The following code snippet uses this method in a [View Controller](xref:112621#view-controllers) to find and show a `Contact` the selected `DemoTask` is assigned to. If this `DemoTask` is not assigned to any `Contact`, XAF displays a Detail View for a new `Contact` object.


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
using System;
using System.Threading;
// ...
public class AsyncAssignedToInfoController : ObjectViewController<ListView, DemoTask> {
    View contactView = null;
    public AsyncAssignedToInfoController() : base() {
        SimpleAction showAssignedToInfoAction = new SimpleAction(this, "Assigned contact's info", "Edit");
        showAssignedToInfoAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        showAssignedToInfoAction.Execute += showAssignedToInfoAction_Execute;
    }
    async private void showAssignedToInfoAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        XPObjectSpace contactObjectSpace = (XPObjectSpace)Application.CreateObjectSpace(typeof(Contact));
        contactView = Application.CreateDetailView(contactObjectSpace, "Contact_DetailView", true);
        e.ShowViewParameters.CreatedView = contactView;
        Contact assignedTo = (Contact)ViewCurrentObject.AssignedTo;
            if (assignedTo != null) {
                object obj = await contactObjectSpace.FindObjectAsync<Contact>(
                    CriteriaOperator.Parse(string.Format("[Oid] = '{0}'", assignedTo.Oid)), 
                    cancellationTokenSource.Token);
                contactView.CurrentObject = obj ?? contactObjectSpace.CreateObject(typeof(Contact));
            }
            else {
                contactView.CurrentObject = contactObjectSpace.CreateObject(typeof(Contact));
            }
        if (contactObjectSpace.IsNewObject(contactView.CurrentObject)) {
            contactObjectSpace.Committed += contactObjectSpace_Committed;
        }
    }
    private void contactObjectSpace_Committed(object sender, EventArgs e) {
        ViewCurrentObject.AssignedTo = ObjectSpace.GetObject(contactView.CurrentObject) as Contact;
    }
}
```
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]