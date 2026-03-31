---
uid: '400004'
title: Use Rich Text Documents in Business Objects
seealso:
  - linkId: '400063'
---
# Use Rich Text Documents in Business Objects

This topic describes how to use the **DevExpress.ExpressApp.Office.Win.RichTextPropertyEditor** and **DevExpress.ExpressApp.Office.Blazor.Editors.RichTextPropertyEditor** for byte array and string properties in WinForms and for ASP.NET Core Blazor applications. The following images demonstrate these Property Editors assigned to the `Document.Text` property: 

Windows Forms
:   ![The RichTextPropertyEditor in a WinForms application](~/images/richedit.png)
ASP.NET Core Blazor
:   ![The RichTextPropertyEditor in an ASP.NET Core Blazor application](~/images/richedit_blazor.png)

## Assign the Rich Text Property Editor to a Business Class' Property 

### In Code
To enable the Rich Text Property Editors for a business class' property, apply the @DevExpress.Persistent.Base.EditorAliasAttribute to this property as follows:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
// Byte array property example:
[EditorAlias(EditorAliases.RichTextPropertyEditor)] 
public virtual byte[] Text { get; set; }

// String property example:
[FieldSize(FieldSizeAttribute.Unlimited)]
[EditorAlias(EditorAliases.RichTextPropertyEditor)] 
public virtual string Text { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
// Byte array property example:
private byte[] text;
[EditorAlias(EditorAliases.RichTextPropertyEditor)] 
public byte[] Text { 
    get { return text; }
    set { SetPropertyValue(nameof(Text), ref text, value); }
}

// String property example:
private string text;
[Size(SizeAttribute.Unlimited)]
[EditorAlias(EditorAliases.RichTextPropertyEditor)] 
public string Text { 
    get { return text; }
    set { SetPropertyValue(nameof(Text), ref text, value); }
}
```

***

### In the Model Editor

Open Model Differences in the [platform-specific](xref:118045) project. Navigate to the required [!include[](~/templates/node_views_detailview_items_propertyeditor111384.md)] node and set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType property to **DevExpress.ExpressApp.Office.Win.RichTextPropertyEditor** or **DevExpress.ExpressApp.Office.Blazor.Editors.RichTextPropertyEditor**.

![Rich Text Property Editor in Model Editor](~/images/richedit-propertyeditortype.png)

## Document Storage Formats
In ASP.NET Core Blazor applications, your application saves the documents in the [DOCX](https://en.wikipedia.org/wiki/Office_Open_XML) format when you use the Rich Text Property Editors for a byte array property. The RTF format is used for string properties. Alternatively, you can [change the format to HTML](xref:400063#change-the-document-storage-format). We recommend using byte arrays instead of strings to store your documents because the DOCX format works faster with large documents and supports more formatting options.

## Edit the Document in a Separate Window

In WinForms applications, you can open the document in a new modal window using the **Show in popup** context menu command.

![Show in popup context menu command](~/images/richedit-showinpopup.png)

![Document in a Separate Window](~/images/richedit-documentpreview.png)
