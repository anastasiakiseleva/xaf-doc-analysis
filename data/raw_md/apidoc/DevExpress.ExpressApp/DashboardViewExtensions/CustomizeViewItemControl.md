---
uid: DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem},System.String[])
name: CustomizeViewItemControl(DashboardView, Controller, Action<ViewItem>, String[])
type: Method
summary: Allows you to access and customize controls of the Dashboard View Item.
syntax:
  content: public static void CustomizeViewItemControl(this DashboardView view, Controller controller, Action<ViewItem> customizeAction, params string[] viewItemsId)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DashboardView
    description: The Dashboard View.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of the Dashboard View Item.
  - id: customizeAction
    type: System.Action{DevExpress.ExpressApp.Editors.ViewItem}
    description: A method to customize controls of the specified View Item.
  - id: viewItemsId
    type: System.String[]
    description: The control's identifier.
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
                View.CustomizeViewItemControl(this, item => {
                    if(item is StaticTextViewItem staticTextViewItem) {
                      staticTextViewItem.ComponentModel.UseMarkupString = true;
                    }
                });
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
                View.CustomizeViewItemControl(this, item => {
                    if(item is StaticTextViewItem staticTextViewItem) {
                        staticTextViewItem.Label.BackColor = Color.Red;
                    }
                });
            }
        }
    ```