---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndCloseAction
name: SaveAndCloseAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController)'s **Save And Close** Action.
syntax:
  content: public SimpleAction SaveAndCloseAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **Save and Close** Action.
seealso:
- linkId: "112818"
- linkId: DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAction
---
The **Save And Close** Action commits the changes made to the object selected in the current View and closes the View.

The **Save And Close** Action is active when the current View is root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)). In Windows Forms applications, its active state depends on the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property value.

The **Save And Close** Action is disabled when the current user does not have permission to change the current object.

Information on the **Save And Close** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).
