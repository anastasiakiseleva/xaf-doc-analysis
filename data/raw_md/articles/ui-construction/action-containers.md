---
uid: "112610"
title: Action Containers
seealso:
- linkId: "112622"
- linkId: "112621"
- linkId: "112609"
- linkId: "404559"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-add-custom-buttons-actions-to-the-lookup-and-popup-windows
  altText: 'GitHub Example: XAF - Add Custom Buttons (Actions) to Lookup and Popup Windows'
---
# Action Containers

 _Action Containers_ are placeholders for [Actions](xref:112622) (several action may appear within a single container). [Templates](xref:112609) define the position of Action Containers on screen.

This topic explains how to customize existing Action Containers and implement your own.

XAF supplies a number of built-in Action Containers for automatic UI construction. Built-in Action Containers for ASP.NET Core Blazor and Windows Forms applications ship with the **DevExpress.ExpressApp.Blazor** and **DevExpress.ExpressApp.Win** assemblies, respectively.

You can find the list of all Action Containers in the **ActionDesign** | **ActionToContainerMapping** node of the [Application Model](xref:112580).

## ASP.NET Core Blazor Action Containers

The following images show Action Container placement in ASP.NET Core Blazor application UI:

![|ASP.NET Core Blazor Containers|](~/images/action-container-1-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers|](~/images/action-container-2-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers in Grid Columns|](~/images/action-container-gridcolumn-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers in Popup Windows|](~/images/action-container-popup-blazor-devexpress.png)

> [!TIP]
> For more information about Actions in grid columns in ASP.NET Core Blazor application, refer to the following topic: [](xref:404559).

## Action Container Creation

When XAF creates a Template, it also creates all Action Containers that belong to this Template. The built-in `FillActionContainers` Controller determines Actions that populate each Action Container. That information comes from the **ActionDesign** | **ActionToContainerMapping** node of the [Application Model](xref:112580). The `FillActionContainers` Controller calls the Action Container's `Register` method to create a control for each Action. For example, in a Windows Forms application, the `ActionContainerBarItem` Action Container creates a `BarButtonItem` object for a `SimpleAction` and a `BarEditItem` control for a `SingleChoiceAction`.

## Action Container Customization

You can customize the Actions of a particular Action Container in code, at design time, and at runtime.

### In the Application Model
	
The [Application Model](xref:112580) contains the **ActionDesign**  | **ActionToContainerMapping** node. This node contains information on what Actions a particular Action Container must display. You can customize the automatically generated information in the [Model Editor](xref:112582) at design time or at runtime (see [](xref:402145)). In this node, you can move an Action to another Action Container, delete an Action from a particular Action Container, etc. You can also add a new Action Container and add Actions to it, but such an Action Container only appears in a UI if it belongs to a Template. For more information about this Application Model node, refer to the [](xref:DevExpress.ExpressApp.Model.IModelActions) interface description.

### In code
	
To customize an Action Container, handle the [Frame.ProcessActionContainer](xref:DevExpress.ExpressApp.Frame.ProcessActionContainer) event. You can customize an Action Container using its properties. You can also use the [IActionContainer.Actions](xref:DevExpress.ExpressApp.Templates.IActionContainer.Actions) property to access Actions of a particular Action Container and customize these Actions. For example, you can toggle an Action's [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) property to deactivate this Action. You can also access an Action's control and customize it.

To customize a toolbar item, handle the `CustomizeActionControl` event of the corresponding bar item factory. For additional information, refer to the following topic: [](xref:113183).

You can handle the [ActionControlsSiteController.CustomizeContainerActions](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions) event to customize the action-to-container mapping in code.

### In ASP.NET Core Blazor Application Template

In ASP.NET Core Blazor applications, you can group Actions in a drop-down menu. You can display the root item as a split button (specify one of included Actions as default). You can also enable a traditional sub-menu UI (specify a caption and/or image for the root item).

![|ASP.NET Blazor SaveOptions Container|](~/images/saveoptions-action-container-blazor-devexpress.png)

Create a [custom Blazor application template](xref:403452) and specify the following Action Container properties:

`isDropDown`
:   Specifies whether the container's Actions are grouped into a drop-down list.
`defaultActionId`
:   Specifies the root menu Action's identifier.
`autoChangeDefaultAction`
:   Specifies whether the last executed Action becomes the default one.
`imageName`
:   Specifies the image used as the root menu item.
`caption`
:   Specifies the caption used as the root menu item.

Image and caption are not mutually exclusive. You can use both as the root item at the same time.

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp.Blazor.Templates;
namespace YourSolutionName.Blazor.Server {
    public class CustomApplicationWindowTemplate : ApplicationWindowTemplate {
        public CustomApplicationWindowTemplate() {
            // Action as the root item
            Toolbar.AddActionContainer("SaveOptions", alignment: ToolbarItemAlignment.Right, isDropDown: true, defaultActionId: "SaveAndNew", autoChangeDefaultAction: true);
            // Image as the root item
            // Toolbar.AddActionContainer("SaveOptions", alignment: ToolbarItemAlignment.Right, isDropDown: true, imageName: "Save");
            // Caption as the root item
            // Toolbar.AddActionContainer("SaveOptions", alignment: ToolbarItemAlignment.Right, isDropDown: true, caption: "Save Options");
        }
    }
}
```

If you omit `defaultActionId`, `imageName`, and `caption` parameters, XAF displays the first Action as the root item.

If you specify a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) as default, it is displayed in the main menu without child items.

The drop-down menu does not support `ParametrizedAction` and `SingleChoiceAction` with [ItemType](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType) set to [SingleChoiceActionItemType.ItemIsMode](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionItemType).

## Implement Your Own Action Container

If you need to change controls used to display Actions, you can implement your own Action Containers. To do this, inherit from the required control and implement the [](xref:DevExpress.ExpressApp.Templates.IActionContainer) interface. Alternatively, you can derive your custom container from one of the existing Action Containers. You may also need to specify the controls XAF should use for each Action type.

After you declared your own Action Container, create a new Template or customize an existing template as described in the following topics:

* [](xref:403452)
* [](xref:113706)
* [](xref:112618)

Add your Action Container to the Template and add your Action Container's instance to the list returned by the Template's [IFrameTemplate.GetContainers](xref:DevExpress.ExpressApp.Templates.IFrameTemplate.GetContainers) method.

If you have XAF sources installed, you can see how built-in Action Containers are implemented in the following locations:

* [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Web\Templates\ActionContainers\
* [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Win\Templates\ActionContainers\
* [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Blazor\Templates\
