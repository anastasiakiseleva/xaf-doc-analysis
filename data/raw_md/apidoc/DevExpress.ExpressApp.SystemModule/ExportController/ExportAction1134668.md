---
uid: DevExpress.ExpressApp.SystemModule.ExportController.ExportAction
name: ExportAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ExportController)'s **Export** [Action](xref:112622).
syntax:
  content: public SingleChoiceAction ExportAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object that is the **Export** Action.
seealso:
- linkId: "113287"
- linkId: "113362"
---
The **ExportAction** is a **SingleChoiceAction** Action that allows end-users to export data displayed in the current List View to various formats. The Action is active when the current List View's [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) supports the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface and the editor's control supports the [](xref:DevExpress.XtraPrinting.IPrintable) interface.

The List Editor determines the target formats that the Action can export. The Action fills its [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) list based on the List Editor's [IExportable.SupportedExportFormats](xref:DevExpress.ExpressApp.SystemModule.IExportable.SupportedExportFormats) property. To customize the `Items` list after population, handle the [ExportController.ExportActionItemsCreated](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportActionItemsCreated) event.

Windows Forms
:   ![Export_1](~/images/export_1116692.png)![Export_SaveAs](~/images/export_saveas116766.png)

Currently, the following built-in List Editors implement the `IExportable` interface:

In Windows Forms applications:

* [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor)
* [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)
* [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor)
* [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor)
* [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)

To activate the **Export** Action for a custom List Editor, support the `IExportable` interface in the List Editor class' declaration.

If you need a custom List Editor to be exported by the **Export** Action instead of the current List View's List Editor, set the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) property.

To determine why the **Export** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **Export** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).