---
uid: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController
name: ListViewProcessCurrentObjectController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **ListViewShowObject** [Action](xref:112622).
syntax:
  content: 'public class ListViewProcessCurrentObjectController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController._members
  altText: ListViewProcessCurrentObjectController Members
---
`ListViewProcessCurrentObjectController` executes its **ListViewShowObject** Action when an end-user clicks an object in the current List View. This Action invokes a Detail View that displays the clicked object.

The `ListViewProcessCurrentObjectController` executes its **ListViewShowObject** Action when XAF calls the `OnProcessSelectedItem` method of the current List View's List Editor (see [](xref:DevExpress.ExpressApp.Editors.ListEditor)).

The [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor), Windows Forms **SchedulerListEditor**, and [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) call this method when the end-user double-clicks an object or presses <kbd>ENTER</kbd>. When you implement a [custom List Editor](xref:112659), you can call `OnProcessSelectedItem` where you need.

To execute a custom Action instead of the **ListViewShowObject** Action in a certain List View, handle the Controller's [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event. For details, refer to the following topic: [How to: Replace a List View's Default Action](xref:112820).

To access the **ListViewShowObject** Action, use the [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) property.

XAF activates `ListViewProcessCurrentObjectController` for [List Views](xref:112611) only. To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information on the `ListViewProcessCurrentObjectController` and its **ListViewShowObject** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).