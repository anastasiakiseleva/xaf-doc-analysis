---
uid: '400006'
title: Mail Merge
owner: Ekaterina Kiseleva
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t680332/winforms-how-to-hide-a-mail-merge-template-from-the-showindocument-action
  altText: How to hide a mail merge template from the ShowInDocument Action
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/12/20/javascript-consume-the-devexpress-backend-web-api-with-svelte-part-7-mail-merge.aspx
  altText: JavaScript — Consume the DevExpress Backend Web API with Svelte (Part 7. Mail Merge)
---
# Mail Merge

This topic describes how to enable and use the [Mail Merge](xref:9330) feature in ASP.NET Core Blazor or Windows Forms applications.

To enable Mail Merge, set the @DevExpress.ExpressApp.Office.OfficeModule.RichTextMailMergeDataType property to the type you use for storing document templates.

Specify the type as one of office module options.

**File**: _YourSolutionName.Blazor.Server/Startup.cs_ or _YourSolutionName.Win/Startup.cs_.

# [ASP.NET Core Blazor](#tab/tabid-blazor)

[!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Blazor_example.md)]

# [Windows Forms](#tab/tabid-winforms)

[!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Win_example.md)]
---

## In Applications Without Application Builder

Specify the type when you add the office module:

**File**: _MyApplication.Blazor.Server/MyApplication.Designer.cs_ or _MyApplication.Win/MyApplication.Designer.cs_.

```csharp{7}
using Devexpress.Persistent.BaseImpl.EF
// ...
partial class MyApplication {
    private void InitializeComponent() {
        // ...
        this.officeModule = new DevExpress.ExpressApp.Office.OfficeModule();
        this.officeModule.RichTextMailMergeDataType = typeof(RichTextMailMergeData);
        // ...
    }
    // ...
}
```

## Data Types

You can use one of the following built-in types, depending on your ORM:

| ORM                   | Business Object Type                                        |
|:----------------------|:------------------------------------------------------------|
| XPO                   | `DevExpress.Persistent.BaseImpl.RichTextMailMergeData`      |
| Entity Framework Core | `DevExpress.Persistent.BaseImpl.EF.RichTextMailMergeData`   |

> [!IMPORTANT]
> If you use Entity Framework (Core), register the `DevExpress.Persistent.BaseImpl.EF.RichTextMailMergeData` type in the `DbContext` (see [Ways to Add a Business Class - Import Classes from a Business Class Library or Module](xref:112847#import-classes-from-a-business-class-library-or-module)).

## Mail Merge Template

Run the application and invoke the **Reports** | **Mail Merge Template** navigation item to create new and access existing document templates.

ASP.NET Core Blazor
:   ![|ASP.NET Core Blazor document template|](~/images/richedit-mailmerge_blazor.png)
Windows Forms
:   ![Windows Forms document template](~/images/richedit-mailmerge.png)

Use the **Data Type** field to specify the business class to be used as the document's data source.

In the drop-down **Insert Merge Field** window (Windows Forms) or pop-up **Insert Merge Field** window (ASP.NET Core Blazor), select fields from the data type to add to the document template.

> [!Tip] 
> If the **Data Type** field does not list the class, use one of the fixes below: 
> * Apply the [VisibleInReportsAttribute](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) (with the parameter set to `true`) or [DefaultClassOptionsAttribute](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) to the class.
> * Set the [IModelClassReportsVisibility.IsVisibleInReports](xref:DevExpress.ExpressApp.Model.IModelClassReportsVisibility.IsVisibleInReports) property of the corresponding **BOModel** | **_\<Class\>_** node to `true`.

### Subfields in Mail Merge Design Time and Preview

Subfields allow you to reference nested properties in mail merge templates (for example, `ObjectProperty.SubProperty`).

#### How to Add Subfields

Subfields are not available in the **Insert Merge Field** drop-down or pop-up window. To add a subfield:

1. Click **Show All Field Codes** in the template editor.
2. Type the field using the `{ MERGEFIELD ObjectProperty.SubProperty }` notation.

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor Show All Field Codes button in the mail merge template editor](~/images/richedit-mailmerge-subfields_blazor.png)
Windows Forms
:   ![XAF Windows Forms Show All Field Codes button in the mail merge template editor](~/images/richedit-mailmerge-subfields.png)

#### Subfields Behavior in Preview

**Windows Forms**: Subfields display correctly in preview mode when you click **View Merged Data**.

**ASP.NET Core Blazor**: Subfields do not display in preview mode when you click **View Merged Data**. The ASP.NET Core Blazor @DevExpress.Blazor.RichEdit.DxRichEdit component does not support subfield preview.

Both platforms generate the final merged document and display subfields correctly when you use the **Show In document** Action described in the [View Mail Merge Results](#view-mail-merge-results) section of this topic.

## View Mail Merge Results

To view the records merged with the specified document template, select the required business objects in a List View (or open a single object's Detail View) and click **Show in document**.
The **ShowInDocument** Action lets you view the records merged with the specified mail merge template directly from ListView.

ASP.NET Core Blazor
:   ![|Show in document in an ASP.NET Core Blazor application](~/images/richedit-showindocument_blazor.png)
Windows Forms
:   ![|Show in document in a Windows Forms application](~/images/richedit-showindocument-winforms.png)

> [!Note]
> The **ShowInDocument** Action uses the in-place documents cache to generate and store the Action's items. Note that this cache is not updated automatically. Refer to the [](xref:DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase) class description for information on how to update this cache.
