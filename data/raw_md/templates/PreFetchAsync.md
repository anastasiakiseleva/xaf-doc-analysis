The following code uses this method in a WinForms-specific [View Controller](xref:112621#view-controllers).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
using MainDemo.Module.BusinessObjects;
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
        Contact obj = null;
        if (ViewCurrentObject.AssignedTo != null) {
            obj = (Contact)await contactObjectSpace.GetObjectAsync(ViewCurrentObject.AssignedTo);
            Contact[] contacts = new Contact[] { obj };
            await contactObjectSpace.PreFetchAsync(contacts, new string[] { "Tasks" });
        }
        if (obj == null) {
            obj = contactObjectSpace.CreateObject<Contact>();
            contactObjectSpace.Committed += contactObjectSpace_Committed;
        }
        contactView.CurrentObject = obj;
    }
    private void contactObjectSpace_Committed(object sender, EventArgs e) {
        ViewCurrentObject.AssignedTo = ObjectSpace.GetObject(contactView.CurrentObject) as Contact;
    }
}
```
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]