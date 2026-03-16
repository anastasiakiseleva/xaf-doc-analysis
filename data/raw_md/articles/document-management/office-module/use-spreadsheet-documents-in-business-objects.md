---
uid: '400931'
title: Use Spreadsheet Documents in Business Objects
owner: Yekaterina Kiseleva
seealso:
  - linkId: '400894'
  - linkId: '401211'
---
# Use Spreadsheet Documents in Business Objects

[!include[blazor-does-not-support-spreadsheet](~/templates/blazor-does-not-support-spreadsheet.md)]

This topic describes how to use the **SpreadsheetPropertyEditor** to display byte array properties in WinForms applications. The following images demonstrate these Property Editors assigned to the **Document.Data** property: 

![The SpreadsheetPropertyEditor in a WinForms application](~/images/spreadsheet.png)

## Assign the Spreadsheet Property Editor to a Business Class' Property

### In Code
Decorate a business class' property with the @DevExpress.Persistent.Base.EditorAliasAttribute and pass the @DevExpress.ExpressApp.Editors.EditorAliases.SpreadsheetPropertyEditor value as the attribute's parameter:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[EditorAlias(EditorAliases.SpreadsheetPropertyEditor)] 
public virtual byte[] Data { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
private byte[] data;
[EditorAlias(EditorAliases.SpreadsheetPropertyEditor)] 
public byte[] Data { 
    get { return data; }
    set { SetPropertyValue(nameof(Data), ref data, value); }
}
```
***

### In the Model Editor
Navigate to the [!include[](~/templates/node_views_detailview_items_propertyeditor111384.md)] node and set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType property to **DevExpress.ExpressApp.Office.Win.SpreadsheetPropertyEditor**.

![Spreadsheet Property Editor in Model Editor](~/images/spreadsheet-propertyeditortype.png)

## Edit the Document in a Separate Window

Use the **Show in popup** context menu command to open the document in a new modal window.

![Show in popup context menu command](~/images/spreadsheet-showinpopup.png)

![Document in a Separate Window](~/images/spreadsheet-documentpreview.png)
