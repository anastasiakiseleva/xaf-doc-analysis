---
uid: DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController
name: DeleteObjectsViewController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Delete** [Action](xref:112622).
syntax:
  content: 'public class DeleteObjectsViewController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController._members
  altText: DeleteObjectsViewController Members
---
The `DeleteObjectsViewController` contains the **Delete** Action.

In a Windows Forms application:

![DeleteAction](~/images/deleteaction116254.png)

For details on the **Delete** Action, refer to the following topic: [DeleteObjectsViewController.DeleteAction](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction).

To customize the default behavior of the **Delete** Action, you can inherit from this Controller or subscribe to its events. In addition, you can access the Action to modify its behavior.

If you need to inherit from the `DeleteObjectsViewController`, the following protected virtual methods are available for overriding:

{|
|-

! Method
! When is it called?
! Description
|-

| Delete
| Invoked as a result of executing the **Delete** Action.
| The **Delete** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Deletes the object(s) selected in the current View. In case of a List View, this method refreshes the collection source and editor. In case of a Detail View, the method closes it.

Raises the [DeleteObjectsViewController.Deleting](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.Deleting) event.
|-

| UpdateActionState
| Invoked as a result of changes made to the current View's object(s):
| Checks whether the **Delete** Action's active or enabled state should be changed after the environment has been changed.
|}

Public members are described individually in the documentation.

This Controller is activated for all [Views](xref:112611). To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

