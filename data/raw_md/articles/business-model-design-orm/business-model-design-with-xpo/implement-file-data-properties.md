---
uid: "112658"
seealso:
- linkId: "112781"
- linkId: DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)
- linkId: DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)
title: 'Implement File Data Properties'
---
# Implement File Data Properties

This topic demonstrates how to implement a business class with a file data property and a file collection property. For this purpose, the **Resume** class, which is used to store and manage an employee's resume information, is implemented. It has three properties: **File**, **Contact** and **Portfolio**. The **File** property provides a file, the **Contact** property contains a reference to the **Contact** class, and the **Portfolio** property returns a collection of the employee's files.

To add a file data type property and a file collection property to a business object, you should use a type that implements the **IFileData** interface and one that applies the **FileAttachment** attribute. In this instance, the **FileAttachmentsWindowsFormsModule**, **FileAttachmentsAspNetModule**, or **FileAttachmentsBlazorModule** modules should be added to your WinForms, ASP.NET Web, or ASP.NET Core Blazor module projects respectively. If your solution does not contain these projects, add it to [application projects](xref:118045). These modules contain [Property Editors](xref:112612) for **IFileData** type properties, and [Controllers](xref:112621) with [Actions](xref:112622) that are necessary for file manipulation. For details, refer to the [File Attachments Module Overview](xref:112781) topic.

To add the **FileAttachmentsWindowsFormsModule**  or **FileAttachmentsBlazorModule** module to an existing application, install the **DevExpress.ExpressApp.FileAttachment.Win** or **DevExpress.ExpressApp.FileAttachment.Blazor** NuGet package to the WinForms or ASP.NET Core Blazor [application project](xref:118045). Add the File Attachment Module to the platform-specific module's **RequiredModuleTypes** collection. Rebuild the solution. For more information, refer to the [Reuse Implemented Functionality](xref:401955) topic.

> [!Tip]
> [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsOptions})>,<ASP.NET Core Blazor/WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

The following code demonstrates a **Resume** business object.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Resume : BaseObject {
   public Resume(Session session) : base(session) {}
   private FileData file;
   [Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
   public FileData File {
      get { return file; }
      set {
         SetPropertyValue(nameof(File), ref file, value);
      }
   }
  [Aggregated, Association("Resume-PortfolioFileData")]
  public XPCollection<PortfolioFileData> Portfolio {
     get { return GetCollection<PortfolioFileData>(nameof(Portfolio)); }
  }
}
public class PortfolioFileData : FileAttachmentBase {
   public PortfolioFileData(Session session) : base(session) {}
   private DocumentType documentType;
   protected Resume resume;
   [Persistent, Association("Resume-PortfolioFileData")]
   public Resume Resume {
      get { return resume; }
      set { 
         SetPropertyValue(nameof(Resume), ref resume, value); 
      }
   }
   public override void AfterConstruction() {
      base.AfterConstruction();
      documentType = DocumentType.Unknown;
   }
   public DocumentType DocumentType {
      get { return documentType; }
      set { SetPropertyValue(nameof(DocumentType), ref documentType, value);}
   }
}
public enum DocumentType { SourceCode = 1, Tests = 2, Documentation = 3, 
   Diagrams = 4, ScreenShots = 5, Unknown = 6 };
```
***

To create a collection of an employee's files, the **Resume** class has the **Portfolio** property of the `XPCollection<PortfolioFileData>` type. The **PortfolioFileData** class is inherited from the **FileAttachmentBase** class, which in turn, uses the **FileAttachment** interface. The **FileAttachmentBase** class and the **FileAttachment** attribute are the parts of the **Business Objects Library**.

The **PortfolioFileData** class has the **DocumentType** property that specifies the portfolio file type. This property is initialized in the **AfterConstruction** method override. The **PortfolioFileData** class also stores a reference to a **Resume** object in its **Resume** property.

The following images show the **Resume** [Detail View](xref:112611) in WinForms, ASP.NET Web, and ASP.NET Core Blazor applications.

**WinForms**  
![ResumeInWin](~/images/resumeinwin115388.png)

**Blazor**  
![ResumeInBlazor](~/images/ResumeInBlazor.png)