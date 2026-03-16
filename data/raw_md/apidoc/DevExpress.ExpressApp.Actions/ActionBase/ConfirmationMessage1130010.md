---
uid: DevExpress.ExpressApp.Actions.ActionBase.ConfirmationMessage
name: ConfirmationMessage
type: Property
summary: Specifies the confirmation message displayed when an end-user executes an [Action](xref:112622).
syntax:
  content: |-
    [DefaultValue("")]
    public string ConfirmationMessage { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string containing the current Action's confirmation message.
seealso:
- linkId: "112580"
---
When executing an Action, a pop-up window is invoked to display a confirmation message if it is specified by the `ConfirmationMessage` property. To change an Action's confirmation message at run time, use the Application Model's [IModelAction.ConfirmationMessage](xref:DevExpress.ExpressApp.Model.IModelAction.ConfirmationMessage) property of the corresponding [!include[Node_Action](~/templates/node_action111373.md)] node. You can do this either via the [Model Editor](xref:112582) or by [accessing the Application Model in code](xref:112810).

You can include the '{0}' format item in the confirmation message. This item will be replaced at run time with either the currently selected object's caption (if the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property is set to `RequireSingleObject`) or the selected objects count (if the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property is set to `RequireMultipleObjects`). To learn more about formatting confirmation messages, refer to the [](xref:402146) article.


> [!TIP]
> To use data from objects that are currently selected by user, follow the approach described in the [How to: Access Objects Selected in the Current View](xref:113324) example.

The example below adds a confirmation message to a @DevExpress.ExpressApp.Actions.SimpleAction, and if the user confirms, assigns a `Contact`'s `FirstName` value to the `NickName` property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class SetNickNameController : ObjectViewController<DetailView, Contact> {
    public SetNickNameController() {
        SimpleAction setNickNameAction = new SimpleAction(this, "SetNickName", PredefinedCategory.Edit);
        setNickNameAction.ConfirmationMessage = "Do you want to continue?";
        setNickNameAction.Execute += SetNickNameAction_Execute;
    }
    private void SetNickNameAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Contact currentObject = ViewCurrentObject;
        if(currentObject != null) {
            currentObject.NickName = currentObject.FirstName;
        }
    }
}

```
***