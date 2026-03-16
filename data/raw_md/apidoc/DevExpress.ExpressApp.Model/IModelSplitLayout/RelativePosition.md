---
uid: DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition
name: RelativePosition
type: Property
summary: Specifies the splitter position as a percentage.
syntax:
  content: |-
    [DefaultValue(-1)]
    float RelativePosition { get; set; }
  parameters: []
  return:
    type: System.Single
    description: The splitter position as a percentage. Set to a value between 0 and 100 to move the splitter between top/left and bottom/right View borders.<br/>`-1` if the @DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition property defines the splitter position.
seealso: []
---
You can use the [Model Editor](xref:112830) to specify the `RelativePosition` property value at design time and runtime. The property value is set automatically when a user moves the splitter. 

The @DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition property takes priority over the @DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition property. If @DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition value is specified (in UI or in code), the  @DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition property is not in effect.
