---
uid: "405839"
title: Add a Custom Button to a Property Editor (ASP.NET Core Blazor)
seealso:
  - linkId: '113014'
  - linkId: '402188'
  - linkId: '402189'
  - linkId: '403870'
---
# Add a Custom Button to a Property Editor (ASP.NET Core Blazor)

In the XAF ASP.NET Core Blazor UI, you can add custom buttons to built-in Property Editors, such as text, numeric, date/time, and lookup editors. Handle the custom button’s `Click` event to implement required functionality.

## How Custom Buttons Work in Property Editors

Property Editors that support custom buttons expose a custom button collection (`Buttons`). Each collection element is a `DxEditorButtonModel` object. This type is a XAF wrapper model that you can use to access [DxEditorButton](xref:DevExpress.Blazor.DxEditorButton) properties.

When you add, remove, or replace items in the `Buttons` collection, XAF automatically updates the application's UI.

XAF renders buttons in the Property Editor's button area in the following order:
- The **Clear** button
- Custom buttons 
- Built-in buttons 

Custom buttons appear in the same order as they are defined in the `Buttons` collection.

## Supported Editors

The following Property Editor classes support custom buttons:

- [BooleanPropertyEditor](xref:113540#aspnet-core-blazor) based on [DxComboBox\<TData, TValue>](xref:DevExpress.Blazor.DxComboBox`2)
- [ComboBoxListPropertyEditor](xref:113568#comboboxlistpropertyeditor)
- [DateTimePropertyEditor and TimeSpanPropertyEditor](xref:113536#aspnet-core-blazor)
- [DxFileDataPropertyEditor](xref:113548#dxfiledatapropertyeditor)
- [EnumPropertyEditor](xref:113552#aspnet-core-blazor)
- [LookupPropertyEditor and ObjectPropertyEditor](xref:113572#lookuppropertyeditor)
- [NumericPropertyEditor](xref:113532#numericpropertyeditor)
- [StringPropertyEditor](xref:113528#stringpropertyeditor) based on [DxTextBox](xref:DevExpress.Blazor.DxTextBox), [DxMaskedInput\<T>](xref:DevExpress.Blazor.DxMaskedInput`1), or [DxComboBox\<TData, TValue>](xref:DevExpress.Blazor.DxComboBox`2)
- [TypePropertyEditor](xref:113579#typepropertyeditor)

> [!TIP]
> You can also add custom buttons to a [property editor based on a custom component](xref:402189).

## Add a Custom Button

The following code snippet adds a custom button and specifies its icon, tooltip, and a [text message](xref:118549) that appears when a user clicks the button.

Add this controller to your _SolutionName.Blazor.Server_ project.

**File:** _SolutionName.Blazor.Server/Controllers/PropertyEditorCustomButtonDetailViewController.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;
using SolutionName.Module.BusinessObjects;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;

namespace SolutionName.Blazor.Server.Controllers;

public class PropertyEditorCustomButtonDetailViewController : ObjectViewController<DetailView, PhoneNumber> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StringPropertyEditor>(this, Customize_PhoneNumberEditor, nameof(PhoneNumber.Number));
    }

    private void Customize_PhoneNumberEditor(StringPropertyEditor editor) {
        var customButtonModel = new DxEditorButtonModel() {
            IconCssClass = "fluent-icon fluent-icon-phone",
            Tooltip = "Call this phone number",
            Click = EventCallback.Factory.Create<MouseEventArgs>(this,
                 (e) => Application.ShowViewStrategy.ShowMessage($"Calling {ViewCurrentObject.Number}..."))
        };
        editor.Buttons.Add(customButtonModel);
    }
}
```

![XAF ASP.NET Core Blazor: Custom Button in a Detail View Property Editor, DevExpress](~/images/xaf-blazor-custom-button-in-property-editor-devexpress.png)

You can use the same technique in List Views. Use a ListView-specific controller base and target an editable List View.

> [!TIP]
> Ensure that [in-place editing](xref:113249#in-place-editing) is enabled for the required List View. Otherwise, XAF does not create Property Editors in List Views.

**File:** _SolutionName.Blazor.Server/Controllers/PropertyEditorCustomButtonListViewController.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;
using SolutionName.Module.BusinessObjects;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;

namespace SolutionName.Blazor.Server.Controllers;

public class PropertyEditorCustomButtonListViewontroller : ObjectViewController<ListView, PhoneNumber> {
    public PropertyEditorCustomButtonListViewController() {
        TargetViewId = "Employee_PhoneNumbers_ListView";
    }
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StringPropertyEditor>(this, Customize_PhoneNumberEditor, nameof(PhoneNumber.Number));
    }

    private void Customize_PhoneNumberEditor(StringPropertyEditor editor) {
        var customButtonModel = new DxEditorButtonModel() {
            IconCssClass = "fluent-icon fluent-icon-phone",
            Tooltip = "Call this phone number",
            Click = EventCallback.Factory.Create<MouseEventArgs>(this,
                 (e) => Application.ShowViewStrategy.ShowMessage($"Calling {((PhoneNumber)editor.CurrentObject).Number}..."))
        };
        editor.Buttons.Add(customButtonModel);
    }
}
```

![XAF ASP.NET Core Blazor: Custom Button in a List View Property Editor, DevExpress](~/images/xaf-blazor-custom-button-in-property-editor-listview-devexpress.png)
