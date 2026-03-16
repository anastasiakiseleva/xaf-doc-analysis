---
uid: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CreateCustomXafReportVerbsManager
name: CreateCustomXafReportVerbsManager
type: Event
summary: Occurs when the `XafReportVerbsManager` object is created for the Report Designer.
syntax:
  content: public event EventHandler<CreateCustomXafReportVerbsManagerEventArgs> CreateCustomXafReportVerbsManager
seealso: []
---
Handle this event to provide custom implementation of an `XafReportVerbsManager` object by setting an instance of this object to the handler's `Manager` parameter.  Set the `Handled` parameter to true  to disable use of the default `XafReportVerbsManager`. The `XafReportVerbsManager` class extends the standard list of verbs and adds the ExportLayout and ImportLayout commands to the Report Designer. You can set `Manager` to `null` to disable the extension.

The `XtraReport.Name` property is automatically loaded in the **Report Designer** when the **Import layout from file** command is executed. This ensures avoiding the situation when the REPX file is created from a report with a modified `XtraReport.Name` value and the modified name was used in scripts. Use the `CreateCustomXafReportVerbsManager` event if you want to customize this behavior.