---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType
name: ItemType
type: Property
summary: Specifies the type of a Single Choice Action's items from the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection.
syntax:
  content: |-
    [DefaultValue(SingleChoiceActionItemType.ItemIsMode)]
    public SingleChoiceActionItemType ItemType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceActionItemType
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionItemType) enumeration value identifying a Single Choice Action's items kind.
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemTypeChanged
---
Use this property to specify whether the Single Choice Action's items represent a mode or an operation. Item type is considered when the Single Choice Action is displayed. When items represent modes, the Action's control indicates the current selection. For items that represent operations, this functionality is not provided.

The example below demonstrates how to add a @DevExpress.ExpressApp.Actions.SingleChoiceAction and set it to perform operations.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;

// ...
public class SingleChoiceActionController : ObjectViewController<ListView, Person> {
    public SingleChoiceActionController() {
        SingleChoiceAction contactAction = new SingleChoiceAction(this, "ContactAction", PredefinedCategory.Edit);
        contactAction.ItemType = SingleChoiceActionItemType.ItemIsOperation;
        ChoiceActionItem openContact = new ChoiceActionItem("openContact", "Open Contact", null);
        ChoiceActionItem deleteContact = new ChoiceActionItem("deleteContact", "Delete Contact", null);
        contactAction.Items.Add(openContact);
        contactAction.Items.Add(deleteContact);
        contactAction.Execute += ContactAction_Execute;
    }
    private void ContactAction_Execute(object sender, SingleChoiceActionExecuteEventArgs e) {
        if(View.CurrentObject != null) {
            if(e.SelectedChoiceActionItem.Id == "openContact") {
                IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
                object currentObject = objectSpace.GetObject(View.CurrentObject);
                if(currentObject != null) {
                    e.ShowViewParameters.CreatedView = Application.CreateDetailView(objectSpace, currentObject);
                }
                else {
                    objectSpace.Dispose();
                }
            }
            else if(e.SelectedChoiceActionItem.Id == "deleteContact") {
                View.ObjectSpace.Delete(View.CurrentObject);
                View.ObjectSpace.CommitChanges();
                View.Refresh(true);
            }
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

Public Class SingleChoiceActionController
    Inherits ObjectViewController(Of ListView, Person)

    Public Sub New()
        Dim contactAction As New SingleChoiceAction(Me, "ContactAction", PredefinedCategory.Edit)
        contactAction.ItemType = SingleChoiceActionItemType.ItemIsOperation
        Dim openContact As New ChoiceActionItem("openContact", "Open Contact", Nothing)
        Dim deleteContact As New ChoiceActionItem("deleteContact", "Delete Contact", Nothing)
        contactAction.Items.Add(openContact)
        contactAction.Items.Add(deleteContact)
        AddHandler contactAction.Execute, AddressOf ContactAction_Execute
    End Sub
    Private Sub ContactAction_Execute(ByVal sender As Object, ByVal e As SingleChoiceActionExecuteEventArgs)
        If View.CurrentObject IsNot Nothing Then
            If e.SelectedChoiceActionItem.Id = "openContact" Then
                Dim objectSpace As IObjectSpace = Application.CreateObjectSpace(GetType(Person))
                Dim currentObject As Object = objectSpace.GetObject(View.CurrentObject)
                If currentObject IsNot Nothing Then
                    e.ShowViewParameters.CreatedView = Application.CreateDetailView(objectSpace, currentObject)
                Else
                    objectSpace.Dispose()
                End If
            ElseIf e.SelectedChoiceActionItem.Id = "deleteContact" Then
                View.ObjectSpace.Delete(View.CurrentObject)
                View.ObjectSpace.CommitChanges()
                View.Refresh(True)
            End If
        End If
    End Sub
End Class
```

***

Items represent modes

![SingleChoiceAction_ItemType_Mode](~/images/singlechoiceaction_itemtype_mode115414.png)

Items represent operations

![SingleChoiceAction_ItemType_Operation](~/images/singlechoiceaction_itemtype_operation115415.png)
> [!NOTE]
> The defined behavior is provided by built-in [Action Containers](xref:112610). You can customize this by implementing a custom Action Container.