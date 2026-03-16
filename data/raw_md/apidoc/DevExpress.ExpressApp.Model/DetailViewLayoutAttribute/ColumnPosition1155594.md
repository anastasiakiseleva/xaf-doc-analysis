---
uid: DevExpress.ExpressApp.Model.DetailViewLayoutAttribute.ColumnPosition
name: ColumnPosition
type: Property
summary: Returns the @DevExpress.ExpressApp.Model.LayoutColumnPosition collection.
syntax:
  content: public LayoutColumnPosition? ColumnPosition { get; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.ExpressApp.Model.LayoutColumnPosition}
    description: The position of a column in which the editor of the target property is placed.
seealso: []
---
This property is in effect if the target property is in the **SimpleEditors** [layout group](xref:113680) with two columns. The second column is generated automatically when the number of editors in a group is more than the @DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewLayoutNodesGenerator.EditorsMaxCountForLayoutInFlow value.

[!include[detailviewattribute](~/templates/detailviewattribute.md)]

For information on other ways to customize a Detail View layout, refer to the following help topic: [Detail View Layout Customization](xref:112817).
