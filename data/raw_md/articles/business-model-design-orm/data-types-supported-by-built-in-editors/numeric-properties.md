---
uid: "113532"
seealso:
- linkId: "402188"
title: Numeric Properties
owner: Ekaterina Kiseleva
---
# Numeric Properties

XAF supports Property Editors for numeric data types (`byte`, `int`, `decimal`, `long`, corresponding nullable types and so on) on all platforms. However, WinForms and ASP.NET Core Blazor UI applications use different formatting rules depending on the underlying property type.

Refer to the following topics for information on how to add Numeric properties to business classes in the supported ORM systems:

* [Numeric Properties in XPO](xref:113533)
* [Numeric Properties in EF Core](xref:113534)

## ASP.NET Core Blazor

![|XAF ASP.NET Core Blazor Numeric Property Editors in List View, DevExpress](~/images/xaf-blazor-numeric-properties-listview-devexpress.png)

![|XAF ASP.NET Core Blazor Numeric Property Editors in Detail View, DevExpress](~/images/xaf-blazor-numeric-properties-detailview-devexpress.png)

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

### NumericPropertyEditor
	
Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxSpinEditModel<T>`.
	
Component: the [DxSpinEdit\<T\>](xref:DevExpress.Blazor.DxSpinEdit`1) editor shipped with the DevExpress ASP.NET Core Blazor Library.
	
Description:
	
This is the default Property Editor for the following numeric property types: `Int16`, `UInt16`, `Int32`, `UInt32`, `Int64`, `UInt64`, `float`, `double`, `Decimal`, `byte`.

To access and customize UI controls in XAF applications, create a @DevExpress.ExpressApp.ViewController that accesses a `NumericPropertyEditor` object to modify the underlying @DevExpress.Blazor.DxSpinEdit`1 control. For more information, refer to the following topic: [](xref:402153).

#### Disable Mouse Wheel Functionality

Users can scroll the mouse wheel to change the `NumericPropertyEditor`'s value. To disable this behavior, set the [DxSpinEdit.AllowMouseWheel](xref:DevExpress.Blazor.DxSpinEdit`1.AllowMouseWheel) property to `false`.

# [MySolution.Blazor.Server\Controllers\NumericPropertyEditorController.cs](#tab/tabid-csharp)
```csharp{8,10-11}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

public class CustomizeNumericPropertyEditorController : ViewController {

    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<NumericPropertyEditor>(this, editor => {
            editor.ComponentModel.AllowMouseWheel = false;
        });
    }
}
```
***

#### Hide Spin Buttons

A `NumericPropertyEditor` displays spin buttons that allow users to change the editor's value. To hide these buttons, set the [DxSpinEdit.ShowSpinButtons](xref:DevExpress.Blazor.DxSpinEdit`1.ShowSpinButtons) property to `false`.

# [MySolution.Blazor.Server\Controllers\NumericPropertyEditorController.cs](#tab/tabid-csharp)
```csharp{8,10-11}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

public class CustomizeNumericPropertyEditorController : ViewController {

    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<NumericPropertyEditor>(this, editor => {
            editor.ComponentModel.ShowSpinButtons = false;
        });
    }
}
```
***

#### Apply Numeric Mask

To apply a mask to a `NumericPropertyEditor`, use the [EditMask](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask) property and the [Numeric](xref:1498) mask type syntax.

To further customize the mask, access the `NumericPropertyEditor.MaskProperties` property.

