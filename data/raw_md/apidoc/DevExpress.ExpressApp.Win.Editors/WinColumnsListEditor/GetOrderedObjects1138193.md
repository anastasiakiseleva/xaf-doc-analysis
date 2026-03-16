---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.GetOrderedObjects
name: GetOrderedObjects()
type: Method
summary: Returns an ordered list of objects that represent the [WinColumnsListEditor.ColumnView](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.ColumnView)'s rows.
syntax:
  content: public IList GetOrderedObjects()
  return:
    type: System.Collections.IList
    description: An ordered list of objects that represent the **ColumnView**'s rows.
seealso: []
---
This method is not intended to be called from your code. It is implemented as a part of the **IOrderProvider** interface. The [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor) implements this interface to support the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s [Actions](xref:112622) for the [Views](xref:112611) that use this List Editor.