---
uid: "113548"
seealso:
- linkId: "402188"
title: File Attachment Properties
---
# File Attachment Properties

XAF can display the **File Data** or **PDF Viewer** property editor for properties that hold file data. These properties must use a type that implements the @DevExpress.Persistent.Base.IFileData interface. For instance, XAF's built-in `FileData` type.

File Data Property Editor (ASP.NET Core Blazor, WinForms)
:   Enable the [File Attachments](xref:112781) module to display objects that implement the `IFileData` interface in the File Data Property Editor. The following lessons contain a detailed explanation on how to use the File Attachments module: [Attach files to objects](xref:403288).
PDF Viewer Property Editor (ASP.NET Core Blazor, WinForms)
:   Enable the [Office Module](xref:400003) and assign `PdfViewerPropertyEditor` to a file data property to display PDF files in the PDF Viewer. Refer to the following topic for additional details: <xref:405488>.

# [EF Core](#tab/tabid-csharp-efcore)
```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace MainDemo.Module.BusinessObjects;

[DefaultClassOptions]
public class Resume : BaseObject {
    // ... 
    [FileTypeFilter("pdf-only", "PDF file", "*.pdf")]
    public virtual FileData File { get; set; }
    [EditorAlias(EditorAliases.PdfViewerPropertyEditor)]
    public FileData ResumeView => File;
}
```

# [XPO](#tab/tabid-csharp-xpo)
```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;

namespace MainDemo.Module.BusinessObjects;

[FileAttachment(nameof(File))]
[DefaultClassOptions]
public class Resume : BaseObject {
    // ...
    [Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
    [FileTypeFilter("pdf-only", "PDF file", "*.pdf")]
    public FileData File {
        get {
            return file;
        }
        set {
            SetPropertyValue(nameof(File), ref file, value);
        }
    }
    [EditorAlias(EditorAliases.PdfViewerPropertyEditor)]
    public FileData ResumeView => File;
}
```
***

![File Data and PDF Viewer Property Editors in an XAF Blazor Application](~/images/xaf-blazor-file-data-editors.png)
[`PdfViewerPropertyEditor`]: DevExpress.ExpressApp.Editors.EditorAliases.PdfViewerPropertyEditor

> [!tip]
> Try out File Data editor and PDF Viewer in the **MainDemo.NET.EFCore** demo application installed as part of the XAF package (see **Resume** objects). The default application location is _%PUBLIC%\Documents\DevExpress Demos 25.1\Components\XAF\MainDemo.NET.EFCore_.


## ASP.NET Core Blazor

### DxFileDataPropertyEditor

[!include[dxfiledatapropertyeditor](~/templates/dxfiledatapropertyeditor.md)]

#### Customize Maximum File Size and Allowed File Types

The following code snippet changes the uploaded file's maximum size and specifies the allowed file types.

[!include[dxfileinputmodel-customization](~/templates/dxfileinputmodel-customization.md)]

### PdfViewerPropertyEditor

`DevExpress.ExpressApp.Office.Blazor.Editors.PdfViewerPropertyEditor` displays PDF documents in a PDF Viewer property editor.

## WinForms

![File Attachment Properties WinForms](~/images/xaf-win-file-properties.png)

Each WinForms Property Editor has a control that displays the corresponding property in a [Detail View](xref:112611), and a repository item that displays the property in a [List Editor](xref:113189) that supports in-place editing.
### FileDataPropertyEditor

The editor allows a user to perform the **Open**, **SaveTo**, and **ClearContent** Actions that **FileAttachmentController** contains. Use the editor's context menu to execute these Actions. You can also click the editor's ellipsis button or press _Enter_ to execute the **Open** Action.

Control
:   **FileDataEdit** - a [](xref:DevExpress.XtraEditors.ButtonEdit) descendant. The editor uses [OpenFileDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.openfiledialog) to attach a file.

Repository Item
:   **RepositoryItemFileDataEdit** - a [](xref:DevExpress.XtraEditors.Repository.RepositoryItemButtonEdit) descendant.


### PdfViewerPropertyEditor

`DevExpress.ExpressApp.Office.Win.PdfViewerPropertyEditor` displays PDF documents in a PDF Viewer property editor.
