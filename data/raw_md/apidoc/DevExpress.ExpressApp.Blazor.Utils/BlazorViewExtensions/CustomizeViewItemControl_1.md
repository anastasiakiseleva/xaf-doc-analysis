---
uid: DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem})
name: CustomizeViewItemControl(View, Controller, Action<ViewItem>)
type: Method
summary: Allows you to access and customize controls of [View Items](xref:112612) that the specified View contains in ASP.NET Core Blazor applications. This applies to View Items in Detail View, Dashboard View, and List View (DxGridListEditor and DxTreeListEditor in edit mode)
syntax:
  content: public static void CustomizeViewItemControl(this View view, Controller controller, Action<ViewItem> customizeAction)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A View that contains the View Item with controls the `customizeAction` method customizes.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of the specified View Item.
  - id: customizeAction
    type: System.Action{DevExpress.ExpressApp.Editors.ViewItem}
    description: A method to customize controls of the specified View Item.
seealso: []
---
The following code snippet uses the @DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem}) method to enable HTML markup in a Static Text component:

[!include[<MySolution.Blazor.Server\Controllers\CustomizeViewController.cs>](~/templates/platform_specific_file_path.md)]

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

namespace MySolution.Blazor.Server;

public class CustomizeViewController : ViewController {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl(this, item => {
                if(item is StaticTextViewItem staticTextViewItem) {
                    staticTextViewItem.ComponentModel.UseMarkupString = true;
                }
            });
        }
    }
```