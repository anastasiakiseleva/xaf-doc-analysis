---
uid: DevExpress.ExpressApp.Model.IModelClass.IsCreatableItem
name: IsCreatableItem
type: Property
summary: Indicates whether the current class can represent an item in the **New** Action, when objects of another type are displayed in the List View.
syntax:
  content: bool IsCreatableItem { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if the current class can represent the **New** Action's item, when objects of another type are displayed in the List View; otherwise, **false**."
seealso: []
---
By default, this property is set to the **IsCreatableItem** property value of the current class' base class.

This property value is set to **true** if the [DefaultClassOptions or CreatableItem(true)](xref:112701) attribute is applied to the class declaration. You can change the default behavior by adding or removing the corresponding item from the [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node.