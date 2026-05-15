---
uid: DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)
name: GetObject(Object)
type: Method
summary: Retrieves an object that corresponds to an @DevExpress.ExpressApp.IObjectRecord wrapper or object from another Object Space.
syntax:
  content: object GetObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A business object wrapper or object from another Object Space that corresponds to the required persistent object.
  return:
    type: System.Object
    description: An object retrieved from the database via the current Object Space.
seealso: []
---
The example below demonstrates how to use the **GetObject** method.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;

// ...
public class ShowDetailViewController : ObjectViewController<ListView, Person> {
    public ShowDetailViewController() {
        PopupWindowShowAction showDetailViewAction = new PopupWindowShowAction(
            this, "ShowDetailView", PredefinedCategory.Edit);
        showDetailViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        showDetailViewAction.CustomizePopupWindowParams += ShowDetailViewAction_CustomizePopupWindowParams;
    }
    private void ShowDetailViewAction_CustomizePopupWindowParams(
        object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
        Object currentObject = objectSpace.GetObject(View.CurrentObject);
        if(currentObject != null) {
            e.View = Application.CreateDetailView(objectSpace, currentObject, true);
        }
        else {
            objectSpace.Dispose();
        }
    }
}

```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.BaseImpl

Public Class ShowDetailViewController
    Inherits ObjectViewController(Of ListView, Person)
    Public Sub New()
        Dim showDetailViewAction As New PopupWindowShowAction(Me, "ShowDetailView", PredefinedCategory.Edit)
        showDetailViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
        AddHandler showDetailViewAction.CustomizePopupWindowParams, _
            AddressOf ShowDetailViewAction_CustomizePopupWindowParams
    End Sub
    Private Sub ShowDetailViewAction_CustomizePopupWindowParams(ByVal sender As Object, _
        ByVal e As CustomizePopupWindowParamsEventArgs)
        Dim objectSpace As IObjectSpace = Application.CreateObjectSpace(GetType(Person))
        Dim currentObject As Object = objectSpace.GetObject(View.CurrentObject)
        If currentObject IsNot Nothing Then
            e.View = Application.CreateDetailView(objectSpace, currentObject, True)
        Else
            objectSpace.Dispose()
        End If
    End Sub
End Class

```

***
