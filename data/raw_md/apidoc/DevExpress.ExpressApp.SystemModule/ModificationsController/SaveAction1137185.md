---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAction
name: SaveAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController)'s **Save** Action.
syntax:
  content: public SimpleAction SaveAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **Save** Action.
seealso: []
---
The **Save** Action commits the changes made to the object selected in the current View (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)).

The **Save** Action is active when the current View is root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)). In Windows Forms applications, its active state depends on the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property value.

The **Save** Action can be disabled if the current user does not have permission to change the current object.

Information on the **Save** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).
