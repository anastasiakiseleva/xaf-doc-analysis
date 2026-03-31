---
uid: "117813"
seealso:
- linkId: "113283"
title: 'How to: Customize the Report Export Options'
---

# How to: Customize the Report Export Options

This example demonstrates how to access the [](xref:DevExpress.XtraPrinting.ExportOptions) object, which stores document export options for different formats. These options are applied when you export a report from a Report Viewer.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## 1. Implement an ExportConfigurator Helper Class

In the [platform-agnostic module](xref:118045), declare the following helper class:
	
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraPrinting;
// ...
public static class ExportConfigurator {
	public static void Setup(ExportOptions exportOptions) {
		SetHtmlOptions(exportOptions.Html);
		SetPdfOptions(exportOptions.Pdf);
		SetXlsOptions(exportOptions.Xls);
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
}
```

***

## 2. Handle the BeforeShowPreview Event

In the application's _Startup.cs file_, add the `OnBeforeShowPreview` event handler to the `builder.Modules.AddReports` method call. In this event handler, call the `ExportConfigurator.Setup` static method as shown below:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{5-7}
// ...
builder.Modules
    .AddReports(options => {
        // ...
		options.Events.OnBeforeShowPreview = context => {
			ExportConfigurator.Setup(context.Report.ExportOptions);
		};
    })
// ...
```

***