For an example, refer to the following topic: [Access EditMask In Code](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask#access-editmask-in-code).

### ProgressBarPropertyEditor

Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxProgressBar`.
	
Component: the [](xref:DevExpress.Blazor.DxProgressBar) editor shipped with the DevExpress ASP.NET Core Blazor Library.
	
Description:
	
[!include[<MinValue><MaxValue>](~/templates/progressbareditordescription.md)]

To access and customize a `ProgressBarPropertyEditor` in XAF applications, create a @DevExpress.ExpressApp.ViewController that accesses a `ProgressBarPropertyEditor` object and modifies the underlying @DevExpress.Blazor.DxProgressBar control. For more information about Property Editor customization in Detail Views, refer to the following topic: [](xref:402153).

The following code snippet specifies a new `MinValue` and `MaxValue` for a **ProgressBarPropertyEditor** in a List View:

# [MySolution.Blazor.Server\Controllers\NumericPropertyEditorController.cs](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp;

namespace MySolution.Blazor.Server.Controllers;

public partial class NumericPropertyEditorController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        if (View.Editor is DxGridListEditor gridListEditor) {
            gridListEditor.CustomizeViewItemControl<ProgressBarPropertyEditor>(this, e => {
                e.ComponentModel.MinValue = 200;
                e.ComponentModel.MaxValue = 400;
            });
        }
    }
}
```
***

## WinForms

![|XAF Windows Forms Numeric Property Editors in List View, DevExpress](~/images/xaf-win-numericproperties-listview-devexpress.png)

![|XAF Windows Forms Numeric Property Editors in Detail View, DevExpress](~/images/xaf-win-numericproperties-detailview-devexpress.png)

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### BytePropertyEditor
	
Control: `IntegerEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.SpinEdit) editor shipped with the XtraEditors Library.
	
Repository Item: `RepositoryItemIntegerEdit` -- a descendant of the XtraEditors Library's [](xref:DevExpress.XtraEditors.Repository.RepositoryItemSpinEdit) item.
	
Description:
	
This is the default Property Editor for `byte` properties.
	
The editor is a descendant of the `IntegerPropertyEditor` class. If the repository item's `MaxValue` property is set to `0` or to a value that exceeds `Byte.MaxValue`, the property value is reset to `Byte.MaxValue`. If the repository item's `MinValue` property is set to `0` or to a value that is less than `Byte.MinValue`, the property value is reset to `Byte.MinValue`.

### DecimalPropertyEditor
	
Control: `DecimalEdit` -- a descendant of the `SingleEdit` editor used by the `FloatPropertyEditor`.
	
Repository Item: `RepositoryItemDecimalEdit` -- a `RepositoryItemSingleEdit` item descendant used by the `FloatPropertyEditor`.
	
Description:
	
This is the default Property Editor for `decimal` properties.
	
The `RepositoryItemSingleEdit` class helps to store and display values using the `C` [Numeric](xref:1498) edit mask when the Property Editor's `EditMask` is not specified.

### DoublePropertyEditor
	
Control: `DoubleEdit` -- a `SingleEdit` editor descendant used by the `FloatPropertyEditor`.
	
Repository Item: `RepositoryItemDoubleEdit` -- a `RepositoryItemSingleEdit` item descendant used by the `FloatPropertyEditor`.
	
Description:
	
This is the default Property Editor for `double` properties.

### FloatPropertyEditor
	
Control: `SingleEdit` -- an `IntegerEdit` editor descendant used by the `IntegerPropertyEditor`.
	
Repository Item: `RepositoryItemSingleEdit` -- a `RepositoryItemIntegerEdit` item descendant used by the `IntegerPropertyEditor`.
	
Description:
	
This is the default Property Editor for `float` properties.
	
The `RepositoryItemIntegerEdit` class allows you to display float values.

### IntegerPropertyEditor
	
Control: `IntegerEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.SpinEdit) editor shipped with the XtraEditors Library.
	
Repository Item: `RepositoryItemIntegerEdit` -- a descendant of the XtraEditors Library's [](xref:DevExpress.XtraEditors.Repository.RepositoryItemSpinEdit) item.
	
Description:
	
This is the default Property Editor for `Int32` properties.
	
An `IntegerPropertyEditor` object has the `EditMask` property. This property's default value is the [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node's [IModelCommonMemberViewItem.EditMask](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask) property value. When you assign a value to this property or to the `EditMask` attribute directly in code, use the syntax of the [Numeric](xref:1498) mask type. In this instance, the specified mask is applied to the property value displayed by the Property Editor. Refer to the following topic for more information: [Mask Editors Overview | Mask Types](xref:583).

### LongPropertyEditor
	
Control: `IntegerEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.SpinEdit) editor shipped with the XtraEditors Library.
	
Repository Item: `RepositoryItemIntegerEdit` -- a descendant of the XtraEditors Library's [](xref:DevExpress.XtraEditors.Repository.RepositoryItemSpinEdit) item.
	
Description:
	
This is the default Property Editor for `Int64` properties.
	
The editor is an `IntegerPropertyEditor` class descendant. If the repository item's `MaxValue` property is set to `0` or to a value that exceeds `Long.MaxValue`, the property value is reset to `Long.MaxValue`. If the repository item's `MinValue` property is set to `0` or to a value that is less than `Long.MinValue`, the property value is reset to `Long.MinValue`.

### ProgressBarPropertyEditor

Control: `ProgressBar` -- a descendant of the [](xref:DevExpress.XtraEditors.ProgressBarControl) editor shipped with the XtraEditors Library.
	
Repository Item: `RepositoryItemProgressBar` -- a descendant of the XtraEditors Library's [](xref:DevExpress.XtraEditors.Repository.RepositoryItemProgressBar) item.
	
Description:
	
[!include[<Minimum><Maximum>](~/templates/progressbareditordescription.md)]

>[!NOTE]
> The minimum value cannot exceed the maximum value. When you customize these values in code, make sure that the maximum value is assigned first. For more information, refer to the following topic: @DevExpress.XtraEditors.Repository.RepositoryItemProgressBar

To access and customize a `ProgressBarPropertyEditor` in XAF applications, create a @DevExpress.ExpressApp.ViewController that accesses a `ProgressBarPropertyEditor` object and modifies the underlying `ProgressBar` control. For more information about Property Editor customization in Detail Views, refer to the following topic: [](xref:402153).

# [MySolution.Win\Controllers\NumericPropertyEditorController.cs](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp;

namespace MySolution.Blazor.Server.Controllers;

public class NumericPropertyEditorController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ProgressBarPropertyEditor>(this, e => {
           e.Control.Properties.Minimum = 200;
           e.Control.Properties.Maximum = 400;
        });
    }
}
```
***
