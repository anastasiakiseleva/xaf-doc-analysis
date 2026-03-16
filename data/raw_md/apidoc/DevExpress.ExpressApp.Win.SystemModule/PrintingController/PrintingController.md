---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController
name: PrintingController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that provides printing functionality in the Windows Forms  applications.
syntax:
  content: 'public class PrintingController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.PrintingController._members
  altText: PrintingController Members
- linkId: "113012"
- linkId: "113283"
---
The **PrintingController** [Controller](xref:112621) is provided by the [System Module](xref:118046), and is activated for Detail Views whose control implements the [](xref:DevExpress.XtraPrinting.IPrintable) interface and List Views whose [List Editor](xref:113189) implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface. Contains the [PrintingController.PageSetupAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PageSetupAction), [PrintingController.PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction) and [PrintingController.PrintPreviewAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintPreviewAction) [Actions](xref:112622), allowing end-users to print the current View. These Actions are added to the **Print** [Action Container](xref:112610), available in the **File** main menu.

![PrintingModule](~/images/printingmodule115833.png)

The **Print** Action Container is also available in the context menu and main toolbar of the [NestedFrameTemplateV2](xref:112609). Note that only the **PrintPreview** Action is available in nested List Views.

![PrintingModule_3](~/images/printingmodule_3116763.png)

To execute these Actions, the [Printing-Exporting](xref:2079) system is used. It supplies many features, such as export to various formats, sending via email, scaling, zooming, numbering pages, UI skinning and so on. This system works with the controls that implement the **DevExpress.XtraPrinting.IPrintable** interface. This interface is implemented in many controls representing object collections, for example: **XtraGrid**, **XtraScheduler** and **XtraTreeList**. To customize the behavior of these Actions, you can subscribe to the [PrintingController.CustomGetPrintableControl](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomGetPrintableControl) and [PrintingController.PrintingSettingsLoaded](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintingSettingsLoaded) events, exposed by the **PrintingController**. Refer to the [How to: Customize Export Options of the Printing System](xref:113283) topic, for an example.