---
uid: DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportActionEnableMode
name: ShowInReportActionEnableMode
type: Property
summary: Specifies when the [PrintSelectionBaseController.ShowInReportAction](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportAction) is disabled depending on data modifications in the current View.
syntax:
  content: public PrintSelectionBaseController.ActionEnabledMode ShowInReportActionEnableMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ActionEnabledMode
    description: A value that specifies when the **ShowInReportAction** is disabled.
seealso: []
---
Data for a selected report is always read from a separate Object Space, so unsaved changes are not included. To specify the Action availability when there are changes in the current View, use one of the following values:

* `None` - Action is not disabled.
* `ModifiedChanged` - Action is disabled in accordance with the [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) event. Used by default.

The `ShowInReportActionEnableMode` default value is taken from the static @DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportActionEnableModeDefault field.

Handle the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event to modify the default value or [introduce a new Controller](xref:112676), access the [](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController) controller, and change the `ShowInReportActionEnableMode` property value.