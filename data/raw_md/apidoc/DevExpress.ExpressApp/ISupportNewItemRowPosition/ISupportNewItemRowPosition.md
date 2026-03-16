---
uid: DevExpress.ExpressApp.ISupportNewItemRowPosition
name: ISupportNewItemRowPosition
type: Interface
summary: Declares members implemented by [List Editors](xref:113189) that support a new item row.
syntax:
  content: public interface ISupportNewItemRowPosition
seealso:
- linkId: DevExpress.ExpressApp.ISupportNewItemRowPosition._members
  altText: ISupportNewItemRowPosition Members
---
A new item row allows end-users to create a new object directly in a [List View](xref:112611). Three built-in **XAF** List Editors implement the **ISupportNewItemRowPosition** interface. They are the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and [](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor).

When implementing a custom List Editor, support this interface if the List Editor has a configurable new item row.