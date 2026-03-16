---
uid: DevExpress.ExpressApp.DetailView.SelectedObjects
name: SelectedObjects
type: Property
summary: Returns a Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject).
syntax:
  content: public override IList SelectedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An array that contains a single object representing the current Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject).
seealso: []
---
Generally, there is no reason to use this property, as in the **DetailView** class, this property is overridden to return the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) wrapped into a list. So, in most cases you should use the **DetailView.CurrentObject** property instead.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.