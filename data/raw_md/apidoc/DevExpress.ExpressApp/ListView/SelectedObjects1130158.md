---
uid: DevExpress.ExpressApp.ListView.SelectedObjects
name: SelectedObjects
type: Property
summary: Provides access to a collection of objects currently selected in a List View's [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor).
syntax:
  content: public override IList SelectedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An **IList** collection on selected objects.
seealso:
- linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
---
If the current List View's [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) has not been instantiated yet, an empty collection is returned.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.