---
uid: DevExpress.ExpressApp.View.SelectedObjects
name: SelectedObjects
type: Property
summary: Specifies a [](xref:DevExpress.ExpressApp.View)'s selected objects.
syntax:
  content: public virtual IList SelectedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An object list that contains the current View's selected objects.
seealso:
- linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
- linkId: DevExpress.ExpressApp.ListView.SelectedObjects
- linkId: DevExpress.ExpressApp.DetailView.CurrentObject
- linkId: DevExpress.ExpressApp.ListView.CurrentObject
---
This property returns **null** and is intended to be overridden in [](xref:DevExpress.ExpressApp.View) descendants. See [ListView.SelectedObjects](xref:DevExpress.ExpressApp.ListView.SelectedObjects) and [DetailView.SelectedObjects](xref:DevExpress.ExpressApp.DetailView.SelectedObjects).

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.