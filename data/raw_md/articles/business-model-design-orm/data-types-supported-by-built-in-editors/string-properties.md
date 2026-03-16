---
uid: "113528"
title: String Properties
owner: Ekaterina Kiseleva
seealso:
  - linkId: "404597"
  - linkId: "113101"
  - linkId: "403100"
  - linkId: "402188"
---
# String Properties

XAF supports [Property Editors](xref:113097) for the `string` data type on all platforms. The Property Editor type depends on the underlying property's attributes and settings specified in the Application Model.

* Text editors display string properties with a fixed length (for example, 100 or 15 characters).
* Memo editors display large string properties. The default List Views do not display these properties.
* Combo boxes display string properties with the [predefined values](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PredefinedValues) specified in the Application Model.
* [Rich Text Editors](xref:400004) can display string properties with HTML-formatted string values.

The list below contains XPO-specific notes related to string properties:

* If you assign a `StringCompressionConverter` [Value Converter](xref:2053) to a string property, databases store these properties in a compressed form.
* You can use the [Delayed Loading](xref:2024) feature to improve performance when handling unlimited size properties.

Refer to the following topics for information on how to add string properties to business classes in the supported ORM systems:

* [String Properties in XPO](xref:113529)
* [String Properties in EF Core](xref:113530)

## ASP.NET Core Blazor

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

### StringPropertyEditor

IComponentContentHolder descendant:

The table below shows the match between the `IComponentContentHolder` descendant type and the resulting UI component type.

| Component Model | A Blazor component | Additional info
|--------|--------|--------|
| `DevExpress.ExpressApp.Blazor.Components.Models.DxTextBoxModel` | @DevExpress.Blazor.DxTextBox | The `DxTextBox` component is used when the corresponding **BOModel** \| **_\<Class\>_** \| **OwnMembers** \| **_\<Member\>_** node's [IModelCommonMemberViewItem.RowCount](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.RowCount) property is set to `0` (default) or `1`.|
| `DevExpress.ExpressApp.Blazor.Components.Models.DxMaskedInputModel<T>` | @DevExpress.Blazor.DxMaskedInput`1 | The `DxMaskedInput<T>` component is used when the corresponding **BOModel** \| **_\<Class\>_** \| **OwnMembers** \| **_\<Member\>_** node's [IModelCommonMemberViewItem.EditMask](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask) property is specified. For more information, refer to the following topic: [](xref:402141). |
| `DevExpress.ExpressApp.Blazor.Components.Models.DxMemoModel` | @DevExpress.Blazor.DxMemo | The `DxMemo` component is used when the corresponding **BOModel** \| **_\<Class\>_** \| **OwnMembers** \| **_\<Member\>_** node's [IModelCommonMemberViewItem.RowCount](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.RowCount) property value exceeds `1`. |
| `DevExpress.ExpressApp.Blazor.Components.Models.DxComboBoxModel<TData, TValue>` | @DevExpress.Blazor.DxComboBox`2 | The `DxComboBox` component is used when the corresponding **BOModel** \| **_\<Class\>_** \| **OwnMembers** \| **_\<Member\>_** node's `PredefinedValues` property is specified. Press Alt+Down to expand the control's drop-down window. |

![blazor_string_properties_editors](~/images/blazor_string_properties_editors.png)

Description:
	
This is the default Property Editor for `string` properties.

#### Hide the Clear Button

`DxTextBox` and `DxMaskedInput` display the **Clear** button when the editor's value is not empty. To hide this button, ensure that the editor's @DevExpress.Blazor.Base.DxInputDataEditorBase`1.ClearButtonDisplayMode property is set to `DevExpress.Blazor.DataEditorClearButtonDisplayMode.Never`.

The following code snippet hides the **Clear** button in all `DxTextBox` components.

```csharp{8,10,11}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

public class CustomizeStringPropertyEditorController : ViewController {

    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StringPropertyEditor>(this, editor => {
            editor.ComponentModel.ClearButtonDisplayMode = DevExpress.Blazor.DataEditorClearButtonDisplayMode.Never;
        });        
    }
}
```

#### Customize Mask Properties of a Masked Input Component

To customize mask properties of a masked input component, specify the `MaskMode` property explicitly:

```csharp{11}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;

