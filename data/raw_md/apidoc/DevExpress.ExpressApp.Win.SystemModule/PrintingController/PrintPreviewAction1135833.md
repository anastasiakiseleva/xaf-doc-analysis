---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintPreviewAction
name: PrintPreviewAction
type: Property
summary: Represents the **PrintPreview** [Action](xref:112622).
syntax:
  content: public SimpleAction PrintPreviewAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Print Preview** Action.
seealso: []
---
The **PrintPreview** Action shows how the current [View](xref:112611) will be printed. An end-user can make changes in the prepared page; for example; add color, margins, header, footer and so on. To accomplish this, there are numerous options in the **Preview** window.

![Tutorial_EM_Lesson3_1_0](~/images/xaf-printing-print-preview.png)

The **PrintPreview** Action is added to the **Print** [Action Container](xref:112610), which is available in the **File** main menu. This Action is also available in nested List Views.

![PrintingModule](~/images/xaf-printing-print-actions.png)