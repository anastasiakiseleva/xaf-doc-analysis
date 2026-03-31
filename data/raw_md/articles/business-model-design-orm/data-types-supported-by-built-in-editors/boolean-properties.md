---
uid: "113540"
seealso:
- linkId: "402188"
title: Boolean Properties
---
# Boolean Properties

In XAF, the following controls can display Boolean and Nullable Boolean properties:

* A checkbox control (default).
* A drop-down control that displays Boolean values as custom text strings. You can use the [IModelCommonMemberViewItem.CaptionForTrue](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForTrue) and [IModelCommonMemberViewItem.CaptionForFalse](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForFalse) properties to specify these strings in the Application Model.
* A drop-down control can display Boolean values as custom text strings accompanied by images. You can define these strings in the same manner as for a drop-down control. Use the [IModelCommonMemberViewItem.ImageForTrue](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForTrue) and [IModelCommonMemberViewItem.ImageForFalse](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForFalse) properties to assign images for the `true` and `false` values.

Refer to the following topics for more ORM-specific information on Boolean properties:

* [Boolean Properties in XPO](xref:113541)
* [Boolean Properties in EF Core](xref:113542)

## ASP.NET Core Blazor

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

![|XAF Boolean Property ASP.NET Core Blazor, DevExpress|](~/images/blazor-boolean-property.png)

![|XAF Boolean Property With Captions ASP.NET Core Blazor, DevExpress|](~/images/blazor-boolean-property-with-captions.png)

![|XAF Boolean Property With Images ASP.NET Core Blazor, DevExpress|](~/images/blazor-boolean-property-with-images.png)


The following table shows available Component Models for `BooleanPropertyEditor`:

{|
|-
! IComponentContentHolder descendant
! Component
! Description
|-
| `DevExpress.ExpressApp.Blazor.Components.Models.DxCheckBoxModel<T>`
| @DevExpress.Blazor.DxCheckBox`1
| The default control.
|-
| `DevExpress.ExpressApp.Blazor.Components.Models.DxComboBoxModel<TData, TValue>`
| @DevExpress.Blazor.DxComboBox`2
| This component is used when one of the following property pairs is specified:
* @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForFalse and @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForTrue
* @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForFalse and @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForTrue
|}

## WinForms

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

![|XAF Boolean Properties WinForms|](~/images/pe_boolwin117308.png)

The following table shows available controls and repository items for `BooleanPropertyEditor`:

{|
|-
! Control
! Repository item
! Description
|-
| BooleanEdit (a @DevExpress.XtraEditors.CheckEdit descendant). 
| RepositoryItemBooleanEdit (a @DevExpress.XtraEditors.Repository.RepositoryItemCheckEdit descendant).
| A CheckEdit control (default).
|-
| BoolComboBoxEdit (an @DevExpress.XtraEditors.ImageComboBoxEdit descendant).
| RepositoryItemBoolComboBoxEdit (a @DevExpress.XtraEditors.Repository.RepositoryItemImageComboBox descendant).
| A drop-down control with custom text. An optional image is displayed next to the text when one of the following property pairs is specified: 
* @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForFalse and @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForTrue
* @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForFalse and @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForTrue
|}
