---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction
name: PrintAction
type: Property
summary: Represents the **Print** [Action](xref:112622).
syntax:
  content: public SimpleAction PrintAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Print** Action.
seealso: []
---
The **Print** Action invokes the **Print** dialog, where an end-user can set up printing options, and print the prepared page.

![PrintingModule_1](~/images/printingmodule_1115834.png)

This Action is added to the **Print** [Action Container](xref:112610), which is available in the **File** main menu.

![PrintingModule](~/images/printingmodule115833.png)

This Action is enabled only for root Views.