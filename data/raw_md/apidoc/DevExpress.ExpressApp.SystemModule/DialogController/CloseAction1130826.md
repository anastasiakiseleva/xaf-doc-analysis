---
uid: DevExpress.ExpressApp.SystemModule.DialogController.CloseAction
name: CloseAction
type: Property
summary: Provides access to the current DialogController's **Close** Action.
syntax:
  content: public SimpleAction CloseAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the DialogController's **Close** Action.
seealso: []
---
The Dialog Controller contains the **Close** Action. This Action is not displayed in a Window where the DialogController is activated, because the Template that represents pop-up Windows does not contain the [Action Container](xref:112610) associated with the Action. However, the **Close** Action is executed when pressing an object in the pop-up Window's List View. The **ExecuteCompleted** event of this Action is handled by the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction)'s **ExecuteCompleted** event handler, which closes the window. To perform additional operations before the **ExecuteCompleted** event hander is called, handle the **Close**  Action's **Execute** event.