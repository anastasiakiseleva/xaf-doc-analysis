---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.GetOrderedObjects
name: GetOrderedObjects()
type: Method
summary: Returns an ordered list of objects that represent the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)'s nodes.
syntax:
  content: public IList GetOrderedObjects()
  return:
    type: System.Collections.IList
    description: An ordered list of objects that represent the **TreeListEditor**'s nodes.
seealso: []
---
This method is not intended to be called from your code. It is implemented as a part of the **IControlOrderProvider** interface. The [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor) implements this interface to support the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s [Actions](xref:112622) for the [Views](xref:112611) that use this List Editor.