---
uid: DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition
name: SplitterPosition
type: Property
summary: Specifies the splitter position within the View, in pixels.
syntax:
  content: |-
    [DefaultValue(150)]
    int SplitterPosition { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: The distance, in pixels, between the splitter and the left/top View border.
seealso:
- linkId: "113249"
---
The @DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition property takes priority over the @DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition property. If @DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition value is specified (in the UI or in code), the  @DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition property is not in effect.
