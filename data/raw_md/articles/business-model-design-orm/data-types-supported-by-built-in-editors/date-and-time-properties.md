---
uid: "113536"
seealso:
- linkId: "113097"
- linkId: "402188"
title: Date and Time Properties
owner: Anastasiya Kisialeva
---
# Date and Time Properties

XAF supports Property Editors for the following types and their nullable variants on all platforms: 
* `DateTime`
* `DateOnly`
* `TimeSpan`
* `TimeOnly`

Refer to the following topics for information on how to add Date and Time properties to business classes in the supported ORM systems:

* [Date and Time Properties in XPO](xref:113537)
* [Date and Time Properties in EF Core](xref:113538)

## ASP.NET Core Blazor

![|Blazor Date Time property editors|](~/images/pe_datetimeblazor.png)

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

### DateTimePropertyEditor
	
Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxDateEditModel<T>`.
	
Component: DevExpress ASP.NET Core Blazor Library's [DxDateEdit\<T\>](xref:DevExpress.Blazor.DxDateEdit`1) editor.
	
Description:
	
This is the default Property Editor for `DateTime` and `DateOnly` (EF Core) properties. Access the `DxDateEditMaskProperties` property to modify the Component mask properties.

### TimeSpanPropertyEditor
	
Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxTimeEditModel<T>`.
	
Component: DevExpress ASP.NET Core Blazor Library's [DxTimeEdit\<T\>](xref:DevExpress.Blazor.DxTimeEdit`1) editor.
	
Description:
	
This is the default Property Editor for `TimeSpan` and `TimeOnly` (EF Core) properties. Access the `DxTimeEditMaskProperties` property to modify the Component's mask properties.

## Windows Forms

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

![WinForms Date Time property editors](~/images/pe_datetimewin117306.png)

### DatePropertyEditor

Control: `DateTimeEdit` (a @DevExpress.XtraEditors.DateEdit descendant).

Repository Item: `RepositoryItemDateTimeEdit` (a @DevExpress.XtraEditors.Repository.RepositoryItemDateEdit descendant).

Description

This Property Editor is used for `DateTime` properties and applies the [DateTime](xref:1497) mask type to store and display values. To set the mask, specify one of the following:

* The Property Editor's `EditMask` property in code
* The [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node's [IModelCommonMemberViewItem.EditMask](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask) property in the Model Editor

Do one of the following to invoke a drop-down calendar:

* Press Alt + Down Arrow
* Click the editor's arrow
* Double-click the editor

In the invoked calendar, you can select any date or the current date (at the top of the calendar). Click **Clear** to set the editor value to `null`.
	
You can perform date operations without the drop-down calendar. For example, press the Space key to enter a date from the keyboard. To clear the editor value, press Ctrl+0 or Ctrl+Delete.

### TimeSpanPropertyEditor

Control: `TimeSpanEdit` (a @DevExpress.XtraEditors.TextEdit descendant).

Repository Item: `RepositoryItemTimeSpanEdit` (a @DevExpress.XtraEditors.Repository.RepositoryItemTextEdit descendant).

Description

The default value of this Property Editor's `EditMaskType` property is `RegEx`. This way you can use [extended regular expressions](xref:1501) to specify the `EditMask` (in code or in the Model Editor). To switch the mask type, change the `EditMaskType` property value. Then, use a View Controller to access the corresponding `TimeSpanPropertyEditor` instance and specify a mask for it. For more information, refer to the following topic: [](xref:402153).
