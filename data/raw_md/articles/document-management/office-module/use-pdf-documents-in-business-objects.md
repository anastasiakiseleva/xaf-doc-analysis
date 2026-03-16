---
uid: "405488"
title: Use PDF Documents in Business Objects
seealso: []
---
# Use PDF Documents in Business Objects

Blazor and WinForms XAF applications allow you to display PDF documents in a PDF Viewer property editor. The editor can display PDF documents stored in properties of the following types:

* Byte array
* Types that implement the @DevExpress.Persistent.Base.IFileData interface

> [!note]
> WinForms PDF Viewer saves documents in database as IFileData or byte[].

> [!tip]
> Try out the PDF Viewer in the **MainDemo.NET.EFCore** demo application installed as part of the XAF package. The default application location is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore_.

![PDF Viewer in an XAF Blazor Application](~/images/xaf-blazor-pdf-viewer-in-application.png)


You can add the PDF Viewer to your application as follows:

1. Enable the [Office Module](xref:400003#add-the-office-module-to-your-application).
2. Assign `PdfViewerPropertyEditor` to a file data property in code or in the [Model Editor](xref:112582) (_MySolution.Blazor.Server\Model.xafml_ (for Blazor) or _MySolution.Win\Model.xafml_ (for WinForms)).

## Assign the PDF Viewer Property Editor to a Property in Code

Decorate a business class property with the @DevExpress.Persistent.Base.EditorAliasAttribute and pass the `PdfViewerPropertyEditor` value as the attribute parameter:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[EditorAlias(EditorAliases.PdfViewerPropertyEditor)] 
public virtual byte[] Data { get; set; }
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
private byte[] data;
[EditorAlias(EditorAliases.PdfViewerPropertyEditor)] 
public byte[] Data { 
    get { return data; }
    set { SetPropertyValue(nameof(Data), ref data, value); }
}
```
***

## Assign the PDF Viewer Property Editor to a Property in the Model Editor

1. Double-click the corresponding _Model.xafml_ file to start the [Model Editor](xref:112582):
    * _MySolution.Blazor.Server\Model.xafml_ (for Blazor)
    * _MySolution.Win\Model.xafml_ (for WinForms)
2. Navigate to the following node: **Views | {AppName}.Module.BusinessObjects | {ObjectType} | {ObjectType}_DetailView | Items | {Property Name}**. 
3. Set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType property to one of the following values:

    * `DevExpress.ExpressApp.Office.Blazor.Editors.PdfViewerPropertyEditor` (for Blazor)
    * `DevExpress.ExpressApp.Office.Win.PdfViewerPropertyEditor` (for WinForms)

![PropertyEditorType property in Model Editor](~/images/xab-pdf-viewer-in-model-editor.png)

[`PdfViewerPropertyEditor`]: DevExpress.ExpressApp.Editors.EditorAliases.PdfViewerPropertyEditor

## Display the Document in a Separate Window (WinForms)
In WinForms applications, you select the **Show in popup** context menu command to open the document in a new popup window.

![Show in popup context menu command](~/images/xaf-win-pdf-viewer-show-in-popup.png)

![Document in a Separate Window](~/images/xaf-win-pdf-viewer-document-in-popup.png)