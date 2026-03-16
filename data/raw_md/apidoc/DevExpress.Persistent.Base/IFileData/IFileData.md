---
uid: DevExpress.Persistent.Base.IFileData
name: IFileData
type: Interface
summary: Declares members that implement the base functionality of file data objects.
syntax:
  content: public interface IFileData
seealso:
- linkId: DevExpress.Persistent.Base.IFileData._members
  altText: IFileData Members
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e965/how-to-store-file-attachments-in-the-file-system-instead-of-the-database-xpo-and-ef-core
  altText: 'How to: Store file attachments in the file system instead of the database'
- linkType: HRef
  linkId: https://github.com/egarim/FileDataDropBox
  altText: 'GitHub repository: Store file attachments in Dropbox instead of the database'
- linkType: HRef
  linkId: https://www.youtube.com/watch?v=lVfUeDj9T7U
  altText: 'How to: Store file attachments in Dropbox instead of the database (video)'
- linkId: 112781#read-compressed-files-in-the-filedata-database-table-from-external-non-xaf-net-applications
  altText: 'How to: Read Compressed Files in the FileData Database Table from External Non-XAF .NET Applications'
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-use-the-file-attachment-module-with-a-legacy-database
  altText: 'GitHub example: Use the File Attachment Module with a legacy database'
---
If your custom type implements the `IFileData` interface, XAF can display objects of this type in the **File Data** or **PDF Viewer** property editor. 

> [!Tip]
> Refer to the following file for a sample `FileData` class implementation:
_[!include[](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.EFCore\FileData.cs_ 
>> [!spoiler][Display FileData.cs code][Hide FileData.cs code]
>> ```csharp
using System;
using System.ComponentModel;
using System.IO;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Validation;
>> 
>> namespace DevExpress.Persistent.BaseImpl.EF {
    [DefaultProperty(nameof(FileName))]
    public class FileData : BaseObject, IFileData, IEmptyCheckable {
        private Byte[] content;
        public virtual Int32 Size { get; set; }
        public virtual String FileName { get; set; }
        public virtual Byte[] Content {
            get { return content; }
            set {
                if(content != value) {
                    content = value;
                    Size = content != null ? content.Length : 0;
                }
            }
        }
        [Browsable(false)]
        public Boolean IsEmpty {
            get { return String.IsNullOrEmpty(FileName); }
        }
        public void LoadFromStream(String fileName, Stream stream) {
            FileName = fileName;
            Byte[] bytes = new Byte[stream.Length];
            stream.Read(bytes, 0, bytes.Length);
            Content = bytes;
            ObjectSpace.SetModified(this);
        }
        public void SaveToStream(Stream stream) {
            if(String.IsNullOrEmpty(FileName)) {
                throw new InvalidOperationException();
            }
            stream.Write(Content, 0, Size);
            stream.Flush();
        }
        public void Clear() {
            Content = null;
            FileName = "";
            ObjectSpace.SetModified(this);
        }
        public override String ToString() {
            return FileName;
        }
    }
> }
> ```

To access a full file path, additionally implement the @DevExpress.Persistent.Base.ISupportFullName interface in your class (works only in WinForms).

File Data Property Editor (Blazor, WinForms)
:   Enable the [File Attachments](xref:112781) module to display objects that implement the `IFileData` interface in the File Data Property Editor.
PDF Viewer Property Editor (Blazor, WinForms)
:   Enable the [Office Module](xref:400003) and assign `PdfViewerPropertyEditor` to a file data property to display PDF files in the PDF Viewer.  
    Refer to the following topic for additional details: <xref:405488>.

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
    private FileData file;
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