---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.PageSetupAction
name: PageSetupAction
type: Property
summary: Represents the **PageSetup** [Action](xref:112622).
syntax:
  content: public SimpleAction PageSetupAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Page Setup** Action.
seealso: []
---
The **PageSetup** Action invokes the **Page Setup** dialog, where an end-user can set up page printing options:

![PrintingModule_1](~/images/xaf-printing-page-setup.png)

This Action is added to the **Print** [Action Container](xref:112610), which is available in the **File** main menu.

![PrintingModule](~/images/xaf-printing-print-actions.png)

This Action is enabled only for root Views.