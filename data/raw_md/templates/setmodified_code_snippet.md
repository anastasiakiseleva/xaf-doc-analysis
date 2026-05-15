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

# [VB.NET](#tab/tabid-vb)

```vb
Imports System
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Editors
Imports MySolution.Module.BusinessObjects
'...
Namespace MySolution.Module.Controllers
    Public Class ClearEmployeeTasksController
        Inherits ViewController

        Private ClearTasksAction As SimpleAction
        Public Sub New()
            ClearTasksAction = New SimpleAction()
            AddHandler ClearTasksAction.Execute, AddressOf ClearTasksAction_Execute
        End Sub

        Private Sub ClearTasksAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
            Do While DirectCast(View.CurrentObject, Employee).Tasks.Count > 0
                DirectCast(View.CurrentObject, Employee).Tasks.Remove(DirectCast(View.CurrentObject, Employee).Tasks(0))
            Loop
            ObjectSpace.SetModified(View.CurrentObject)
        End Sub
    End Class
End Namespace
```

***