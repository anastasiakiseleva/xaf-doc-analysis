---
uid: "113544"
seealso:
- linkId: "402188"
title: BLOB Image Properties
owner: Ekaterina Kiseleva
---
# BLOB Image Properties

In XAF, BLOB image properties are persisted as byte arrays which can be displayed in the following controls:

* A `PictureEdit` control (default)
* A drop-down control (for WinForms applications only)

> [!NOTE]
> **BLOB**, or **Binary Large Object**, is a set of binary data persisted as a single entity in the database.

The [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) specifies Image Property Editor settings when displaying images.
 
> [!NOTE]
> Refer to the **Property Editors** | **Image Properties** section in the **Feature Center** demo installed with XAF to see Image Property Editors in action. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)] You can also watch the [Image Property Editor](https://www.youtube.com/watch?v=F8EdNZ14tuE) tutorial video at the DevExpress YouTube channel.

## Examples
* [BLOB Image Properties in XPO](xref:113545)
* [BLOB Image Properties in EF Core](xref:113546)

## ASP.NET Core Blazor

![|XAF BLOB Image Properties ASP.NET Core Blazor](~/images/xaf-blazor-blob-image-property.png)

### ImagePropertyEditor

Used as the default editor for properties of the following types:
* Byte array properties decorated by the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute)
* [Reference properties](xref:113572) of the [](xref:DevExpress.Persistent.BaseImpl.MediaDataObject) and [](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject) types

**ImagePropertyEditor** uses a custom `ImageEditComponent` class to implement the editor's functionality. 

In Detail Views, the editor displays a placeholder icon if the bound property is empty. A user can click the icon to upload a new image. An ellipsis button over the image provides access to Replace and Remove buttons.

On mobile devices and in List View [Inline Edit mode](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.InlineEditMode), the editor does not show its ellipsis button. To access Replace and Remove buttons, a user can click or tap the editor. On mobile devices, these commands appear in a pop-up menu. To close the menu, use the Cancel button or tap the pop-up background.

To access Context Menu and mobile pop-up menu instances, use `ComponentModel.ContextMenu` and `ComponentModel.PopupMenu` respectively.

For additional customization, implement your own custom property editor as described in the following topic: [](xref:402189).

## WinForms

![XAF BLOB Image Properties WinForms](~/images/pe_imagewin117310.png)

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### ImagePropertyEditor

Control: The [](xref:DevExpress.XtraEditors.PictureEdit) or [](xref:DevExpress.XtraEditors.ImageEdit) editor from the XtraEditors Library.

Repository Item: [](xref:DevExpress.XtraEditors.Repository.RepositoryItemPictureEdit) or [](xref:DevExpress.XtraEditors.Repository.RepositoryItemImageEdit) repository item from the XtraEditors Library.

Description:

Used for byte array properties decorated by the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) and for [reference properties](xref:113572) of the [](xref:DevExpress.Persistent.BaseImpl.MediaDataObject) and [](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject) types.

The default configuration is **PictureEdit** and **RepositoryItemImageEdit**.

Both **PictureEdit** and **ImageEdit** editors allow end users to perform Load, Save, Delete, Cut, Copy, and Paste operations using a context menu.

Use [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) to configure the **ImagePropertyEditor** for a particular business class property.
