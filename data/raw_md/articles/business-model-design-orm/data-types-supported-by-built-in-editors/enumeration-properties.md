---
uid: "113552"
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-display-an-enumeration-property-as-a-drop-down-box-with-check-boxes
  altText: XAF - How to Display an Enumeration Property as a Drop-down Box with Check Boxes
- linkId: "402188"
title: Enumeration Properties
owner: Ekaterina Kiseleva
---
# Enumeration Properties

In XAF, a combo box with text entries displays enumeration properties. The [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor) class gets images and localized item captions for the Property Editor. Refer to the following topic for implementation details: [How to: Set Images and Captions for Enumeration Values](xref:112825).

Refer to the following topics for more information on enumeration properties related to your ORM:

* [Enumeration Properties in XPO](xref:113553)
* [Enumeration Properties in EF Core](xref:113554)

## ASP.NET Core Blazor

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

![|XAF Enumeration Property ASP.NET Core Blazor, DevExpress|](~/images/blazor-enum-combobox.png)

![|XAF Enumeration Property with Image ASP.NET Core Blazor, DevExpress|](~/images/blazor-enum-property-with-image-devexpress.png)

{|
|-
! Property Editor
! Component Model
! Component
|-
| `EnumPropertyEditor`
| `DevExpress.ExpressApp.Blazor.Components.Models.DxComboBoxModel<TData, TValue>`
| @DevExpress.Blazor.DxComboBox`2
|}

## Windows Forms

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

![|XAF Enumeration Properties Windows Forms, DevExpress|](~/images/pe_enumwin117315.png)

{|
|-
! Property Editor
! Control
! Repository Item
! Description
|-
| `EnumPropertyEditor` 
| `EnumEdit` (an [ImageComboBoxEdit](xref:DevExpress.XtraEditors.ImageComboBoxEdit) descendant).
| `RepositoryItemEnumEdit` (a [RepositoryItemButtonEdit](xref:DevExpress.XtraEditors.Repository.RepositoryItemButtonEdit) descendant).
| Used for enumeration type properties. Press Alt + Down Arrow to expand the `EnumEdit` drop-down window. In this window, you can see items that consist of a caption and an image.
|-
| `EnumIntPropertyEditor<TEnum>`
| `EnumIntEdit` (an [ImageComboBoxEdit](xref:DevExpress.XtraEditors.ImageComboBoxEdit) descendant).
| `RepositoryItemEnumIntEdit` (a [RepositoryItemImageComboBox](xref:DevExpress.XtraEditors.Repository.RepositoryItemImageComboBox) descendant).
| Used to display integer properties as enumerations. Refer to the following topic for more information: [How to: Display an Integer Property as an Enumeration](xref:113563).
|}
