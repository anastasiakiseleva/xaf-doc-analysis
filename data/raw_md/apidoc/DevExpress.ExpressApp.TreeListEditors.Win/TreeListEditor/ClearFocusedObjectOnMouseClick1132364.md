---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.ClearFocusedObjectOnMouseClick
name: ClearFocusedObjectOnMouseClick
type: Property
summary: Specifies whether the focused object can be deselected by clicking on the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)'s region not occupied by a node.
syntax:
  content: public bool ClearFocusedObjectOnMouseClick { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if the focused object can be deselected by clicking on the **TreeListEditor**'s region not occupied by a node; otherwise, **false**. The default value is **true**."
seealso: []
---
This property affects how tree nodes are created via the **New** [Action](xref:112622), in a [List View](xref:112611) represented by the **TreeListEditor**. When a node is created via the **New** Action, it is created as a child of the currently focused node. If the **ClearFocusedObjectOnMouseClick** property is set to **true**, a user can click on the **TreeListEditor**'s region not occupied by a node, and this will deselect the focused node. If a user then uses the **New** Action, the new node will be created as root.