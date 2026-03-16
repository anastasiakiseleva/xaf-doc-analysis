---
uid: DevExpress.ExpressApp.CompositeView.InsertItem(System.Int32,DevExpress.ExpressApp.Editors.ViewItem)
name: InsertItem(Int32, ViewItem)
type: Method
summary: Inserts a new [View Item](xref:112612) to a specified position within the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
syntax:
  content: public void InsertItem(int index, ViewItem item)
  parameters:
  - id: index
    type: System.Int32
    description: A zero-based integer specifying the new View Item's position within the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
  - id: item
    type: DevExpress.ExpressApp.Editors.ViewItem
    description: A [](xref:DevExpress.ExpressApp.Editors.ViewItem) descendant representing the View Item inserted into the current Detail View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
seealso: []
---
This method inserts a View Item into the current Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection at the specified position. All the following items are moved to the end of the collection. The `item` parameter specifies the View Item to be inserted. The `index` parameter specifies the position. If `index` is last in the collection, the View Item is appended to the end.

Inserting an item to the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection raises the [CompositeView.ItemsChanged](xref:DevExpress.ExpressApp.CompositeView.ItemsChanged) event.

Generally, you do not need to use this method. Instead, you can add View Items in the [Application Model](xref:112580). To do so, use the Application | Views | DetailView | Items node.