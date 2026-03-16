---
uid: DevExpress.ExpressApp.SystemModule.ExportController
name: ExportController
type: Class
summary: An abstract [](xref:DevExpress.ExpressApp.ViewController) descendant, that contains the **Export** [Action](xref:112622).
syntax:
  content: 'public abstract class ExportController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController._members
  altText: ExportController Members
- linkId: "113362"
---
XAF activates the `ExportController` [Controller](xref:112621) in all [Views](xref:112611). It provides the export functionality presented by the **Export** Action:

![XAF Windows Forms Export Controller, DevExpress](~/images/exportcontroller_win116962.png)

XAF activates this Action when the current List View's List Editor implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface. To access this editor, use the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) property. The editor's [IExportable.SupportedExportFormats](xref:DevExpress.ExpressApp.SystemModule.IExportable.SupportedExportFormats) property is used to populate the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection. If the `SupportedExportFormats` list is empty, the Action is not activated. For details on the **Export** Action, refer to the description of the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) property, which provides access to this Action.

`ExportController` allows you to change the **Export** Action's behavior. Use the following events: [ExportController.ExportActionItemsCreated](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportActionItemsCreated) and [ExportController.Exported](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exported). Examples of handling these events are provided in the [How to: Customize the Export Action Behavior](xref:113287) topic. In addition, you can set another List Editor to be exported by the Action instead of the current List View's List Editor. To do this, set it to the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) property.

`ExportController` serves as the base for the WinForms-specific [](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController). You usually do not inherit this class. Manual inheritance requires you to implement features that platform-specific descendants already provide. You can inherit the `WinExportController` class if you want to add custom functionality.

To determine whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property (see [How to: Detect a Lookup List View in Code](xref:112908)). If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information about `ExportController` and its **Export** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).