To display View Items according to layout settings defined in a DetailView or DashboardView node of the Application Model, XAF applications use platform-specific Layout Managers. Each Layout Manager uses its own component to display controls in a [Composite View](xref:DevExpress.ExpressApp.CompositeView):

ASP.NET Core Blazor
:   `BlazorLayoutManager`: @DevExpress.Blazor.DxFormLayout
Windows Forms
:   `WinLayoutManager`: @DevExpress.XtraLayout.LayoutControl

Technically, an XAF Layout Manager is a wrapper around platform-specific UI controls, and provides a common API for layout customization. Useful APIs of the `LayoutManager` descendants include:
- `ItemCreated` and `LayoutCreated` events -- to track layout item creation
- The `Container` property -- to access the underlying layout control instance
- The `CustomizationFormEnabled` property -- an `IModelView.CustomizationFormEnabled` alternative to disable runtime layout customizations