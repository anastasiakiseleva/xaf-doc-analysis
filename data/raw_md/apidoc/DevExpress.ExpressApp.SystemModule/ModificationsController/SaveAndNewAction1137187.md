---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndNewAction
name: SaveAndNewAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController)'s **Save and New** Action.
syntax:
  content: public SingleChoiceAction SaveAndNewAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object that is the **Save and New** Action.
seealso: []
---
Use the **Save and New** Action to commit changes made to the current Detail View's object, create a new object, and display the object in a new Detail View form. The [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection contains elements from the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s `Items` collection. The default selected item corresponds to the current View's object type.

Use the `SaveAndNew` protected method of the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) to handle the **Save and New** Action's `Execute` event.

The **Save and New** Action is active when the current View is [root](xref:DevExpress.ExpressApp.View.IsRoot). In addition, the active state depends on the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s active state. When the **New** Action is disabled, the **Save and New** Action is disabled as well.

Information on the **Save and New** Action is available in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelActionDesign) node. To access it, use the [Model Editor](xref:112582).
