---
uid: DevExpress.ExpressApp.SystemModule.ExportController.ExportActionItemsCreated
name: ExportActionItemsCreated
type: Event
summary: Occurs after the **Export** Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection has been populated.
syntax:
  content: public event EventHandler<EventArgs> ExportActionItemsCreated
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController.CustomExport
---
By default, the **Export** Action's `Items` collection is populated based on the [IExportable.SupportedExportFormats](xref:DevExpress.ExpressApp.SystemModule.IExportable.SupportedExportFormats) list of the Controller's [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) editor. To customize the `Items` collection after it's been populated, handle the `ExportActionItemsCreated` event. Note that the exporter used by default can only export data to the formats specified by the [](xref:DevExpress.XtraPrinting.ExportTarget) enumeration. So, the Action's Items must be of the `ExportTarget` type only, if you use the default export.

> [!NOTE]
> If the control of the Controller's [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) Editor doesn't implement the [](xref:DevExpress.XtraPrinting.IPrintable) interface or the `Exportable` Editor is not specified, the **Export** Action's `Items` collection remains empty, the `ExportActionItemsCreated` event is not raised and the **Export** Action is not activated.

The following code demonstrates how to place the required item to the first place in the Export Action's Items collection:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.XtraPrinting;
//...
public class MyExportViewController : ViewController<ListView> {
    private ExportController exportController;

    protected override void OnActivated() {
        base.OnActivated();
        exportController = Frame.GetController<ExportController>();
        if(exportController != null) {
            exportController.ExportActionItemsCreated += ExportController_ExportActionItemsCreated;
        }
    }
    private void ExportController_ExportActionItemsCreated(object sender, EventArgs e) {
        var exportAction = exportController.ExportAction;
        if(exportAction.Items.FirstActiveItem != null && (ExportTarget)exportAction.Items.FirstActiveItem.Data != ExportTarget.Xls) {
            ChoiceActionItem item = exportAction.Items.Find(ExportTarget.Xls);
            exportAction.Items.Remove(item);
            exportAction.Items.Insert(0, item);
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(exportController != null) {
            exportController.ExportActionItemsCreated -= ExportController_ExportActionItemsCreated;
        }
    }
}
```
