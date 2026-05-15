---
uid: DevExpress.ExpressApp.View.SelectionChanged
name: SelectionChanged
type: Event
summary: Occurs after changing a View's selected objects.
syntax:
  content: public event EventHandler SelectionChanged
seealso:
- linkType: HRef
  linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
  altText: DetailView.SelectedObjects
- linkType: HRef
  linkId: DevExpress.ExpressApp.ListView.SelectedObjects
  altText: ListView.SelectedObjects
- linkType: HRef
  linkId: DevExpress.ExpressApp.DetailView.CurrentObject
  altText: DetailView.CurrentObject
- linkType: HRef
  linkId: DevExpress.ExpressApp.ListView.CurrentObject
  altText: ListView.CurrentObject
---
This event is raised in methods of the [](xref:DevExpress.ExpressApp.View) class descendants:

* [](xref:DevExpress.ExpressApp.DetailView)
    
    The **SelectionChanged** event occurs after changing the current object as a result of setting a value to the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) method.
* [](xref:DevExpress.ExpressApp.ListView)
    
    The **SelectionChanged** event is raised when the selected objects are changed in the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor).

  
The example below demonstrates how to change a @DevExpress.ExpressApp.Actions.SimpleAction's caption when the selected object changes.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class ActionCaptionController : ViewController {
    private SimpleAction objectAction;
    private void UpdateActionCaption() {
        objectAction.Caption = CalculateActionCaption();
    }
    private string CalculateActionCaption() {
        Contact currentObject = (Contact)View.CurrentObject;
        if(currentObject != null) {
            return currentObject.FullName;
        }
        return "Object Action";
    }
    private void View_SelectionChanged(object sender, EventArgs e) {
        UpdateActionCaption();
    }
    protected override void OnActivated() {
        base.OnActivated();
        UpdateActionCaption();
        View.SelectionChanged += View_SelectionChanged;
    }
    protected override void OnDeactivated() {
        View.SelectionChanged -= View_SelectionChanged;
        base.OnDeactivated();
    }
    public ActionCaptionController() {
        TargetObjectType = typeof(Contact);
        objectAction = new SimpleAction(this, "ObjectAction", PredefinedCategory.Edit);
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports MainDemo.Module.BusinessObjects

Public Class ActionCaptionController
    Inherits ViewController
    Private objectAction As SimpleAction
    Private Sub UpdateActionCaption()
        objectAction.Caption = CalculateActionCaption()
    End Sub
    Private Function CalculateActionCaption() As String
        Dim currentObject As Contact = CType(View.CurrentObject, Contact)
        If currentObject IsNot Nothing Then
            Return currentObject.FullName
        End If
        Return "Object Action"
    End Function
    Private Sub View_SelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
        UpdateActionCaption()
    End Sub
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        UpdateActionCaption()
        AddHandler View.SelectionChanged, AddressOf View_SelectionChanged
    End Sub
    Protected Overrides Sub OnDeactivated()
        RemoveHandler View.SelectionChanged, AddressOf View_SelectionChanged
        MyBase.OnDeactivated()
    End Sub
    Public Sub New()
        TargetObjectType = GetType(Contact)
        objectAction = New SimpleAction(Me, "ObjectAction", PredefinedCategory.Edit)
    End Sub
End Class
```
***

> [!NOTE]
> To run this code, add the _DevExpress.ExpressApp.XtraGrid.v<:xx.x:>.dll_ assembly to References.

