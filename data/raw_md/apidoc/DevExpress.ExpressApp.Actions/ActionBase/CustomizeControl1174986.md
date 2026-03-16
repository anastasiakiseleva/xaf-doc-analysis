---
uid: DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl
name: CustomizeControl
type: Event
summary: Fires after the control is initialized. Allows you to customize the control.
syntax:
  content: public event EventHandler<CustomizeControlEventArgs> CustomizeControl
seealso:
- linkId: "113183"
- linkId: "112617"
---
The following code snippet changes the @DevExpress.ExpressApp.Actions.SimpleAction's color in a WinForm application. To run this code, add the _DevExpress.ExpressApp.XtraBars.v<:xx.x:>.dll_ assembly to `References`.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.XtraBars;
// ...
public class ChangeActionColorController : WindowController {
    public ChangeActionColorController() {
        SimpleAction simpleAction = new SimpleAction(this, "Action", PredefinedCategory.Edit);
        simpleAction.CustomizeControl += SimpleAction_CustomizeControl;
    }
    private void SimpleAction_CustomizeControl(object sender, CustomizeControlEventArgs e) {
        BarButtonItem button = e.Control as BarButtonItem;
        if(button != null) {
            button.ItemAppearance.Normal.BackColor = Color.LightBlue;
        }
    }
}

