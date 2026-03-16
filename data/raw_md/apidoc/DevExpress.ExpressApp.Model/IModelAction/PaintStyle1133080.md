---
uid: DevExpress.ExpressApp.Model.IModelAction.PaintStyle
name: PaintStyle
type: Property
summary: Specifies the [Action](xref:112622)'s paint style.
syntax:
  content: |-
    [DefaultValue(ActionItemPaintStyle.Default)]
    ActionItemPaintStyle PaintStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.ActionItemPaintStyle
    description: An [](xref:DevExpress.ExpressApp.Templates.ActionItemPaintStyle) enumeration value that specifies the Action's paint style.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.PaintStyle
---
To specify this property, invoke the Model Editor and navigate to an [!include[Node_Action](~/templates/node_action111373.md)] node: 

![PlainStyle property in Model Editor](~/images/PaintStyle_ModelEditor.png)

You can also specify this property in code. For more information, refer to the [ActionBase.PaintStyle](xref:DevExpress.ExpressApp.Actions.ActionBase.PaintStyle) property description.