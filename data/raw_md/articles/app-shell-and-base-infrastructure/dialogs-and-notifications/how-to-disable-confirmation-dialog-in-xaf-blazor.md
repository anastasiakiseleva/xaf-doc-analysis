---
uid: "404550"
title: 'How to: Disable a Confirmation Dialog in an ASP.NET Core Blazor Application'
owner: Anastasiya Kisialeva
seealso:
- linkId: "DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.ConfirmUnsavedChanges"
---
# How to: Disable a Confirmation Dialog in an ASP.NET Core Blazor Application

In XAF ASP.NET Core Blazor applications, a confirmation dialog appears if you attempt to exit a view without saving your changes. The following Controllers implement this functionality:
* `ConfirmationDetailViewController` in Detail Views.
* `ConfirmationListViewController` in List Views.

This topic demonstrates how to disable the confirmation dialog in a Detail View.

## Step-by-Step Instructions

1. In the _YourSolutionName.Blazor.Server\Controllers_ folder, create a new Controller and name it _BlazorSuppressConfirmationsController_.
2. Replace the auto-generated code with the following code snippet:
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.SystemModule;

    namespace MainDemo.Module.Blazor.Controllers {
        public class BlazorSuppressConfirmationsController : ViewController {
            protected override void OnActivated() {
                base.OnActivated();
                    var confirmationDetailViewController = Frame.GetController<ConfirmationDetailViewController>();
                    if (confirmationDetailViewController != null) {
                        confirmationDetailViewController.Active["DeactivateInCode"] = false;
                }
            }
        }
    }
    ```
3. Build the project and run the application. Open a Detail View and change a property value. When you close the view, XAF does not save the changes and the confirmation dialog does not appear.

> [!TIP]
> The `ConfirmationDetailViewController` and `ConfirmationListViewController` are active for [non-persistent objects](xref:116516) only if the @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange property is set to `true`.