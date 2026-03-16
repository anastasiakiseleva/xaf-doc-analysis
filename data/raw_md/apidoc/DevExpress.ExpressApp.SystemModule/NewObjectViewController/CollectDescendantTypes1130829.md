---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes
name: CollectDescendantTypes
type: Event
summary: Occurs when the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s `Items` List is generated or updated.
syntax:
  content: public event EventHandler<CollectTypesEventArgs> CollectDescendantTypes
seealso: []
---
In Windows Forms applications, the **New** Action's `Items` list is generated in two steps. First, the current View's object type and its descendants are added; second, the types listed in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node are added.

Handle the `CollectDescendantTypes` event to change types displayed in the New action. To access the list of these types, use the handler's `CollectTypesEventArgs.Types` parameter. To modify the list of additional creatable types in Windows Forms, handle the [NewObjectViewController.CollectCreatableItemTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes) event.

If you need to inherit from the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) and override the caller of the `CollectDescendantTypes` event, inherit from the `WinNewObjectViewController` and/or **BlazorNewObjectViewController** class and override the `UpdateActionState` method. In this method, you can get the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s `Items` collection via the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) property, and customize it as required.

To see examples of how to handle the `CollectDescendantTypes` event, refer to the [How to: Customize the New Action's Items List](xref:112915) topic.