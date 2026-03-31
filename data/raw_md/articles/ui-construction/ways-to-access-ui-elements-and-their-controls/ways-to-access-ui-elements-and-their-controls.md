---
uid: "120092"
title: Ways to Access UI Elements and Their Controls
seealso: []
---
# Ways to Access UI Elements and Their Controls

This topic describes how to access UI elements such as [Actions](xref:112622), [View Items](xref:112612), [List Editors](xref:113189), [Property Editors](xref:113097), and their underlying controls.

Create a custom [](xref:DevExpress.ExpressApp.ViewController) descendant (or a generic [](xref:DevExpress.ExpressApp.ViewController`1) or [](xref:DevExpress.ExpressApp.ObjectViewController`2)) and implement a solution from one of the following sections:
* [Tasks with View Items and Property Editors](#tasks-with-view-items-and-property-editors)
* [Tasks with List Editors](#tasks-with-list-editors)
* [Tasks with Complex View Items](#tasks-with-complex-view-items)
* [Tasks with Actions](#tasks-with-actions)

To access a Detail View in @DevExpress.ExpressApp.ListView.MasterDetailMode, use the @DevExpress.ExpressApp.ListView.EditView property.

## Tasks with View Items and Property Editors

### Get the ViewItem or Property Editor object

Use the [CompositeView.FindItem(String)](xref:DevExpress.ExpressApp.CompositeView.FindItem(System.String)) method in the overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler. The View Item's name should match the corresponding **Views** | **CompositeView** | **Items** | **ViewItem** Model node's **ID** property. The default Property Editor's ID matches the [property name](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyName).

**Examples**: [](xref:117454) | [](xref:118348)

### Get View's ViewItem objects collection

Use the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) property in the overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler.

### Get all ViewItem objects of a specific type

Use the [CompositeView.GetItems\<T>](xref:DevExpress.ExpressApp.CompositeView.GetItems``1) method overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler.

### Access a custom View Item

To access a custom View Item inside a custom ViewController, use the following `CustomizeViewItemControl` methods:

* @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem}) and its overloads for Detail Views
* @DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem}) and its overloads for Dashboard Views
* @DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem},System.String[]) for Detail Views, Dashboard Views, and List Views in ASP.NET Core Blazor applications

**Examples**: [](xref:113104) | [](xref:402153) | [](xref:402188) | [](xref:403870) | [Add a Custom Button to a Property Editor (ASP.NET Core Blazor)](xref:405839)

### Access an embedded or nested View's View Item

Use the [NestedFrame.ViewItem](xref:DevExpress.ExpressApp.NestedFrame.ViewItem) property in the overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler.

**Examples**: [](xref:112912) | [](xref:113161)

### Customize a control of a Property Editor used both in a List and Detail View globally

Create a Property Editor's descendant and customize it. Apply the custom Property Editor to target properties in Model Editor. You can also use this Property Editor for all properties of a specific type.

**Examples**: How to: Customize a Built-in Property Editor ([ASP.NET Core Blazor](xref:402188) | [WinForms](xref:113104)) 

### Access a ViewItem's parent View

Use the [ViewItem.View](xref:DevExpress.ExpressApp.Editors.ViewItem.View) property overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler.

### Access the Layout Control and its items

If you want to customize layout elements that include `ListPropertyEditor`s (for example, change a caption or options of a parent tab group or page control), use techniques demonstrated in the following learning materials:

