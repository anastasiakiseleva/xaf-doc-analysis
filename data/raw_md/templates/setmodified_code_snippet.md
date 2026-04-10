The following code snippet clears the `Tasks` collection of the `Contact` Detail View and marks the `Contact` object as modified:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Editors;
using MySolution.Module.BusinessObjects;
//...
namespace MySolution.Module.Controllers {
    public class ClearEmployeeTasksController : ViewController {
		private SimpleAction ClearTasksAction;
		public ClearEmployeeTasksController() {
			ClearTasksAction = new SimpleAction();
			ClearTasksAction.Execute += new SimpleActionExecuteEventHandler(ClearTasksAction_Execute);
		}

		private void ClearTasksAction_Execute(Object sender, SimpleActionExecuteEventArgs e) {
			while(((Employee)View.CurrentObject).Tasks.Count > 0) {
				((Employee)View.CurrentObject).Tasks.Remove(((Employee)View.CurrentObject).Tasks[0]);
			}
			ObjectSpace.SetModified(View.CurrentObject);
		}
	}
}

```
***