---
uid: DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Printable
name: Printable
type: Property
summary: Specifies the [](xref:DevExpress.XtraPrinting.IPrintable) control that a List Editor uses to export data.
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An `IPrintable` object that is the control used to export data from a List Editor.
seealso:
- linkId: "113287"
---
The ExportController uses `XtraPrintingLibrary` to perform export operations under a List Editor's control. This library exposes types that export data from the controls that implement the [](xref:DevExpress.XtraPrinting.IPrintable) interface. So, the ExportController exports data only from the List Editors that embed a control that implements the `IPrintable` interface. When handling the [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport) event, use the `Printable` parameter to access the printable control of the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) List Editor.

Use the printable control returned by this property to set export options. The following table details how to access the export options of the printable controls used by the built-in List Editors:

**Windows Forms specific List Editors**

| List Editor | Printing Control | Export Options |
|---|---|---|
| [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) | [](xref:DevExpress.XtraGrid.GridControl) | [GridView.OptionsPrint](xref:DevExpress.XtraGrid.Views.Grid.GridView.OptionsPrint) |
| [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor) | [](xref:DevExpress.XtraTreeList.TreeList) | [TreeList.OptionsPrint](xref:DevExpress.XtraTreeList.TreeList.OptionsPrint) |
| [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor) | [](xref:DevExpress.XtraPivotGrid.PivotGridControl) | [PivotGridControl.OptionsPrint](xref:DevExpress.XtraPivotGrid.PivotGridControl.OptionsPrint) |
| [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor) | [](xref:DevExpress.XtraCharts.ChartControl) | [ChartControl.OptionsPrint](xref:DevExpress.XtraCharts.ChartControl.OptionsPrint) |
| [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) | [](xref:DevExpress.XtraScheduler.SchedulerControl) | [SchedulerControl.OptionsPrint](xref:DevExpress.XtraScheduler.SchedulerControl.OptionsPrint) |