---
uid: DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{``0})
name: CustomizeViewItemControl<T>(View, Controller, Action<T>)
type: Method
summary: Allows you to access controls of [View Item](xref:112612) that the specified View contains in ASP.NET Core Blazor applications. This applies to View Items in Detail View, Dashboard View, and List View (DxGridListEditor and DxTreeListEditor in edit mode)
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this View view, Controller controller, Action<T> customizeAction)
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
  typeParameters:
  - id: T
    description: The View Item type.
seealso: []
---

The following code snippet uses the @DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{``0}) method to hide buttons when [in-place editing](xref:113249#in-place-editing) is enabled in a List View:

[!include[<MySolution.Blazor.Server\Controllers\LookupActionVisibilityController.cs>](~/templates/platform_specific_file_path.md)]

[!include[blazorutils-customizeviewitemcontrol-1](~/templates/blazorutils-customizeviewitemcontrol-1.md)]