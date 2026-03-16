---
uid: DevExpress.ExpressApp.Blazor.Editors.BlazorPropertyEditorBase.ComponentModel
name: ComponentModel
type: Property
summary: Returns an `IComponentModel` descendant that wraps properties and events of a corresponding [ASP.NET Core Blazor Editor](xref:401156).
syntax:
  content: public virtual IComponentModel ComponentModel { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.Components.Models.IComponentModel
    description: A [component model](xref:402189#component-model) of an [ASP.NET Core Blazor Editor](xref:401156).
seealso:
- linkId: "402189"
---

To customize an ASP.NET Core Blazor Property Editor's underlying component, call the `View.CustomizeViewItemControl` method and obtain the component model (the `ComponentModel` property).

If the Property Editor you want to customize is based on a single ASP.NET Core Blazor component type, the `ComponentModel` property returns the corresponding `IComponentModel` descendant.

If the Property Editor is based on multiple ASP.NET Core Blazor component types, you need to check the type before you apply changes.

In the following code sample, [`ColorPropertyEditor`](xref:113658#aspnet-core-blazor)'s component model is of the [`DxComboBoxModel<DataItem<Color>, DataItem<Color>>`](xref:DevExpress.Blazor.DxComboBox`2) type. [`StringPropertyEditor`](xref:113528#stringpropertyeditor)'s component model can be one of 4 types.


# [BlazorDashboardController.cs](#tab/tabid-csharp-blazor)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
// ...
public class PropertyEditorCustomizeController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ColorPropertyEditor>(this, (colorPropertyEditor) => {
            colorPropertyEditor.ComponentModel.CssClass += " custom-class";
        });
        View.CustomizeViewItemControl<StringPropertyEditor>(this, (stringPropertyEditor) => {
            switch(stringPropertyEditor.ComponentModel) {
                case DxTextBoxModel textBox:
                    textBox.CssClass += " custom-class";
                    break;
                case DxComboBoxModel<string, string> comboBox:
                    comboBox.CssClass += " custom-class";
                    break;
                case DxMemoModel memoModel:
                    memoModel.CssClass += " custom-class";
                    break;
                case DxMaskedInputModel<string> maskedInput:
                    maskedInput.CssClass += " custom-class";
                    break;
            }
        });
    }
}

``` 
***

For more information about XAF's built-in Property Editors, refer to the following section: [](xref:113014).
