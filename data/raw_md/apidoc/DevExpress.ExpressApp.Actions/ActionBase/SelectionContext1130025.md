---
uid: DevExpress.ExpressApp.Actions.ActionBase.SelectionContext
name: SelectionContext
type: Property
summary: Specifies a context of an [Action](xref:112622)'s execution.
syntax:
  content: |-
    [Browsable(false)]
    public ISelectionContext SelectionContext { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ISelectionContext
    description: An instance of the class that implements the **ISelectionContext** interface.
seealso: []
---
This property is used as a parameter of the **Execute** event handlers in the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class descendants ([](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) and so on). Use the property's value to determine whether the current [View](xref:112611) is root, or to access the current View's current object or the collection of selected objects. By default, for Actions contained in [View Controllers](xref:112621), this property is set to the [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property value. For Actions from Window Controllers, this property is set to **null**.

Currently, members of the **ISelectionContext** interface are implemented in the [](xref:DevExpress.ExpressApp.View) class only. If you need to set a new value to this property, use the [](xref:DevExpress.ExpressApp.View) class or a custom class that implements the **ISelectionContext** interface.