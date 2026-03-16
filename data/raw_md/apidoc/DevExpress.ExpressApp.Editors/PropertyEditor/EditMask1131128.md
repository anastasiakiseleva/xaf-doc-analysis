---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.EditMask
name: EditMask
type: Property
summary: Specifies a mask expression for a [Property Editor's](xref:113097) control.
syntax:
  content: public string EditMask { get; set; }
  parameters: []
  return:
    type: System.String
    description: A mask expression for a [Property Editor's](xref:113097) control.
seealso:
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat
- linkId: "113015"
- linkId: "583"
- linkId: "402141"
- linkId: "402154"
---

Use `EditMask` to specify a format or pattern that an input value should follow in XAF ASP.NET Core Blazor applications. For example, if an editor field accepts phone numbers, you can set the editor's mask to `(000) 000-0000`.

![|XAF ASP.NET Core Blazor Masked Editor, DevExpress|](~/images/mask-edit.png)

> [!NOTE]
> In XAF Windows Forms applications, use [ModelMaskSettings.MaskSettings](xref:DevExpress.ExpressApp.Win.SystemModule.IModelMaskSettings.MaskSettings) instead.

Mask expression syntax depends on the mask type. For more information about available mask types and their syntaxes, refer to the following topics:
* [MaskMode Enum](xref:DevExpress.Blazor.MaskMode) (ASP.NET Core Blazor).
* [Mask Types](xref:583#mask-types) (Windows Forms).

## Access Edit Mask In the Model Editor

You can set the `EditMask` property in the [Application Model](xref:112580). In the [Model Editor](xref:112830), locate the View Item node that corresponds to the Property Editor. In that node, set the [EditMask](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask) property value.

![The EditMask Property in XAF Model Editor, DevExpress](~/images/mask-edit-model-editor.png)

## Access EditMask In Code

You can specify the `EditMask` property in the Controller's code. You can further customize the mask properties by accessing the Property Editor's Control:

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using MainDemo.Module.BusinessObjects;
 
namespace MainDemo.Blazor.Server.Controllers;
public class CustomizeEditMaskController : ObjectViewController<DetailView, Employee> {
    protected override void OnActivated() {
        base.OnActivated();
        if(View.FindItem(nameof(Employee.LastName)) is StringPropertyEditor editor) {
            editor.EditMask = "#####";
        }
        View.CustomizeViewItemControl<StringPropertyEditor>(this, SetMaskedInputProperties, nameof(Employee.LastName));
    }
    private void SetMaskedInputProperties(StringPropertyEditor editor) {
        if(editor.ComponentModel is DxMaskedInputModel maskedInputModel) {
            editor.DxMaskedInputMaskProperties.Text.Placeholder = '?';
            maskedInputModel.MaskMode = DevExpress.Blazor.MaskMode.Text;
        }
    }
}
```
 
***

For more information on how to access editors in code, refer to the following topic: [](xref:402153).

If you create a custom Property Editor that should support the `EditMask` property, implement your own logic to apply the `EditMask` property value to your custom Property Editor.

[!include[EditMaskNote](~/templates/editmasknote11188.md)]
