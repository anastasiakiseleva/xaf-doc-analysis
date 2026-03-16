---
uid: DevExpress.ExpressApp.XafApplication.CreateObjectSpace``1
name: CreateObjectSpace<T>()
type: Method
summary: Creates an [Object Space](xref:113707) of the specified type.
syntax:
  content: public IObjectSpace CreateObjectSpace<T>()
  typeParameters:
  - id: T
    description: Object type.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object.
seealso: []
---
For more information about creating an Object Space of the specified type, refer to the following topic: @DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type).

The following code demonstrates how to implement a @DevExpress.ExpressApp.Actions.PopupWindowShowAction to create a new `Note` object:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Blazor.Server.Controllers;
public class ShowNotesController : WindowController {
    public ShowNotesController() {
        PopupWindowShowAction showNotesAction = new PopupWindowShowAction(this, "ShowNotes", PredefinedCategory.Edit);
        showNotesAction.CustomizePopupWindowParams += ShowNotesAction_CustomizePopupWindowParams;
    }
    private void ShowNotesAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace objectSpace = Application.CreateObjectSpace<Note>();
        var note = objectSpace.CreateObject<Note>();
        e.View = Application.CreateDetailView(objectSpace, note);
    }
}
```