```
***

Do not handle this event for a [built-in Action](xref:113016) in a [View or Window Controller](xref:112621)'s `OnActivated` method because this method is called after the Action control is created - call the `OnFrameAssigned` method instead.

The [CustomizeControlEventArgs.Control](xref:DevExpress.ExpressApp.Actions.CustomizeControlEventArgs.Control) event parameter returns the Action Item object that contains control settings.

[!demo[Actions - Simple Action](https://demos.devexpress.com/XAF/FeatureCenter/SimpleActionRootObject_DetailView/?mode=Edit)]

### WinForms Specific Scenarios

#### Simple Actions

If you customize a @DevExpress.ExpressApp.Actions.SimpleAction, the `e.Control` argument can return the following types:

* [](xref:DevExpress.XtraEditors.SimpleButton) for Layout Actions
* [](xref:DevExpress.XtraBars.BarButtonItem) for BarManager Actions

# [C#](#tab/tabid-csharp)
```csharp
myAction.CustomizeControl += (s, e) => {
    SimpleButton control = e.Control as SimpleButton;
    // or
    BarButtonItem control = e.Control as BarButtonItem;
    //...
}
```
***

#### Single Choice Actions

If you customize a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), the `e.Control` argument can return the following types:
* [](xref:DevExpress.XtraEditors.ImageComboBoxEdit) for Layout Actions
* [](xref:DevExpress.XtraBars.BarEditItem), [](xref:DevExpress.XtraBars.BarButtonItem), [](xref:DevExpress.XtraBars.RibbonGalleryBarItem) for BarManager Actions

# [C#](#tab/tabid-csharp)
```csharp
myAction.CustomizeControl += (s, e) => {
    ImageComboBoxEdit control = e.Control as ImageComboBoxEdit;
    // or
    BarEditItem control = e.Control as BarEditItem;
    //...
}
```
***

#### ShowNavigationItem Actions

If you customize a [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction), the `e.Control` argument can return the following types:
* [](xref:DevExpress.XtraNavBar.NavBarControl) if the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property value is [NavigationStyle.NavBar](xref:DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle.NavBar)
* [](xref:DevExpress.XtraTreeList.TreeList) if the `IModelRootNavigationItems.NavigationStyle` property is [NavigationStyle.TreeList](xref:DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle.TreeList)

# [C#](#tab/tabid-csharp)
```csharp
Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction.CustomizeControl += (s, e) => {
    NavBarControl navBar = e.Control as NavBarControl;
    // or
    TreeList treeList = e.Control as TreeList;
    //...
}
```
***

#### Parametrized Actions

If you customize a [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), the `e.Control` argument can return the following types:
* [](xref:DevExpress.XtraEditors.ButtonEdit) descendants ([](xref:DevExpress.XtraEditors.SpinEdit), `ButtonEditWithClearButton`, and [](xref:DevExpress.XtraEditors.DateEdit)) for Layout Actions
* [](xref:DevExpress.XtraBars.BarEditItem) for BarManager Actions

# [C#](#tab/tabid-csharp)
```csharp
myAction.CustomizeControl += (s, e) => {
    DateEdit control = e.Control as DateEdit;
    // or
    BarEditItem control = e.Control as BarEditItem;
    //...
}
```
***

#### PopupWindowShow Actions

If you customize a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction), the `e.Control` argument can return the following types:
* [](xref:DevExpress.XtraEditors.SimpleButton) for Layout Actions
* [](xref:DevExpress.XtraBars.BarButtonItem) for BarManager Actions

# [C#](#tab/tabid-csharp)
```csharp
myAction.CustomizeControl += (s, e) => {
    SimpleButton control = e.Control as SimpleButton;
    // or
    BarButtonItem control = e.Control as BarButtonItem;
    //...
}
```
***


### ASP.NET Core Blazor Specific Scenarios

For detailed information on how to add Actions to Context Menu or Command Column of a List View grid, refer to the following topic: [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category#how-to-add-an-action-to-a-context-menu-or-command-column).

#### Simple and PopupWindowShow Actions 

If you customize a @DevExpress.ExpressApp.Actions.SimpleAction or a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction), the `e.Control` argument can return the following types:
* `DxToolbarItemSimpleActionControl` for Toolbar Actions
* `DxRibbonItemSimpleActionControl` for Ribbon Actions
* `DxContextMenuItemSimpleActionControl` for DxGrid Context Menu Actions
* `ListEditorInlineActionControl` for DxGrid Inline Actions

```csharp
myAction.CustomizeControl += (s, e) => {
    DxToolbarItemSimpleActionControl actionControl = e.Control as DxToolbarItemSimpleActionControl;
    // or
    DxRibbonItemSimpleActionControl actionControl = e.Control as DxRibbonItemSimpleActionControl;
    // or
    DxContextMenuItemSimpleActionControl actionControl = e.Control as DxContextMenuItemSimpleActionControl;  
    // or
    ListEditorInlineActionControl actionControl = e.Control as ListEditorInlineActionControl;  
    //...
}
```

For information on how to customize an Inline Action in a DxGrid row, refer to the following topic: [Customize Inline Action Control (ASP.NET Core Blazor)](xref:404559#customize-inline-action-control).

#### Single Choice Actions

If you customize a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), the `e.Control` argument can return the following types:
- `DxToolbarComboBoxItemSingleChoiceActionControl` for non-hierarchical Toolbar Actions with [SingleChoiceAction.ItemType.ItemIsMode](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType)
- `DxRibbonItemSingleChoiceActionControl` or `DxRibbonComboBoxItemSingleChoiceActionControl` for Ribbon Actions
- `DxToolbarItemSingleChoiceActionControl` for other Toolbar Actions
- `DxContextMenuItemSingleChoiceActionControl` for Context Menu Actions

```csharp
myAction.CustomizeControl += (s, e) => {
    DxToolbarComboBoxItemSingleChoiceActionControl actionControl = e.Control as DxToolbarComboBoxItemSingleChoiceActionControl;
    // or
    DxRibbonItemSingleChoiceActionControl actionControl = e.Control as DxRibbonItemSingleChoiceActionControl;
    // or
    DxToolbarItemSingleChoiceActionControl actionControl = e.Control as DxToolbarItemSingleChoiceActionControl;
    // or
    DxContextMenuItemSingleChoiceActionControl actionControl = e.Control as DxContextMenuItemSingleChoiceActionControl;  
    //...
}
```

#### Parametrized Actions

If you customize a [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), the `e.Control` argument returns a `DxToolbarItemParametrizedActionControl` or `DxRibbonItemParametrizedActionControl` object.

# [C#](#tab/tabid-csharp1)
```csharp
myAction.CustomizeControl += (s, e) => {
    DxToolbarItemParametrizedActionControl actionControl = e.Control as DxToolbarItemParametrizedActionControl;
    // or
    DxRibbonItemParametrizedActionControl actionControl = e.Control as DxRibbonItemParametrizedActionControl;
    //...
}
```
***

#### ShowNavigationItem Actions

If you customize a [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction), the `e.Control` argument returns a `ShowNavigationItemActionControl` object. You can use `ShowNavigationItemActionControl.NavigationComponentAdapter` to customize the navigation control. The following adapter types are available:
* [DxAccordionAdapter](xref:DevExpress.ExpressApp.Blazor.Templates.Navigation.DxAccordionAdapter) if the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property value is `Accordion` or `NavBar`
* [DxTreeViewAdapter](xref:DevExpress.ExpressApp.Blazor.Templates.Navigation.DxTreeViewAdapter) if the `IModelRootNavigationItems.NavigationStyle` property value is `TreeList`.

Both component adapter types have the following members:
* The `Component` property contains a reference to the underlying navigation control ([DxTreeView](xref:DevExpress.Blazor.DxTreeView) or [DxAccordion](xref:DevExpress.Blazor.DxAccordion)). Use this reference to expand or collapse navigation items.
* The `ComponentModel` property contains the [component model](xref:404767) that you can use to modify properties of the navigation control.
* The `ComponentCaptured` event fires when the `Component` property is initialized with a reference to a navigation control.

# [C#](#tab/tabid-csharp1)
```csharp
Frame.GetController<ShowNavigationItemController>().ShowNavigationItemAction.CustomizeControl += (s, e) => {
    var navigationComponentAdapter = (e.Control as ShowNavigationItemActionControl)?.NavigationComponentAdapter;
    if(navigationComponentAdapter is DxTreeViewAdapter treeViewAdapter) {
        // ...
    }
    else if(navigationComponentAdapter is DxAccordionAdapter accordionAdapter) {
        // ...
    }
}
```
***

Refer to the following topic for more information on how to access control properties: [How to: Access the Navigation Control](xref:112617#aspnet-core-blazor-controller).
