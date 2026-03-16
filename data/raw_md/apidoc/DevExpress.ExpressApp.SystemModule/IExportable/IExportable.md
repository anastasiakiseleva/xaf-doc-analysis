---
uid: DevExpress.ExpressApp.SystemModule.IExportable
name: IExportable
type: Interface
summary: Declares members to be implemented by [List Editors](xref:113189) to support the [Printing](xref:113012) and [Exporting](xref:113362) functionalities in List Editors.
syntax:
  content: public interface IExportable
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IExportable._members
  altText: IExportable Members
---
To enable printing and exporting for a custom List Editor, implement the `IExportable` interface.

Printing is provided by the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController) Controller.

Export is provided by the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) Controller.

XAF activates the following Actions for the List Views where List Editors implement the `IExportable` interface:

| Controller | Actions|
|-|-|
|[PrintingController](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController)| [PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction), [PrintPreviewAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintPreviewAction), [PageSetupAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PageSetupAction)|
|[ExportController](xref:DevExpress.ExpressApp.SystemModule.ExportController)|[ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction)|

Currently, the following built-in List Editors support this interface in Windows Forms applications:

* [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor)
* [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)
* [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor)
* [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor)
* [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)