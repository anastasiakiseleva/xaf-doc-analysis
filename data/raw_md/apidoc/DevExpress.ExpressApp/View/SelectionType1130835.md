---
uid: DevExpress.ExpressApp.View.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by a View.
syntax:
  content: public virtual SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value representing the selection type supported by the current View.
seealso: []
---
The **SelectionType** property returns the [SelectionType.None](xref:DevExpress.ExpressApp.SelectionType.None) value, indicating that the selection is not supported. This property should be overridden in [](xref:DevExpress.ExpressApp.View) class descendants. The [](xref:DevExpress.ExpressApp.ListView) and [](xref:DevExpress.ExpressApp.DetailView) classes specify this property in different ways (see [ListView.SelectionType](xref:DevExpress.ExpressApp.ListView.SelectionType) and [DetailView.SelectionType](xref:DevExpress.ExpressApp.DetailView.SelectionType)).