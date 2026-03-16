---
uid: DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{``0})
name: CustomizeViewItemControl<T>(DashboardView, Controller, Action<T>)
type: Method
summary: Allows you to access and customize controls of the Dashboard View Item.
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this DashboardView view, Controller controller, Action<T> customizeAction)
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
  typeParameters:
  - id: T
    description: The View Item type.
seealso: []
---
[!include[statictextviewitem-customization](~/templates/statictextviewitem-customization.md)]