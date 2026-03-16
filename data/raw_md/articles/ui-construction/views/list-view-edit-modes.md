---
uid: "113249"
title: List View Edit Modes
seealso:
- linkId: "404203"
- linkId: "113296"
- linkId: DevExpress.ExpressApp.DefaultListViewOptionsAttribute.MasterDetailMode
- linkId: DevExpress.ExpressApp.MasterDetailMode
- linkId: DevExpress.ExpressApp.DefaultListViewOptionsAttribute
- linkId: DevExpress.ExpressApp.ListView.CreateCustomCurrentObjectDetailView
- linkId: DevExpress.ExpressApp.ListView.CurrentObject
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-prevent-a-detailview-from-being-shown-for-a-listview-record
  altText: 'GitHub Example: XAF - Prevent Showing a Detail View of a List View Object'
---
# List View Edit Modes

Default data editing UI in XAF applications involves two steps. You first locate a record in a List View. You can then open a Detail View with that record's data and make the changes. This general behavior is common to all supported UI platforms - WinForms and ASP.NET Core Blazor. 

This topic demonstrates a few ways to make data editing available in List Views. In that case, a user does not have to navigate to a separate Detail View.

## Common Functionality Available in WinForms and ASP.NET Core Blazor Applications

### In-place Editing

The following image illustrates an editable List View:

![XAF Inline Edit Mode, DevExpress](~/images/inlineedit_1116538.png)
In a WinForms XAF application, select a row and click a property cell to edit an existing object. Use the **New** action or the grid's **New Item Row** to add a new object.

In ASP.NET Core Blazor XAF applications, you can click the **Edit** button to edit an existing object and the **New** button to create a new object. You can find these buttons in a row or table header. You can also use the `InlineEditMode` option to enable a WinForms-like style of Batch editing (see below).

### Make a List View Editable

* Invoke the [Model Editor](xref:112582), expand the **Views** node, and navigate to the child node that corresponds to the desired List View.
* Set the [IModelView.AllowEdit](xref:DevExpress.ExpressApp.Model.IModelView.AllowEdit) property to `True`.
* To allow users to create new objects directly in the List View, set the [IModelListViewNewItemRow.NewItemRowPosition](xref:DevExpress.ExpressApp.SystemModule.IModelListViewNewItemRow.NewItemRowPosition) property to `Top` or `Bottom`. The New Item Row appears at the top or at the bottom of the List View, respectively.

    ![|XAF Model Editor Settings for Editable List View, DevExpress](~/images/xaf-blazor-editablelistview-modeleditorsettings-devexpress.png)

### Split Layout (The MasterDetailMode Property)

The _split layout_ allows you to display both the Detail and List Views in the same window. The Detail View displays the currently selected object's properties. The displayed content changes dynamically based on the object currently focused in the List View. The following images illustrate the split layout:

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Split Layout, DevExpress](~/images/splitlayoutblazor.png)
WinForms
:   ![XAF Windows Forms Split Layout, DevExpress](~/images/splitlayout116545.png)

To enable the split layout for a specific List View, follow the steps below:

* Invoke the [Model Editor](xref:112582), expand the **Views** node, and navigate to the child node that corresponds to the desired List View.
* Set the [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) property to `ListViewAndDetailView`.
* Navigate to the **SplitLayout** child node and set the [IModelSplitLayout.Direction](xref:DevExpress.ExpressApp.Model.IModelSplitLayout.Direction) property to `Horizontal` or `Vertical` to position the Detail View.

An object can have multiple Detail Views available. The [IModelListView.MasterDetailView](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailView) property allows you to specify the Detail View that corresponds to the object currently selected in the List View. If the `IModelListView.MasterDetailView` property is not specified, the List View uses the [IModelListView.DetailView](xref:DevExpress.ExpressApp.Model.IModelListView.DetailView) value. If both the `MasterDetailView` and `DetailView` properties are unspecified, the List View uses the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) value specified for the current object.

Note that in XAF Blazor applications, when `MasterDetailMode` is set to `ListViewAndDetailView`, in-place editing is disabled (the `IModelView.AllowEdit` option has no effect).

## ASP.NET Core Blazor-Specific Functionality

### In-place Editing Customization (The InlineEditMode Property)

