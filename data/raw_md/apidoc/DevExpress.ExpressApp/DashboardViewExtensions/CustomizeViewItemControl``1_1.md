---
uid: DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])
name: CustomizeViewItemControl<T>(DashboardView, Controller, Action<T>, String[])
type: Method
summary: Allows you to access and customize controls of the Dashboard View Item.
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this DashboardView view, Controller controller, Action<T> customizeAction, params string[] viewItemsId)
        where T : ViewItem
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DashboardView
    description: The specified View type.
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
ASP.NET Core Blazor
:   The following code snippet enables HTML markup in a Static Text component:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Editors;

    namespace MySolution.Blazor.Server.Controllers;

    public class CustomizeDashboardViewController : ViewController<DashboardView> {
            protected override void OnActivated() {
                base.OnActivated();
                View.CustomizeViewItemControl<StaticTextViewItem>(this, item => {
                    item.ComponentModel.UseMarkupString = true;
                }, "StaticTextViewItemId");
            }
        }
    ```


Windows Forms
:   The following code snippet specifies the background color in a Static Text component:

    ```csharp
    using DevExpress.ExpressApp;

    namespace MySolution.Win.Controllers;

    public class CustomizeDashboardViewController : ViewController<DashboardView> {
            protected override void OnActivated() {
                base.OnActivated();
                View.CustomizeViewItemControl<StaticTextViewItem>(this, item => {
                    if(item is StaticTextViewItem staticTextViewItem) {
                        staticTextViewItem.Label.BackColor = Color.Red;
                    }
                }, "StaticTextViewItemId");
            }
        }
    ```