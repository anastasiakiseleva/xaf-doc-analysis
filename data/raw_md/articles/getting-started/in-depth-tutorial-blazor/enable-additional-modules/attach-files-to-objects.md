---
uid: "403288"
title: 'Attach Files to Objects'
---
# Attach Files to Objects

This lesson describes how to attach file collections to objects.

In this lesson you will do the following:

- Add the [File Attachment](xref:112781) Module to the application.
- Implement new entity classes: `Resume` to store a Contact's resume information and `PortfolioFileData` to save file data collection items.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:402984)
> * [](xref:402980)

## Step-by-Step Instructions
 
1. Add the **DevExpress.ExpressApp.FileAttachment.Blazor** NuGet package to the _MySolution.Blazor.Server_ project and the **DevExpress.ExpressApp.FileAttachment.Win** NuGet package to the _MySolution.Win_ project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042). 

2. In the _MySolution.Blazor.Server_ project, open the _Startup.cs_ file and add the File Attachment module to the application builder. Do the same in the _Startup.cs_ file of the _MySolution.Win_ project:

   # [C# (ASP.NET Core Blazor)](#tab/tabid-csharp-blazor)
 
   ```csharp{9}
   public class Startup {
   // ...
       public void ConfigureServices(IServiceCollection services) {
           // ...
           services.AddXaf(Configuration, builder => {
               builder.UseApplication<MySolutionBlazorApplication>();
               builder.Modules
                    // ...
                   .AddFileAttachments();
               // ...
           });
           // ...
       }
   }
   ```

   # [C# (Windows Forms)](#tab/tabid-csharp-xpo)

   ```csharp{7}
   public class ApplicationBuilder : IDesignTimeApplicationFactory {
       public static WinApplication BuildApplication(string connectionString) {
       var builder = WinApplication.CreateBuilder();
       builder.UseApplication<MySolutionWindowsFormsApplication>();
       builder.Modules
       //...
            .AddFileAttachments();

       }
   }
   ```

   ***

   If you add the [File Attachment](xref:112781) Module when you create an XAF application, the [Template Kit](xref:405447) generates the code that adds the File Attachment Module automatically.

3. In the _MySolution.Module\Business Objects_ folder, create the `Resume` class. Replace the generated class declaration with the following code:

   ```csharp
   using DevExpress.ExpressApp.DC;
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl.EF;
   using System.Collections.ObjectModel;

   namespace MySolution.Module.BusinessObjects {
       [DefaultClassOptions]
       [ImageName("BO_Resume")]
       public class Resume : BaseObject {

           [Aggregated]
           public virtual IList<PortfolioFileData> Portfolio { get; set; } = new ObservableCollection<PortfolioFileData>();

           public virtual Employee Employee { get; set; }

           [Aggregated]
           public virtual FileData File { get; set; }
       }
   }
   ```

5. Add the `Resume` property to the `Employee` class:

   ```csharp{9}
   using System.ComponentModel.DataAnnotations.Schema;

   namespace MySolution.Module.BusinessObjects {
       [DefaultClassOptions]
       [ObjectCaptionFormat("{0:FullName}")]
       [DefaultProperty(nameof(FullName))]
       public class Employee : BaseObject {
           // ...
           public virtual IList<Resume> Resumes { get; set; } = new ObservableCollection<Resume>();
       }
       // ...
   }
   ```

6. Create the `PortfolioFileData` class. Replace the generated class declaration with the following code:

   ```csharp
   using DevExpress.ExpressApp.Model;
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl.EF;
   using DevExpress.Persistent.Validation;

   namespace MySolution.Module.BusinessObjects {
       [DefaultClassOptions]
       [ImageName("BO_FileAttachment")]
       public class PortfolioFileData : BaseObject {

           [RuleRequiredField("PortfolioFileDataRule", "Save", "File should be assigned")]
           public virtual FileData File { get; set; }

           public virtual Resume Resume { get; set; }

           public virtual DocumentType DocumentType { get; set; }

           public override void OnCreated() {
               DocumentType = DocumentType.Unknown;
           }
       }
       public enum DocumentType {
           SourceCode = 1,
           Tests = 2,
           Documentation = 3,
           Diagrams = 4,
           Screenshots = 5,
           Unknown = 6
       }
   }
   ```

7. Add the [Required](xref:System.ComponentModel.DataAnnotations.RequiredAttribute) attribute to the `Resume` property in the `PortfolioFileData` class.

   ```csharp{8}
   // ...
   namespace MySolution.Module.BusinessObjects;

   [DefaultClassOptions]
   [ImageName("BO_FileAttachment")]
   public class PortfolioFileData : BaseObject {   
       //...
       [Required]
       public virtual Resume Resume { get; set; }
       //...
   }
   ```

   The `Resume` and `PortfolioFileData` entities are connected with a One-to-Many relationship. For more information on how to create such relationships between entities, refer to the following lesson: [](xref:402984).

   In the EF Core-based application, a deletion of a master object does not delete the related objects. In this lesson, we use the [Required](xref:System.ComponentModel.DataAnnotations.RequiredAttribute) attribute to configure the associations between classes. This way you can delete the referenced objects with the master object and avoid integrity violation.

   Alternatively, you can use the [Fluent API](https://learn.microsoft.com/en-us/ef/core/modeling/#use-fluent-api-to-configure-a-model) and specify the [OnDelete](xref:Microsoft.EntityFrameworkCore.Metadata.Builders.ReferenceCollectionBuilder.OnDelete*) method for the `Portfolio`-`Resume` relationship as described in the following topic: [The Fluent API OnDelete Method](https://www.learnentityframeworkcore.com/configuration/fluent-api/ondelete-method).

8. Open the _MySolution.Module.BusinessObjects\MySolutionDbContext.cs_ file and add the properties of `Resume` and `PortfolioFileData` types to `DbContext`:

   ```csharp
   public class MySolutionEFCoreDbContext : DbContext {
       //...
       public DbSet<Resume> Resumes { get; set; }
	   public DbSet<PortfolioFileData> FileAttachments { get; set; }
   }
   ```

9. Run the application. Open the **Resume** List View and create a new **Resume** object. Fill the **Employee** field and add a new **Portfolio File Data** object. In the **Portfolio File Data** window, select the file that you wish to attach.

    **ASP.NET Core Blazor**

    ![|ASP.NET Core Blazor Add a Resume object|](~/images/blazor-tutorial-file-attachment-add-file.gif)

    **Windows Forms**

    ![|Windows Forms Add a Resume object|](~/images/blazor-tutorial-file-attachment-add-file-winforms.gif)

Users can click the file link to download the resume file.
    
To get a file stored within a `PortfolioFileData` object in code, use the [](xref:DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)) method of its `File` property.

## Next Lesson

[](xref:404206)
