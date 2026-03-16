---
uid: "112617"
seealso:
- linkId: "113183"
- linkId: "113198"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-list-view-items-in-the-navigation-control
  altText: How to show the number of List View items in the Navigation Control
title: Access the Navigation Control
---
# Access the Navigation Control

This example shows how to access and customize the navigation control. Since customizations affect only the UI and do not depend on the current [View](xref:112611) or data, you need to create a [Window Controller](xref:112621). For more information on the navigation system, refer to the following topic: [Navigation System](xref:113198).

## WinForms Controller

Add a new Window Controller to the [WinForms application project](xref:118045) (_MySolution.Win_). Override the Controller's protected `OnActivated` method, subscribe to the [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event, and customize the navigation control in the event handler:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.XtraBars.Navigation;
using DevExpress.XtraNavBar;
using DevExpress.XtraTreeList;
// ...
public class WinCustomizeNavigationController : WindowController {
    public WinCustomizeNavigationController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction.CustomizeControl += 
            ShowNavigationItemAction_CustomizeControl;
    }
    private TreeList GetEmbeddedTreeList(NavBarGroupControlContainer container) {
        if(container != null && container.Controls.Count == 1) {
            return container.Controls[0] as TreeList;
        }
        return null;
    }
    private void CustomizeEmbeddedTreeList(NavGroupCollection groups) {
        foreach(NavBarGroup group in groups) {
            TreeList treeList = GetEmbeddedTreeList(group.ControlContainer);
            // Customize TreeList
        }
    }
    private void ShowNavigationItemAction_CustomizeControl(object sender, CustomizeControlEventArgs e) {
        if(e.Control is AccordionControl) {
            // Customize AccordionControl
        }
        else if(e.Control is NavBarControl) {
            // Customize NavBarControl
            CustomizeEmbeddedTreeList(((NavBarControl)e.Control).Groups);
        }
        else if(e.Control is TreeList) {
            // Customize TreeList in old templates and new templates with UseLightStyle set to false
        }
    }
    protected override void OnDeactivated() {
        Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction.CustomizeControl -= 
            ShowNavigationItemAction_CustomizeControl;
        base.OnDeactivated();
    }
}
```
***

## ASP.NET Core Blazor Controller

In XAF Blazor applications, you can use `DxTreeViewAdapter` or `DxAccordionAdapter` to customize the navigation control based on the selected [navigation style](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle). The both adapters expose the actual underlying component ([DxTreeView](xref:DevExpress.Blazor.DxTreeView) or [DxAccordion](xref:DevExpress.Blazor.DxAccordion)) and their [component models](xref:404767).

The following example demonstrates how to access the navigation component adapter and use it to expand all navigation items and hide the filter panel when the navigation menu is shown for the first time:

[!include[<MySolution.Blazor.Server\Controllers\BlazorCustomizeNavigationController.cs>](~/templates/platform_specific_file_path.md)]

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Components;
using DevExpress.ExpressApp.Blazor.Templates.Navigation;
using DevExpress.ExpressApp.Blazor.Templates.Navigation.ActionControls;
using DevExpress.ExpressApp.SystemModule;

public class BlazorCustomizeNavigationController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction
             .CustomizeControl += ShowNavigationItemAction_CustomizeControl;
    }

    protected override void OnDeactivated() {
        base.OnDeactivated();
        Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction
             .CustomizeControl -= ShowNavigationItemAction_CustomizeControl;
    }

    private void ShowNavigationItemAction_CustomizeControl(object? sender, CustomizeControlEventArgs e) {
        var navigationComponentAdapter = (e.Control as ShowNavigationItemActionControl)?.NavigationComponentAdapter;
        if(navigationComponentAdapter is DxTreeViewAdapter treeViewAdapter) {
            treeViewAdapter.ComponentModel.ShowFilterPanel = false;
            treeViewAdapter.ComponentCaptured += TreeViewAdapter_ComponentCaptured;
        }
        else if(navigationComponentAdapter is DxAccordionAdapter accordionAdapter) {
            accordionAdapter.ComponentModel.ShowFilterPanel = false;
            accordionAdapter.ComponentCaptured += AccordionAdapter_ComponentCaptured;
        }
    }

    private void TreeViewAdapter_ComponentCaptured(object? sender, ComponentCapturedEventArgs<DxTreeView> e) {
        e.Component.ExpandAll();
    }

    private void AccordionAdapter_ComponentCaptured(object? sender, ComponentCapturedEventArgs<DxAccordion> e) {
        e.Component.ExpandAll();
    }
}
```
