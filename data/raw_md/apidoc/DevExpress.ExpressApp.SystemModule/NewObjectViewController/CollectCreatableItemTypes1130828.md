---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes
name: CollectCreatableItemTypes
type: Event
summary: Occurs when the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s **Items** List is generated or updated.
syntax:
  content: public event EventHandler<CollectTypesEventArgs> CollectCreatableItemTypes
seealso: []
---
In Windows Forms applications, the **New** Action's `Items` list is generated in two steps. First, the current View's object type and its descendants are added; second, the types listed in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node are added. To modify the list of the types added first, handle the [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) event. To modify the list of the types added second, handle the `CollectCreatableItemTypes` event. To access this list, use the handler's `CollectTypesEventArgs.Types` parameter.


If you need to inherit from the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) and override the caller of the `CollectCreatableItemTypes`  event, inherit from the `WinNewObjectViewController` class and override the `UpdateActionState` method. In this method, you can get the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s `Items` collection via the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) property, and customize it as required.

To see examples of how to handle the `CollectCreatableItemTypes` event, refer to the following topic: [How to: Customize the New Action's Items List](xref:112915).