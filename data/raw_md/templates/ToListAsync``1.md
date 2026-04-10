The following code snippet uses this method in a WinForms-specific [View Controller](xref:112621#view-controllers) to add contacts from the Development Department to the task's `Contacts` collection.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win;
using DevExpress.ExpressApp.Xpo;
using DevExpress.XtraSplashScreen;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
// ...
public class AsyncTaskContactsController : ObjectViewController<DetailView, DemoTask> {
    public AsyncTaskContactsController() : base() {
        base.OnActivated();
        SimpleAction assignToDepartmentAction = new SimpleAction(this, "Assign to the Dev.Departmant", "Edit");
        assignToDepartmentAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        assignToDepartmentAction.Execute += assignToDepartmentAction_Execute;
    }
    async private void assignToDepartmentAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        IOverlaySplashScreenHandle handle = null;
        Control control = Frame.Template as Control;
        WinApplication application = Application as WinApplication;
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        var contacts = from c in ObjectSpace.GetObjectsQuery<Contact>()
                        where c.Department.Title == "Development Department"
                        select c;
        IList<Contact> contactsList = null;
        try {
            if (control != null && control.IsHandleCreated) {
                handle = application.StartOverlayForm(control);
            }
            contactsList = await ((XPObjectSpace)ObjectSpace).ToListAsync<Contact>(contacts, cancellationTokenSource.Token);
            ViewCurrentObject.Contacts.AddRange(contactsList);
        }
        finally {
            if (handle != null) {
                application.StopOverlayForm(handle);
            }
        }
    }
}
```
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]