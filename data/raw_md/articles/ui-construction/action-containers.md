---
uid: "112610"
title: Action Containers
seealso:
- linkId: "112622"
- linkId: "112621"
- linkId: "112609"
- linkId: "402157"
- linkId: "112816"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-add-custom-buttons-actions-to-the-lookup-and-popup-windows
  altText: 'GitHub Example: XAF - Add Custom Buttons (Actions) to Lookup and Popup Windows'
---
# Action Containers

 Action Containers are UI placeholders that display [Actions](xref:112622) (commands and buttons) in an XAF application. They determine where actions appear, such as toolbars, menus, ribbons, and context menus. [Templates](xref:112609) control where containers appear on screen.

## Common Tasks with Action Containers

You interact with Action Containers when you want to reorganize your application's command UI, create custom toolbars, or control where specific actions appear:

- [Move an Action to a Different Toolbar or Menu](xref:402145)
- [Group Actions in a Drop-Down Menu (ASP.NET Core Blazor)](#group-actions-in-a-drop-down-menu-aspnet-core-blazor)
- [Add a Grid Column with an Action (ASP.NET Core Blazor)](xref:404559)
- [Create a Custom Action Container](#implement-a-custom-action-container)
- [Reorder Actions in an Action Container](xref:112815)

## How Action Containers Work

XAF creates Action Containers automatically when it initializes a Template. The process consists of the following steps:

1. **Template initialization.** XAF creates all Action Containers defined in the Template.
2. **Action mapping.** The built-in [FillActionContainersController](xref:113141#fillactioncontainerscontroller) reads the **ActionDesign** | **ActionToContainerMapping** node in the [Application Model](xref:112580) to determine which Actions belong in each container.
3. **Control creation.** The Controller calls each container's [`Register`](xref:DevExpress.ExpressApp.Templates.IActionContainer.Register(DevExpress.ExpressApp.Actions.ActionBase)) method to create platform-specific controls for Actions.

Example (Windows Forms):
- **SimpleAction** creates a `BarButtonItem` button control
- **SingleChoiceAction** creates a `BarEditItem` dropdown control

### ASP.NET Core Blazor Action Containers

The following images show Action Container placement in ASP.NET Core Blazor application UI:

![|ASP.NET Core Blazor Containers|](~/images/action-container-1-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers|](~/images/action-container-2-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers in Grid Columns|](~/images/action-container-gridcolumn-blazor-devexpress.png)

![|ASP.NET Core Blazor Containers in Popup Windows|](~/images/action-container-popup-blazor-devexpress.png)

> [!TIP]
> For more information about Actions in grid columns in ASP.NET Core Blazor applications, refer to the following topic: [](xref:404559).

## Customize Action Containers in the Application Model

**When to use:** Move Actions between existing containers (toolbars/menus) or delete Actions at design time or runtime.

For a detailed scenario, refer to the following topic: [How to: Place an Action in a Different Location](xref:402145).

For more information about this Application Model node, refer to the [](xref:DevExpress.ExpressApp.Model.IModelActions) interface description.

## Customize Action Containers in Code

**When to use:** Apply conditional logic or dynamic behavior that cannot be configured in the Application Model.

| API | Use |
|-|-|
| [Frame.ProcessActionContainer](xref:DevExpress.ExpressApp.Frame.ProcessActionContainer) | Use event's properties to customize Action Container |
| [IActionContainer.Actions](xref:DevExpress.ExpressApp.Templates.IActionContainer.Actions) | Access Actions of a particular Action Container and customize these Actions. For example, you can toggle an Action's [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) property to deactivate this Action. You can also access an Action's control and customize it.|
| [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) | Customize an Action Control. For a detailed scenario, refer to the following topic: [How to: Customize Action Controls](xref:113183) |
| [ActionControlsSiteController.CustomizeContainerActions](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions) | Customize the action-to-container mapping in code. |

## Group Actions in a Drop-Down Menu (ASP.NET Core Blazor)

**When to use:**
- Group Actions in a drop-down menu
- Display the root item as a split button (specify one of included Actions as default)
- Enable a traditional sub-menu UI (specify a caption and/or image for the root item)

> [!Important]
> Drop-down menus do not support `ParametrizedAction` and `SingleChoiceAction` when [ItemType](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType) is set to [SingleChoiceActionItemType.ItemIsMode](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionItemType).

### Action Container Properties

   | Property | Description |
   |-|-|
   | `isDropDown` | Specifies whether the container's Actions are grouped into a drop-down list. |
   | `defaultActionId` | Specifies the root menu Action's identifier. |
   | `autoChangeDefaultAction` | Specifies whether the last executed Action becomes the default one. |
   | `imageName` | Specifies the image used as the root menu item. |
   | `caption` | Specifies the caption used as the root menu item. |

> [!tip]
> - Image and caption are not mutually exclusive. You can use both as the root item at the same time.
> - If you omit `defaultActionId`, `imageName`, and `caption` parameters, XAF displays the first Action as the root item.
> - If you specify a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) as default, it is displayed in the main menu without child items.

### Drop-Down Menu in Main Toolbar

1. Create a [custom Blazor application template](xref:403452).
2. Specify the Action Container properties.

The following code snippet demonstrates the recommended approach (using an Action as the root item). Two alternative approaches are shown as comments.

**File:** _MySolution.Blazor.Server/Templates/CustomApplicationWindowTemplate.cs_

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp.Blazor.Templates;
namespace MySolution.Blazor.Server {
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

![|ASP.NET Blazor SaveOptions Container|](~/images/saveoptions-action-container-blazor-devexpress.png)

### Drop-Down Menu in Ribbon UI

1. Under the _MySolution.Blazor.Server_ project, [add a Window Controller](xref:405447#create-a-new-item) to the _Controllers_ folder.
2. Override the `OnActivated` method to access the `BlazorRibbonController` and subscribe to its `RibbonActionContainerCreating` event. This event fires when the controller generates a [DxRibbon](xref:DevExpress.Blazor.DxRibbon) [Action Container](xref:112610) model.
3. Specify the Action Container properties.

The following code snippet:
- Groups the Actions in the `SaveOptions` Container in a drop-down menu
- Sets the default Action to **SaveAndClose**
- Sets the last executed Action as the default

    **File:** _MySolution.Blazor.Server\Controllers\CustomizeRibbonActionContainerController.cs_

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.SystemModule;

    namespace MySolution.Blazor.Server.Controllers;

    public class CustomizeRibbonActionContainerController : WindowController {
        protected override void OnActivated() {
            base.OnActivated();
            var controller = Frame.GetController<BlazorRibbonController>();
            if(controller != null) {
                controller.RibbonActionContainerCreating += Controller_RibbonActionContainerCreating;
            }
        }
        private void Controller_RibbonActionContainerCreating(object sender, RibbonActionContainerCreatingEventArgs e) {
            if(e.ActionContainer.ContainerId == "SaveOptions") {
                e.ActionContainer.IsDropDown = true;
                e.ActionContainer.DefaultActionId = "SaveAndClose";
                e.ActionContainer.AutoChangeDefaultAction = true;
            }
        }
        protected override void OnDeactivated() {
            var controller = Frame.GetController<BlazorRibbonController>();
            if(controller != null) {
                controller.RibbonActionContainerCreating -= Controller_RibbonActionContainerCreating;
            }
            base.OnDeactivated();
        }
    }
    ```

## Implement a Custom Action Container

**When to use:** Replace the default controls with custom UI components (advanced scenario).

1. Inherit from the desired platform control and implement the [](xref:DevExpress.ExpressApp.Templates.IActionContainer) interface. Alternatively, you can inherit your custom container from one of the existing Action Containers. You may also need to specify the controls XAF should use for each Action type.
2. After you declared your own Action Container, create a new Template or customize an existing template as described in the following topics:

    - [](xref:403452)
    - [](xref:113706)
    - [](xref:112618)

3. Add your Action Container to the Template and add your Action Container's instance to the list returned by the Template's [IFrameTemplate.GetContainers](xref:DevExpress.ExpressApp.Templates.IFrameTemplate.GetContainers) method.

> [!Tip]
> If you have XAF sources installed, you can see how built-in Action Containers are implemented in the following locations:
> - [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Web\Templates\ActionContainers\
> - [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Win\Templates\ActionContainers\
> - [!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Blazor\Templates\

## API Reference

| API | Description |
|-|-|
| @DevExpress.ExpressApp.Actions.ActionBase.Category | Specifies the Action Container where XAF displays the current Action. |
| @DevExpress.ExpressApp.Editors.ListEditor.ContextMenuTemplate | Offers access to a List Editor's Context Menu Template. |
| @DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions | Fires when Actions are added to the Action Containers. |
