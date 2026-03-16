---
uid: DevExpress.ExpressApp.CompositeView.RemoveItem(System.String)
name: RemoveItem(String)
type: Method
summary: Removes a particular [View Item](xref:112612) from a Composite View's [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
syntax:
  content: public void RemoveItem(string id)
  parameters:
  - id: id
    type: System.String
    description: A string value that is the ID of the View Item to be removed.
seealso:
- linkId: DevExpress.ExpressApp.CompositeView.AddItem*
- linkId: DevExpress.ExpressApp.CompositeView.InsertItem*
---
If the specified [View Item](xref:112612) cannot be found, this method does nothing.

You can handle the [CompositeView.ItemsChanged](xref:DevExpress.ExpressApp.CompositeView.ItemsChanged) event to perform specific actions after removing an item from the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.

You can also remove a View Item in the [Application Model](xref:112580). To do so, use the Application | Views | DetailView | Items node.