---
uid: DevExpress.ExpressApp.Model.IModelAction.CaptionFormat
name: CaptionFormat
type: Property
summary: Specifies the format for a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) caption.
syntax:
  content: |-
    [DefaultValue("{0}")]
    string CaptionFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A format string for a **SingleChoiceAction** caption.
seealso: []
---
This string is formatted using two parameters. The first one is the caption of the **SingleChoiceAction** ([ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption)) and the second is the caption of the Action's default item ([ChoiceActionBase.DefaultItemCaption](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.DefaultItemCaption)). For example, suppose you have a **SingleChoiceAction** whose caption is **Process Order**, and its default item has a **Quick Process** caption. If you specify **{0} - {1}** as the **CaptionFormat**, the resulting caption will be **Process Order - Quick Process**. If you specify **{0} Action** as the caption format, the resulting caption will be **Process Order Action**.