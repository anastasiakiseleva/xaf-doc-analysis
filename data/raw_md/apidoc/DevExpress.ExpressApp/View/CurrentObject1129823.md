---
uid: DevExpress.ExpressApp.View.CurrentObject
name: CurrentObject
type: Property
summary: Specifies a [](xref:DevExpress.ExpressApp.View)'s current object.
syntax:
  content: public virtual object CurrentObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An object representing the current View's current object.
seealso:
- linkType: HRef
  linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
  altText: DetailView.SelectedObjects
- linkType: HRef
  linkId: DevExpress.ExpressApp.ListView.SelectedObjects
  altText: ListView.SelectedObjects
---
The example below demonstrates how to set a **Contact**'s **FirstName** value to the **NickName** property via a @DevExpress.ExpressApp.Actions.SimpleAction.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class SetNickNameController : ViewController {
    public SetNickNameController() {
        SimpleAction setNickNameAction = new SimpleAction(this, "SetNickName", PredefinedCategory.Edit);
        setNickNameAction.Execute += SetNickNameAction_Execute;
    }
    private void SetNickNameAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Contact currentObject = View.CurrentObject as Contact;
        if(currentObject != null) {
            currentObject.NickName = currentObject.FirstName;
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)
```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports MainDemo.Module.BusinessObjects

Public Class SetNickNameController
    Inherits ViewController
    Public Sub New()
        Dim setNickNameAction As New SimpleAction(Me, "SetNickName", PredefinedCategory.Edit)
        AddHandler setNickNameAction.Execute, AddressOf SetNickNameAction_Execute
    End Sub
    Private Sub SetNickNameAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim currentObject As Contact = TryCast(View.CurrentObject, Contact)
        If currentObject IsNot Nothing Then
            currentObject.NickName = currentObject.FirstName
        End If
    End Sub
End Class
```
***

This property returns **null** and is intended to be overridden in [](xref:DevExpress.ExpressApp.View) descendants. See [ListView.CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject) and [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject).

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.