* [](xref:404428) (help topic)
* [XAF - How to show the number of nested List View items in tab captions](https://github.com/DevExpress-Examples/xaf-how-to-show-the-number-of-nested-list-views-items-in-tab-captions) (example) 

## Tasks with List Editors

### Get the ListEditor object

Use the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) property in the overridden `ViewController.OnActivated` virtual method (recommended) or the [ViewController.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler.

**Example**: [](xref:402154)

### Access a List Editor's underlying control

XAF includes various [platform-specific List Editors](xref:113189). Each editor has properties, methods, and events to access an editor's control such as [ListEditor.Control](xref:DevExpress.ExpressApp.Editors.ListEditor.Control). Use the overridden `ViewController.OnViewControlsCreated` virtual method (recommended) or the [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) | [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) event handler.

**Examples**:
- [View.CustomizeViewItemControl](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem})) (ASP.NET Core Blazor)
- [How to add an unbound column to GridListEditor](https://github.com/DevExpress-Examples/XAF-how-to-add-an-unbound-column-to-gridlisteditor-to-execute-a-custom-action-for-a-record) (Windows Forms)

### Access a List Editor's data cell control

A List Editor can instantiate an internal Property Editor to propagate settings to underlying data cell controls in view and edit modes. Use List Editor's members or customize its underlying control directly as described in the control's documentation. If you want to customize a control globally for List and Detail Views, refer to the [Customize a control of a Property Editor used both in a List and Detail View globally](#customize-a-control-of-a-property-editor-used-both-in-a-list-and-detail-view-globally) section.

**Examples**: [How to add an unbound column to GridListEditor](https://github.com/DevExpress-Examples/XAF-how-to-add-an-unbound-column-to-gridlisteditor-to-execute-a-custom-action-for-a-record) (WinForms)

### Access a Control in Tree List Editors

[!include[access-control-tree-list-editor](~/templates/access-control-tree-list-editor.md)]

### Access a Scheduler Control in Code

> [!NOTE]
> For more information about accessing the Scheduler control, refer to the following topic: [](xref:404610).

## Tasks with Complex View Items

### Access a control of an Action included in a Detail View layout

To access an @DevExpress.ExpressApp.Editors.ActionContainerViewItem's control, follow the directions from the [](xref:112816) topic.

### Access a ListPropertyEditor's control (inside a NestedFrame's List View)

1. Use the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[]) method to access `ListPropertyEditor`'s control and its nested List View.
2. Handle the underlying List View's [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) event. The additional event subscription may be required for complex View Items (like `ListPropertyEditor`, `DetailPropertyEditor`, `DashboardViewItem`), those control is a NestedFrame's template and embeds a nested View with own controls.
3. In the event handler, use [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) to get this Editor's methods or properties (for example, [GridListEditor.GridView](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView)) to access a control.

    The following snippet enables appearance customization for even grid rows in the nested List View:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Win.Editors;
    using DevExpress.XtraGrid.Views.Grid;
    using MainDemo.Module.BusinessObjects;

    namespace MainDemo.Win.Controllers;

    public class MyViewController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<ListPropertyEditor>(this, listPropertyEditor  => {
                listPropertyEditor.ListView.ControlsCreated += (s, e) => {
                    if (listPropertyEditor.ListView.Editor is GridListEditor gridListEditor) {
                        GridView gridView = gridListEditor.GridView;
                        gridView.OptionsView.EnableAppearanceEvenRow = true;
                    }
                };
            }, nameof(Employee.Tasks));
        }
    }
    ```

### Access a DetailPropertyEditor's or DashboardViewItem's control

1. Use the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[]) method to access `DetailPropertyEditor` and the @DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem})  method to access `DashboardViewItem` controls.
2. In the event handler, use the `DetailPropertyEditor`'s or `DashboardViewItem`'s `Frame` property to access the NestedFrame object and its template control.
3. Handle the `DetailPropertyEditor`'s or `DashboardViewItem`'s [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) event.

   The following code snippet hides the actions toolbar for the `Address1` Detail Property Editor of the `Employee` object when it is displayed in a nested frame:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Editors;
    using DevExpress.ExpressApp.Templates;
    using MainDemo.Module.BusinessObjects;

    public class MyViewController : ObjectViewController<DetailView, Employee>  {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<DetailPropertyEditor>(this, detailPropertyEditor => {
            if (detailPropertyEditor.Frame is NestedFrame nestedFrame
                && nestedFrame.Template is ISupportActionsToolbarVisibility template) {
                    template.SetVisible(false);
                    // NOTE: `template`, `detailPropertyEditor.Control`,
                    // and `nestedFrame.ViewItem.Control` refer to the same template control.
                }
            }, nameof(Employee.Address1));
        }
    }
    ```

## Tasks with Actions

### Access an Action

Use the [Frame.GetController\<ControllerType>()](xref:DevExpress.ExpressApp.Frame.GetController``1) method to get the Action's Controller and the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property to get the Action from this Controller. Refer to the following help topic to determine an Action identifier: [Determine an Action's Controller and Identifier](xref:113484).

**Example**: [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions)

[!include[platform-specific-events-control-customization](~/templates/platform-specific-events-control-customization.md)]

## Application Model-Specific Customizations

If you customize an existing control's [Application Model](xref:112580) options, this customization does not affect the control until its next creation. Customize the control or its corresponding Application Model options before XAF creates and renders the control. For more information, refer to the following topic: [](xref:112810).

## Familiarize Yourself with Underlying non-XAF Components First

- Note that XAF uses DevExpress WinForms, ASP.NET WebForms, ASP.NET Core Blazor, DevExtreme components for each corresponding platform.
- Research standard solutions for non-XAF components within DevExpress documentation, demos, code examples, and knowledge base articles. Feel free to use [our search engine](https://search.devexpress.com/) or Google. You have a higher chance to locate solutions in the component section of the DevExpress help system/docs than within XAF learning materials (that only describe XAF-related concepts).
- If your case is not covered by DevExpress component learning materials, submit questions to the corresponding DevExpress Support Team.