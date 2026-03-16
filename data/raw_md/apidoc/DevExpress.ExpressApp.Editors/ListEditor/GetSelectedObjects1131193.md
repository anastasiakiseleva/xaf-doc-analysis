---
uid: DevExpress.ExpressApp.Editors.ListEditor.GetSelectedObjects
name: GetSelectedObjects()
type: Method
summary: Provides access to the collection of objects that are currently selected in the [List Editor](xref:113189)'s control.
syntax:
  content: public abstract IList GetSelectedObjects()
  return:
    type: System.Collections.IList
    description: A list of the selected objects.
seealso: []
---
Use this method to access selected objects. To perform the required actions when the selection is changed, handle the [ListEditor.SelectionChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionChanged) event.

When deriving from the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class, override this method to return a collection of the selected objects.
If the List Editor's control does not support selection, return an empty collection. In this instance, set the [ListEditor.SelectionType](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType) property to **SelectionType.None**.