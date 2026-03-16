---
uid: '400003'
title: Office Module (Rich Text Editor, Spreadsheet Editor, PDF Viewer)
seealso: []
---
# Office Module (Rich Text Editor, Spreadsheet Editor, PDF Viewer)

The Office Module integrates the following DevExpress controls into an XAF application:

| Platform | Rich Text Editor | Spreadsheet Editor | PDF Viewer |
|:---:|:---:|:---:|:---:|
| **Blazor** | @DevExpress.Blazor.RichEdit.DxRichEdit | Not supported | @DevExpress.Blazor.PdfViewer.DxPdfViewer |
| **WinForms** | @DevExpress.XtraRichEdit.RichEditControl | @DevExpress.XtraSpreadsheet.SpreadsheetControl | @DevExpress.XtraPdfViewer.PdfViewer |

> [!tip]
> Try out the Office Module in the **MainDemo.NET.EFCore** demo application that ships with XAF. Refer to Detail Views of the following business objects: Note (Rich Text Editor), Resume (PDF Viewer).
> You can find the demo in the following folder: _[!include[](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore_.

## Add the Office Module to Your Application

To enable the Office module in your application follow the steps below:

1. Install NuGet packages that contain the Office module:
    * [DevExpress.ExpressApp.Office](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office)
    * [DevExpress.ExpressApp.Office.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Blazor)
    * [DevExpress.ExpressApp.Office.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Win)
2. Navigate to the _MyApplication.Blazor.Server\Startup.cs_ file (for Blazor) or _MyApplication.Win\Startup.cs_ file (for WinForms) and call the [AddOffice](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeOptions})) (for Blazor) / [AddOffice](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Office.Win.OfficeOptions})) (for WinForms) method:

    # [ASP.NET Core Blazor](#tab/tabid-appbuilder-blazor)

    [!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Blazor_example.md)]
      
    # [Windows Forms](#tab/tabid-appbuilder-winforms)
      
    [!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Win_example.md)]

    ***

XAF offers other methods to integrate the Office Module into a newly created or existing application. For more information, refer to the following topic: <xref:118047>.

## Add and Customize Office Components 

Refer to the following help topics for details on how to work with the office components:

### Rich Text Editor
* <xref:400004>
* <xref:400063>
* <xref:400006> 

### Spreadsheet Editor
* <xref:400931>
* <xref:400894>
* <xref:401211> 

### PDF Viewer
* <xref:405488>
* <xref:405489>


## Office Module Components

### Modules

| Platform | Module | NuGet package |
| -------- | ------ | ------------- |
| Platform-agnostic | @DevExpress.ExpressApp.Office.OfficeModule | [DevExpress.ExpressApp.Office](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office) |
| ASP.NET Core Blazor | @DevExpress.ExpressApp.Office.Blazor.OfficeBlazorModule | [DevExpress.ExpressApp.Office.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Blazor) |
| Windows Forms | @DevExpress.ExpressApp.Office.Win.OfficeWindowsFormsModule | [DevExpress.ExpressApp.Office.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Win) |

On Linux, the Office Module for Blazor might need extra libraries: [Use Office File API on Linux - Prerequisites](xref:401441#prerequisites).

### Application Model Extensions
The Office Module extends the [Application Model](xref:112579) with the following properties:

{|
|-
! Module
! Extended node
! Property
|-

| OfficeModule
| @DevExpress.ExpressApp.Model.IModelMember
| [IModelRichTextFormatSettings.DocumentStorageFormat](xref:DevExpress.ExpressApp.Office.IModelRichTextFormatSettings.DocumentStorageFormat)<br/>[IModelSpreadsheetPropertyEditorSettings.EnableFormulaBar](xref:DevExpress.ExpressApp.Office.IModelSpreadsheetPropertyEditorSettings.EnableFormulaBar)
|-

| rowspan="2" | OfficeWindowsFormsModule
| @DevExpress.ExpressApp.Model.IModelColumn
| [IModelRichTextColumn.CustomHeight](xref:DevExpress.ExpressApp.Office.Win.IModelRichTextColumn.CustomHeight)
|-

| @DevExpress.ExpressApp.Model.IModelPropertyEditor
| [IModelWinOfficeMenuManagerSettings.MenuManagerType](xref:DevExpress.ExpressApp.Office.Win.IModelWinOfficeMenuManagerSettings.MenuManagerType)
|}
