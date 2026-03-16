---
uid: DevExpress.ExpressApp.Editors.ViewItem.CurrentObject
name: CurrentObject
type: Property
summary: Specifies the object for which the current View Item's [View](xref:112611) is created.
syntax:
  content: public object CurrentObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An object represented by the View where the current View Item is contained.
seealso: []
---
Use this property to access the object represented by the current View Item's View.

When this property value is changed, the **OnCurrentObjectChanging** and **OnCurrentObjectChanged** methods are called. If you implement the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class' descendant, override these methods and raise the **CurrentObjectChanging** and **CurrentObjectChanged** events, if required.