---
uid: "113097"
seealso:
- linkId: "113014"
title: Property Editors
---
# Property Editors

Detail Views use Property Editors to display object data. Each Property Editor is bound to a property in the associated object/entity.

![|XAF ASP.NET Core Blazor Property Editors in a Detail View, DevExpress](~/images/property-editors-detail-view.png)

> [!TIP]
> To display static information or an unbound control, implement a View Item instead of a Property Editor. For more information, refer to the following topic: [Add an Unbound Control (Button) to the Form Layout in an XAF View](xref:405483).

Property Editors create UI controls based on [Application Model](xref:112579) settings. To customize a Property Editor in a specific Detail View before XAF creates the control, use the [PropertyEditor](xref:DevExpress.ExpressApp.Editors.PropertyEditor) object and its descendants. After XAF creates and initializes the control, customize the underlying platform control settings. For more information on how to access Property Editor settings, refer to the following help topic: [Get the View Item or Property Editor Object](xref:120092#get-the-viewitem-or-property-editor-object).

XAF includes built-in Property Editors that address most data management scenarios. For more information about built-in Property Editors, refer to the following help topic: [Data Types Supported by Built-in Editors](xref:113014).

## Custom Property Editors

If built-in Property Editors do not meet your requirements, you can implement a custom Property Editor. This section explains common reasons to create a custom editor and outlines basic implementation steps.

Customize a built-in Property Editor's control functionality
:   Built-in XAF Property Editors use controls supplied by [DevExperss WinForms Editors](xref:401381) and [DevExpress Blazor Editors](xref:401156). You can customize these controls by accessing the Property Editor and changing its settings. If you want to reuse the same customization across views, implement a custom Property Editor that inherits from a built-in editor. For more information about accessing Property Editor settings, refer to the following help topic: [Access the Settings of a Property Editor in a Detail View](xref:402153).

Use third-party controls
:   If you want to use a third-party control for data editing, implement a custom Property Editor.

Support management of custom data types
:   If a business class has a property of a custom type, implement a custom Property Editor to display and edit this value.

Advanced data management scenarios
:   Implement a custom Property Editor when you need to read and write values from a custom data source.

### Implement Custom Property Editor

To implement a custom Property Editor, inherit from the [PropertyEditor](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class or one of its descendants.

![PropertyEditorsDiagram](~/images/property-editors-diagram.png)

Use the following table to choose a base class for your Property Editor:

| Base class | Description | When to Use |
|---|---|---|
| [PropertyEditor](xref:DevExpress.ExpressApp.Editors.PropertyEditor) | Implements platform-independent Property Editor features. | Inherit from this class if you need to develop Property Editors for a platform that is not supported internally by XAF. In other cases, use one of the following classes. |
| [BlazorPropertyEditorBase](xref:DevExpress.ExpressApp.Blazor.Editors.BlazorPropertyEditorBase),<br/>[WinPropertyEditor](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor) | Base classes for Property Editors that create and configure a custom control. | Inherit from `BlazorPropertyEditorBase` to implement a Blazor Property Editor that uses a custom component. Inherit from `WinPropertyEditor` to implement a WinForms Property Editor that uses a custom control. Override `CreateControlCore` to create the control. In ASP.NET Core Blazor, you can also override `BlazorPropertyEditorBase.CreateViewComponentCore(System.Object)` to customize how the editor renders in a List View. |
| [DXPropertyEditor](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) | Base class for WinForms Property Editors that use `XtraEditors` controls and `XtraGrid` repository items. | Inherit from `DXPropertyEditor` when you build a WinForms Property Editor based on `XtraEditors` and you need consistent behavior in both Detail Views and List Views. Override `CreateControlCore` to create the editor control for a Detail View and `CreateRepositoryItem`/`SetupRepositoryItem` to configure the repository item for a grid column. |
| `BooleanPropertyEditor`, `StringPropertyEditor`, and others | Type-specific base classes for common data types. These classes extend platform-specific base classes such as [DXPropertyEditor](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) (WinForms) and [BlazorPropertyEditorBase](xref:DevExpress.ExpressApp.Blazor.Editors.BlazorPropertyEditorBase) (ASP.NET Core Blazor). | Inherit from a type-specific editor when you need to customize how XAF displays or edits a specific data type (for example, string or Boolean). |

### Register Custom Property Editor

XAF loads custom Property Editors into the [Application Model](xref:112579) so you can use them in the UI.

Implement the editor in a platform-specific [project](xref:118046) (_SolutionName.Blazor.Server_ or _SolutionName.Win_) and apply the [PropertyEditorAttribute](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute). If your solution does not have a platform-specific project, implement the editor in an [application project](xref:118045) (_SolutionName.Model_).

For more information, refer to the following help topic: [PropertyEditorAttribute](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute).

## Replace Standard Property Editors with a Custom Control

To display an object in a [Detail View](xref:112611) with a specific control instead of a set of standard Property Editors, follow these steps:
1. Create a custom Property Editor based on the required control and add a non-persistent (not mapped) property to the target business class that returns the current object's instance.
2. To hide this property in List Views, apply the [VisibleInListViewAttribute](xref:DevExpress.Persistent.Base.VisibleInListViewAttribute).
3. Assign your custom Property Editor to the new property (make it the default editor for the property's data type or set the property's [PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) in the Application Model).
4. [Customize the Detail View layout](xref:112817) to hide all Property Editors except your custom Property Editor.

    **File:** _SolutionName.Module/BusinessObjects/MyBusinessClass.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace SolutionName.Module.BusinessObjects {
        public class MyBusinessClass : BaseObject {
            [NotMapped]
            [VisibleInListView(false)]
            public virtual MyBusinessClass Self => this;
        }
    }
    ```
    ***

    As a result, List Views display a set of properties and Detail Views display the custom control.

## Custom Property Editor Tutorials

* [How to: Customize a Built-in Property Editor (ASP.NET Core Blazor)](xref:402188)
* [How to: Customize a Built-in Property Editor (WinForms)](xref:113104)
* [How to: Implement a Property Editor Based on a Custom Control (ASP.NET Core Blazor)](xref:402189)
* [How to: Implement a Property Editor Based on a Custom Control (WinForms)](xref:112679)
* [Supply Predefined Values for the String Property Editor Dynamically](xref:404599)

[!include[custom-property-editor-popular-scenarios](~/templates/custom-property-editor-popular-scenarios.md)]
