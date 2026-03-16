---
uid: "113012"
seealso:
- linkId: "113283"
title: Printing
owner: Ekaterina Kiseleva
---
# Printing

The printing system allows you to print [Views](xref:112611). This topic describes the basics of using this WinForms-specific system.

The printing system contains the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController) [View Controller](xref:112621). It is activated for Detail Views and List Views. All the functionalities it represents are in the following Actions.

* **Page Setup…**
	
	Invokes the **Page Setup** window, where an end-user can set up page printing options.
	
	![PrintingModule_1](~/images/printingmodule_1115834.png)
	
	This Action is enabled only for root Views.
* **Print Preview…**
	
	Shows how the current View will be printed. An end-user can make changes in the prepared page; for example; add color, margins, header, footer and so on. To accomplish this, there are numerous options in the Preview window. After you are satisfied with the preview, you can print it using the **File** | **Print** menu item.
	
	![Tutorial_EM_Lesson3_1_0](~/images/tutorial_em_lesson3_1_0115583.png)
* **Print…**
	
	Invokes the **Print** dialog, where an end-user can set up printing options and print the prepared page.
	
	![PrintingModule_2](~/images/printingmodule_2115835.png)
	
	This Action is enabled only for root Views.

All the Actions are added to the Print [Action Container](xref:112610), which displays them as an item group in the **File** main menu.

![PrintingModule](~/images/printingmodule115833.png)

The **PrintPreview** Action is also available in nested List Views.

![PrintingModule_3](~/images/printingmodule_3116763.png)

The options specified in the "Page Setup" dialog and the 'Header and Footer' options, which are set in the Preview dialog, are saved automatically. The [](xref:DevExpress.ExpressApp.Win.SystemModule.IModelPrintingSettings) node is added to the [Application Model](xref:112580), and filled with values each time printing settings are changed via the **PageSetup** or **PrintPreview** [Actions](xref:112622) for a [View](xref:112611). These options can be saved separately for each View, or they can be saved to the [](xref:DevExpress.ExpressApp.Model.IModelOptions) to affect all Views in an application. By default, the options set for a View affect all Views. You can change this behavior via the application project designer:

![PrintingSettingsStorage](~/images/printingsettingsstorage116313.png)

The **PrintingController** exposes two useful public events:

* [PrintingController.CustomGetPrintableControl](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomGetPrintableControl) - occurs after View controls have been instantiated. Allows you to specify the control that must be printed;
* [PrintingController.PrintingSettingsLoaded](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintingSettingsLoaded) - occurs when the **Print** Action is executed. Allows you to customize the [](xref:DevExpress.XtraPrinting.PrintableComponentLink) object, which represents a printing link to the printable control.

The XAF printing system actually uses the [XtraPrinting](xref:2403) library to print and preview XAF [Views](xref:112611). **XtraPrinting** enables printing for the controls that implement the [](xref:DevExpress.XtraPrinting.IPrintable) interface. So, if a View in an XAF application is represented by a control that supports the **IPrintable** interface, this View can be printed, and the printing's Actions are enabled for this View. A Detail View's control is a Layout Control, which is printable. So, Detail Views can be printed. List Views are represented by the controls specified by [List Editors](xref:113189). All Windows Forms built-in List Editors support the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface, which in its turn returns a printable control via the [IExportable.Printable](xref:DevExpress.ExpressApp.SystemModule.IExportable.Printable) property. So, all List Views can be printed as well. If you use a custom List Editor to display List Views, and you want its data to be printable, implement the **IExportable** interface in it, and the **DevExpress.XtraPrinting.IPrintable** interface in the control it uses. To learn how to implement the **IPrintable** interface in a standard control, refer to the [How to: Create a Printable ListView Descendant Implementing the IPrintable Interface](xref:3245) topic.

The printing system is demonstrated in the Feature Center Demo installed with **XAF**.