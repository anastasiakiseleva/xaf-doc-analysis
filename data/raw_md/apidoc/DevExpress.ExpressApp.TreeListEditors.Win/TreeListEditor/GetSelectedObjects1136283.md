---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.GetSelectedObjects
name: GetSelectedObjects()
type: Method
summary: Provides access to the collection of objects that are currently selected in the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)'s TreeList control.
syntax:
  content: public override IList GetSelectedObjects()
  return:
    type: System.Collections.IList
    description: A list of the selected objects.
seealso: []
---
Use this method to access selected objects. To perform the required actions when the selection is changed, handle the [ListEditor.SelectionChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionChanged) event.