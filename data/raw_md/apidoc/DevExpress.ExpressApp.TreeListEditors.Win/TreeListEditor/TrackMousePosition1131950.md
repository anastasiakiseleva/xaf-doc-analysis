---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.TrackMousePosition
name: TrackMousePosition
type: Property
summary: Specifies whether mouse tracking is enabled for the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor).
syntax:
  content: public bool TrackMousePosition { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** to enable mouse tracking; otherwise **false**.'
seealso: []
---
When this property is set to **true**, moving the mouse within the **TreeListEditor**'s region changes the focus to the row that is under the mouse pointer. This property is automatically set to **true** in Lookup Property Editors'  [List Views](xref:112611) that are represented by the **TreeListEditor**.