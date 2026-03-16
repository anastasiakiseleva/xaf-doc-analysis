---
uid: DevExpress.ExpressApp.CompositeView.InsertItem(System.Int32,DevExpress.ExpressApp.Model.IModelViewItem)
name: InsertItem(Int32, IModelViewItem)
type: Method
summary: Creates a [View Item](xref:112612) using specified information, and inserts that View Item into Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection at the required position.
syntax:
  content: public ViewItem InsertItem(int index, IModelViewItem info)
  parameters:
  - id: index
    type: System.Int32
    description: A zero-based integer specifying the new View Item's position within the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
  - id: info
    type: DevExpress.ExpressApp.Model.IModelViewItem
    description: An [](xref:DevExpress.ExpressApp.Model.IModelViewItem) object representing the [Application Model](xref:112580) node with information on the new View Item.
  return:
    type: DevExpress.ExpressApp.Editors.ViewItem
    description: A [](xref:DevExpress.ExpressApp.Editors.ViewItem) descendant representing the View Item inserted.
seealso:
- linkId: DevExpress.ExpressApp.CompositeView.AddItem*
- linkId: DevExpress.ExpressApp.CompositeView.RemoveItem(System.String)
---
The `InsertItem` method creates a [View Item](xref:112612) using information from the [Application Model](xref:112580) node. This node is passed as the `info` parameter. The created item is inserted into the current Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection at the specified position by moving all subsequent items to the end of the collection. The `index` parameter specifies this position. If `index` is the last in the collection, the View Item is appended to the end.

Adding an item to the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection raises the [CompositeView.ItemsChanged](xref:DevExpress.ExpressApp.CompositeView.ItemsChanged) event.

Generally, you do not need to use this method. Instead, you can add View Items in the [Application Model](xref:112580). To do so, use the Application | Views | DetailView | Items node.