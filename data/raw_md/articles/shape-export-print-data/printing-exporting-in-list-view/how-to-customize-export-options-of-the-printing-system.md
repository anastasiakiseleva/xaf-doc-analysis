---
uid: "113283"
seealso:
- linkId: DevExpress.XtraPrinting.PrintingSystemBase.ExportOptions
- linkId: "113287"
title: 'How to: Customize Export Options of the Printing System'
owner: Ekaterina Kiseleva
---
# How to: Customize Export Options of the Printing System

In a Windows Forms XAF application, end-users have an ability to export [View](xref:112611) print previews to various formats. Before exporting, an **Export Options** dialog is invoked. The format-specific options can be changed using this dialog, for example, the HTML title or XLS sheet name.

![ExportOptions1](~/images/exportoptions1116675.png)

> [!NOTE]
> To learn how to specify export options for reports, refer to the [How to: Customize the Report Export Options](xref:117813) topic.

* The [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController), supplied with the **System** module, exposes the [PrintingController.PrintingSettingsLoaded](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintingSettingsLoaded) event. You can handle this event to access the [](xref:DevExpress.XtraPrinting.PrintingSystem) object and modify default export options. To do this, implement the following [View Controller](xref:112621):
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.XtraPrinting;
	using DevExpress.ExpressApp.Win.SystemModule;
	// ...
	public class ConfigurePrintingSystemViewController : ViewController {
	    private PrintingController printingService;
	    protected override void OnActivated() {
	        base.OnActivated();
	        printingService = Frame.GetController<PrintingController>();
	        if (printingService != null)
	            printingService.PrintingSettingsLoaded += printingService_PrintingSettingsLoaded;
	    }
	    private void printingService_PrintingSettingsLoaded(
	        object sender, PrintableComponentLinkEventArgs e) {
	        ConfigurePrintingSystem(e.PrintableComponentLink.PrintingSystem);
	    }
	    private void ConfigurePrintingSystem(PrintingSystemBase printingSystem) {
	        SetHtmlOptions(printingSystem.ExportOptions.Html);
	        SetPdfOptions(printingSystem.ExportOptions.Pdf);
	        SetXlsOptions(printingSystem.ExportOptions.Xls);
	    }
	    private static void SetXlsOptions(XlsExportOptions xlsExportOptions) {
	        // XLS-specific options:
	        xlsExportOptions.SheetName = "CustomXlsSheetTitle";
	        xlsExportOptions.ShowGridLines = true;
	    }
	    private static void SetPdfOptions(PdfExportOptions pdfExportOptions) {
	        // PDF-specific options:
	        pdfExportOptions.DocumentOptions.Title = "CustomPdfTitle";
	        pdfExportOptions.ImageQuality = PdfJpegImageQuality.Medium;
	    }
	    private static void SetHtmlOptions(HtmlExportOptions htmlExportOptions) {
	        // HTML-specific options:
	        htmlExportOptions.Title = "CustomHtmlTitle";
	        htmlExportOptions.ExportMode = HtmlExportMode.SingleFilePageByPage;
	        htmlExportOptions.PageBorderColor = System.Drawing.Color.Gray;
	        htmlExportOptions.EmbedImagesInHTML = true;
	    }
	    private static void SetGeneralOptions(PrintPreviewOptions printPreviewOptions) {
	        // General options:
	        printPreviewOptions.DefaultFileName = "CustomFileName";
	    }
	    protected override void OnDeactivated() {
	        if (printingService != null)
	            printingService.PrintingSettingsLoaded -= printingService_PrintingSettingsLoaded;
	        base.OnDeactivated();
	    }
	}
	```
	***
	
	[!include[ShowPreviewDialog_Note](~/templates/showpreviewdialog_note11198.md)]
	
	You can access various export options in the **ConfigurePrintingSystem**, **SetXlsOptions**, **SetPdfOptions**, **SetHtmlOptions** and **SetGeneralOptions** methods. The following classes provide the available properties:
	
	* [](xref:DevExpress.XtraPrinting.ExportOptions)
	* [](xref:DevExpress.XtraPrinting.XlsExportOptions)
	* [](xref:DevExpress.XtraPrinting.PdfExportOptions)
	* [](xref:DevExpress.XtraPrinting.HtmlExportOptions)
	* [](xref:DevExpress.XtraPrinting.PrintPreviewOptions)
	
	> [!NOTE]
	> You can implement additional methods for other export formats, and call them from the **ConfigurePrintingSystem** method.
* Run the Windows Forms application. Execute the **PrintPreview** Action in any View. In the invoked **Preview** dialog, click **File** | **Export Document…** and select the export format. You will see that the default export settings are changed (modified settings are highlighted in the screenshot).
	
	![ExportOptions2](~/images/exportoptions2116682.png)
	
	The default file name in the **Save As** dialog is also changed to "CustomFileName"
* If it is required to disable the **Export Options** dialog and always use the default options, add the following code to the **SetGeneralOptions** method:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	private static void SetGeneralOptions(PrintPreviewOptions printPreviewOptions) {
	    // ...
	    printPreviewOptions.ShowOptionsBeforeExport = false;
	}
	```
	***