namespace YourApplicationName.Module.Controllers {
    public class CustomizeMaskPropertiesController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<StringPropertyEditor>(this, editor => {
                if(editor.ComponentModel is DxMaskedInputModel maskedInput) {
                    maskedInput.MaskMode = DevExpress.Blazor.MaskMode.Text;
                    editor.DxMaskedInputMaskProperties.Text.Placeholder = '?';
                }
            });
        }
    }
}
```
	
### RichTextPropertyEditor

![blazor_string_properties_rich_text_editor](~/images/blazor_string_properties_rich_text_editor.png)
	
Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxRichEditModel`.
	
Component: the [DxRichEdit](xref:DevExpress.Blazor.RichEdit.DxRichEdit) editor shipped with the DevExpress ASP.NET Core Blazor Library.
	
Description:
	
You can use this editor for string properties in List and Detail Views. The editor is supplied with the [Office Module](xref:400003).
	
`RichTextPropertyEditor` allows you to [edit rich text documents](xref:400004) stored in RTF or HTML format. For more information, refer to the following topic: [Use Rich Text Documents in Business Objects](xref:400004).


## WinForms

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### StringPropertyEditor

![XAF StringPropertyEditor WinForms](~/images/pe_stringwin117302.png)	

Controls:
	
* `StringEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.TextEdit) editor shipped with the XtraEditors Library.
* `PredefinedValuesStringEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.ComboBoxEdit) editor shipped with the XtraEditors Library.
* `LargeStringEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.MemoEdit) editor shipped with the XtraEditors Library.
	
Repository Items:
	
* `RepositoryItemStringEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.Repository.RepositoryItemTextEdit) item shipped with the XtraEditors Library.
* `RepositoryItemPredefinedValuesStringEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.Repository.RepositoryItemComboBox) item shipped with the XtraEditors Library.
* A [](xref:DevExpress.XtraEditors.Repository.RepositoryItemMemoExEdit) item shipped with the XtraEditors Library.
	
Description:
	
This is the default Property Editor for `string` properties.
	
The `StringEdit` control and the `RepositoryItemStringEdit` item are used when the corresponding **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's `RowCount` property is set to `0` (default) or `1`.
	
The `PredefinedValuesStringEdit` control and `RepositoryItemPredefinedValuesStringEdit` items are used when the corresponding **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's `RowCount` property is set to `0` or `1`, and the `PredefinedValues` property is specified. Press Alt+Down Arrow to expand the control's drop-down window.
	
The `LargeStringEdit` control and `RepositoryItemMemoExEdit` repository items are used when the corresponding **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's `RowCount` property value exceeds `1`. Note that this property affects only the minimum height of the `LargeStringEdit` control. The actual height is determined by the available space.
	
You can specify a mask for `StringPropertyEditor`. See the following topics for more information:

* @DevExpress.ExpressApp.Win.SystemModule.IModelMaskSettings.MaskSettings

* [Input Mask](xref:583)

* [](xref:402141)

> [!NOTE]
> The `StringEdit` control and the `RepositoryItemStringEdit` item can be used to display a non-string property. For this purpose, assign the `DevExpress.ExpressApp.Win.Editors.StringPropertyEditor` Property Editor for the required **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's `PropertyEditorType` property. In this instance, the `StringEdit` control shows the property's display text.

### RichTextPropertyEditor

![XAF RichEdit WinForms](~/images/richedit.png)

Control: `RichEditorContainer` -- a wrapper for the @DevExpress.XtraRichEdit.RichEditControl control shipped with the XtraEditors Library.

Repository Item: a @DevExpress.XtraEditors.Repository.RepositoryItemRichTextEdit item shipped with the XtraEditors Library.
	
Description:

Intended for string properties and can be used in List and Detail Views. This Property Editor is supplied with the [Office Module](xref:400003).
	
This Property Editor allows you to [edit rich text documents](xref:400004) stored in the RTF or HTML format and create [Mail Merge](xref:400006) templates. Refer to the [Use Rich Text Documents in Business Objects](xref:400004) topic for more information about the `RichTextPropertyEditor`.