You can use the [IModelListViewBlazor.InlineEditMode](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.InlineEditMode) property of a [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node to change the edit form type:

![|XAF ASP.NET Core Blazor Inline Edit Mode Settings in Model Editor, DevExpress](~/images/xaf-blazor-modeleditor-inlineeditmode-devexpress.png)

| InlineEditMode Value | Description | Screenshot |
|---|---|---|
| `Inline` | Cell values are edited in the [Inline Edit Row](xref:DevExpress.Blazor.DxGrid.EditMode#edit-row). | ![Standard Inline edit](~/images/blazor_inlineedit.png) |
| `Batch` | Uses [Cell Edit Mode](xref:DevExpress.Blazor.DxGrid.EditMode#edit-row) to edit multiple rows simultaneously. Use the **Save** Action to save modified values. Unsaved modified values are highlighted in the grid. The Grid component does not support this functionality when you use [Server Data Access Mode](xref:118450). | ![Standard Batch edit](~/images/blazor_batchedit.png) |
| `EditForm` | Cell values are edited in the [Edit Form](xref:DevExpress.Blazor.DxGrid.EditMode#edit-form-default). The data row where values are being edited is not displayed. | ![InlineEditMode_BlazorDifferentEditModes](~/images/blazor_editform.png) |
| `PopupEditForm` | Cell values are edited with the [Popup Edit Form](xref:DevExpress.Blazor.DxGrid.EditMode#popup-edit-form). | ![InlineEditMode_BlazorDifferentEditModes](~/images/blazor_popupeditform.png) |

### Commit Changes Automatically in Nested Views

[!include[blazor-listview-commit-changes](~/templates/blazor-listview-commit-changes.md)]

The code above forces the `ObjectSpace` associated with a nested List View to [commit changes](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) and save them in response to a click on the **Save** button when you in-place edit the *SomeBusinessObject* in the nested List View.

### Customize a Property Editor

When you use inline editing in a List Editor, you can customize Property Editors to change their appearance and subscribe to their events.

The following code snippet uses the `DxGridListEditorBase.CustomizeViewItemControl` method to customize the background for a `StringPropertyEditor`:

**File:** _CS\MySolution.Blazor.Server\Controllers\CustomizeInlinePropertyEditorController.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

public class CustomizeInlinePropertyEditorController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StringPropertyEditor>(this, item => {
            if (item.ComponentModel is DxTextBoxModel textBoxModel) {
                textBoxModel.CssClass += " background-orange";
            }
        });
    }
}
```

**File:** _MySolution.Blazor.Server\wwwroot\css\site.css_

```CSS
.background-orange {
    background-color: darkorange;
}
```

![BlazorInlineEditMode_CustomizeControl](~/images/BlazorInlineEditMode_CustomizeControl.png)

> [!TIP]
> For more information about CSS customization in XAF ASP.NET Core Blazor applications, refer to the following section [Customize UI Elements Using CSS](xref:403068#customize-ui-elements-using-css)

### Customize EditForm Template

You can customize a regular or pop-up edit form. To do this, specify the [GridModel.EditFormTemplate](xref:DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel.EditFormTemplate) as shown in the following code snippet:

**File:** _CS\MySolution.Blazor.Server\Controllers\EditFormGridController.cs_:
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public class EditFormGridController : ObjectViewController<ListView, CustomEditFormObject> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is DxGridListEditor gridListEditor) {
            gridListEditor.GridModel.EditFormTemplate = CustomEditFormTemplate.Create(gridListEditor.PropertyEditors);
        }
    }
}
```

**File:** _CS\MySolution.Blazor.Server\CustomEditFormTemplate.razor_:
```Razor
@using DevExpress.ExpressApp.Blazor.Editors
@inherits DxGridEditFormTemplateBase

<DxFormLayout>
    @foreach((string caption, RenderFragment fragment) in GetItems()) {
        <div>
            @caption:
            @fragment
        </div>
    }
</DxFormLayout>
@CreateSaveCancelButtons()

@code {
    public static new RenderFragment<GridEditFormTemplateContext> Create(IEnumerable<BlazorPropertyEditorBase> propertyEditors) =>
        (GridEditFormTemplateContext context) =>
            @<CustomEditFormTemplate Context="@context" PropertyEditors="@propertyEditors" />;
}
```

### Set List And Detail View Size in Split Layout

In split layout mode, the List View and Detail View have equal sizes. Use either of the following techniques to change this behavior:

- Drag the splitter to a new position at runtime. XAF saves this position in the @DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition property for the current view. To persist these changes for individual users in the database, set up a user model difference store as described in the following topic: [Store Application Model Differences in the Database](xref:113698).
- Specify the [IModelSplitLayout.SplitterPosition](xref:DevExpress.ExpressApp.Model.IModelSplitLayout.SplitterPosition) property to set the size of the view [displayed first](xref:DevExpress.ExpressApp.Model.IModelListViewSplitLayout.ViewsOrder) in pixels.
- Specify the [IModelSplitLayout.RelativePosition](xref:DevExpress.ExpressApp.Model.IModelSplitLayout.RelativePosition) property to set the size of the view [displayed first](xref:DevExpress.ExpressApp.Model.IModelListViewSplitLayout.ViewsOrder) as a percentage.

## WinForms-Specific Functionality

### Commit Changes Automatically

The WinForms application displays a confirmation dialog if a user focuses another element in the window after editing a cell in the in-place editor or the Detail View:

![InlineEdit_Confirmation](~/images/inlineedit_confirmation116543.png)

The changes made in an editable List View can be saved automatically without confirmation when you select another object in the View or focus another element in the window. Use [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) and [ModificationsController.ModificationsCheckingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsCheckingMode) properties to change this behavior for editable List Views.
