---
uid: DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])
name: CustomizeViewItemControl<T>(View, Controller, Action<T>, String[])
type: Method
summary: Allows you to access and customize controls of the specified [View Item](xref:112612) in ASP.NET Core Blazor applications. This applies to View Items in Detail View, Dashboard View, and List View (DxGridListEditor and DxTreeListEditor in edit mode)
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this View view, Controller controller, Action<T> customizeAction, params string[] viewItemsId)
        where T : ViewItem
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A View that contains the specified View Item.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of the specified View Item.
  - id: customizeAction
    type: System.Action{{T}}
    description: A method to customize controls of the specified View Item.
  - id: viewItemsId
    type: System.String[]
    description: The View Item identifier.
  typeParameters:
  - id: T
    description: The View Item type.
seealso: []
---

The following code snippet uses the @DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[]) method to hide buttons for the specified Property Editor when [in-place editing](xref:113249#in-place-editing) is enabled in a List View:

[!include[<MySolution.Blazor.Server\Controllers\LookupActionVisibilityController.cs>](~/templates/platform_specific_file_path.md)]

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

namespace MySolution.Blazor.Server.Controllers;

public class CustomizeInlinePropertyEditorController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
            e.HideNewButton();
            e.HideEditButton();
        }, nameof(MyClass.ReferenceProperty));
    }
}
```