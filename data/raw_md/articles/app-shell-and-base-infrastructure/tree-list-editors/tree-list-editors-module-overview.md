---
uid: "112836"
title: TreeList Editors Module Overview
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-use-tree-list-editors-to-display-list-views
  altText: 'GitHub Example: XAF - How to Use Tree List Editors to Display List Views For ASP.NET Core Blazor And Windows Forms'
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-win-enable-inplace-editing-in-tree-list-view
  altText: 'GitHub Example: XAF WinForms - How to enable in-place editing in the tree List View (TreeListEditor)'
---
# TreeList Editors Module Overview

The **TreeList Editors** module displays [List View](xref:112611) information in a tree-like structure (a TreeList control). Tree List controls allow you to sort data values against multiple columns, calculate summary values, display node preview and node images, customize column layout at runtime, format column and summary values, and use advanced editors to display and edit cell values.

This topic explains how to use the TreeList Editors module.

## TreeList Module Components

### Modules and Integrated DevExpress Controls

| Platform | Module | Editor | Control |
| -------- | ------ | ------ | ------- | 
| ASP.NET Core Blazor | @DevExpress.ExpressApp.Blazor | @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor | [Blazor.DxTreeList](xref:DevExpress.Blazor.DxTreeList) |
| Windows Forms | [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditorsWindowsFormsModule) | [Win.TreeListEditor](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor) | [XtraTreeList.TreeList](xref:DevExpress.XtraTreeList.TreeList) | 
| Platform-agnostic |  @DevExpress.ExpressApp.TreeListEditors.TreeListEditorsModuleBase<br/>(only for Windows Forms) | | |

XAF targets [List Editors](xref:113189) mentioned in the table for objects that implement the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface from the [Business Class Library](xref:112571).

In Windows Forms applications, the **TreeList Editors** module supports a categorized tree view where tree nodes are categories by related items. For this purpose, XAF supplies the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor) for category items that are objects that implement the [](xref:DevExpress.Persistent.Base.General.ICategorizedItem) interface.

ASP.NET Core Blazor @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor supports [flat data](#flat-data-structure) sources and allows you to display objects in a hierarchical structure with Key Field - Parent Key Field relationships.

## Add the TreeList Editors Module to Your Application

### Template Kit

You can add the TreeList Editors module to your application when you use the [Template Kit](xref:405447) to create a new XAF solution. Select the **Tree List Editors** module in the **Additional Modules** section.

### Windows Forms

[!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.TreeListEditorsApplicationBuilderExtensions.AddTreeListEditors(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditorOptions})>,<WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

### ASP.NET Core Blazor

[!include[template-how-to-implement-tree-list-editor-example](~/templates/template-how-to-implement-tree-list-editor-example.md)]

## Organize a Tree

### Tree-like Data Structure with ITreeNode Objects

To display data in a tree-like structure in the UI, implement the `ITreeNode` interface in the required business classes.

# [C#](#tab/tabid-csharp)

```csharp
public interface ITreeNode {
   string Name { get; }
   ITreeNode Parent { get; }
   IBindingList Children { get; }
}
```
***

The [ITreeNode.Name](xref:DevExpress.Persistent.Base.General.ITreeNode.Name) property specifies a tree node caption. The [ITreeNode.Parent](xref:DevExpress.Persistent.Base.General.ITreeNode.Parent) property refers to the parent object (tree node). If this property is set to `null`, the object is the root object (root tree node). The [ITreeNode.Children](xref:DevExpress.Persistent.Base.General.ITreeNode.Children) property is a collection of child objects (child tree nodes).

For an example of the `ITreeNode` interface implementation, refer to the following topic: [Display a Tree List using the ITreeNode Interface](xref:112837).

The [Business Class Library](xref:112571) supplies the `HCategory` class that implements the `ITreeNode` interface. You can use it as is, or inherit from it, instead of implementing the `ITreeNode` interface from scratch. For details, refer to the [Display a Tree List using the HCategory Class](xref:112839) topic. To see the `HCategory` class implementation, refer to the following folders:

* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]Xpo_
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]EFCore_

You can find the _HCategory.cs_ file in these folders.

> [!NOTE]
> The `TreeListEditor` and `CategorizedListEditor` cannot properly display a tree if the hierarchy contains objects that are not assignable from the List View object type (see [Type.IsAssignableFrom](https://learn.microsoft.com/en-us/dotnet/api/system.type.isassignablefrom#System_Type_IsAssignableFrom_System_Type_)).

When you add the TreeList Editors module to the application, XAF uses Tree List Editors to display all List Views associated with `ITreeNode` objects. Editors build root nodes from List View objects where the [ITreeNode.Parent](xref:DevExpress.Persistent.Base.General.ITreeNode.Parent) property is set to `null`. When you expand a node, the editor looks for List View objects contained in the node's [ITreeNode.Children](xref:DevExpress.Persistent.Base.General.ITreeNode.Children) collection. The editor then displays the found objects as child nodes. The following images show XAF Tree List editors:

#### DxTreeListEditor

![XAF ASP.NET Core Blazor Tree List Editor, DevExpress](~/images/xaf-blazor-treelist-editor-devexpress.png)

#### TreeListEditor

![XAF ASP.NET Windows Forms Tree List Editor, DevExpress](~/images/treelisteditorsmodule_runtimewin117299.png)

### Flat Data Structure

XAF ASP.NET Core Blazor @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor supports flat data.

#### How to Implement Flat Data Structure

To build a hierarchical tree from flat data, specify properties that define node relationships:

@DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.KeyFieldName
:   A field name that contains a node's unique identifier.

@DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.ParentKeyFieldName
:   A field name that contains a parent node identifier.

#### Performance Optimization

In [Queryable](xref:402925) data access mode, flat data offers significant advantages over ITreeNode implementation.

**Performance benefits:**
- **Faster initial loading** - Loads only root objects instead of the entire hierarchy
- **On-demand child loading** - Child nodes are loaded only when parents are expanded, reducing memory use
- **Better database performance** - Simple foreign key relationships outperform complex collections
- **Optimized for large datasets** - Better performance with multiple records

**Simplicity benefits:**
- **No interface implementation** - Does not require `ITreeNode` interface implementation
- **Works with existing data** - Compatible with standard parent-child ID patterns in databases  
- **Simpler maintenance** - No need to manage bidirectional parent-child relationships

To use [Queryable](xref:402925) mode, specify an additional model property:

@DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.HasChildrenFieldName
:   Field that indicates whether a node has children. The TreeList component uses it to display expand buttons for those nodes.

> [!NOTE]
> If you make this property persistent, only visible nodes are queried from the database initially. If this property is calculated, XAF loads the next level to allow the Tree List to evaluate whether nodes have children.

In [Client](xref:118449) data access mode, a Tree List loads all objects.

## Support Node Images

To support node images, implement the [](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider) interface in a class that implements the `ITreeNode` interface. As a result, each node should be accompanied by an image.

![ITreeNodeImageProvider](~/images/itreenodeimageprovider116370.png)

> [!NOTE]
> XAF ASP.NET Core Blazor applications do not support [](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider).

The `ITreeNodeImageProvider` declares a single member - the [ITreeNodeImageProvider.GetImage](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider.GetImage(System.String@)) method. Return the image corresponding to a tree node using this member.

To see an example of the `ITreeNodeImageProvider` interface implementation, refer to the following topic: [Node Images in a Tree List](xref:113215).

## Implement the Category-Items Scenario (Windows Forms)

In most scenarios, a tree node is a category that can have related items. The following business model can be implemented in terms of the Category-Items scenario. The root category is represented by objects of the ProjectGroup class (".Net", "VCL", …). This category's child category is represented by Project type objects ("XtraGrid", "XtraEditors", "QuantumGrid", …). There may be more levels in this hierarchy. For example, each Project can contain a list of its own Areas: "Columns", "RepositoryItems", "MaskEdit", etc. These objects should implement the `ITreeNode` interface to be displayed as a tree. At the same time, there can be `Issue` objects related to specific categories (to a ProjectGroup, Project or ProjectArea). Each category is related to `Issue` objects by the One-to-Many relationship. When displaying the `Issue` List View, you may need to see a tree of categories and a list of `Issue` objects related to the currently selected category, as shown in the image below.

![CategorizedListEditor](~/images/categorizedlisteditor115620.png)

This image demonstrates how the Windows Forms `CategorizedListEditor` displays the `Issue` List View. The TreeList Editors module supplies this List Editor for the scenarios, as defined above. It displays List Views associated with objects of the `ICategorizedItem` type, so the `Issue` class from the example above should implement the `ICategorizedItem` interface.

# [C#](#tab/tabid-csharp)

```csharp
public interface ICategorizedItem {
   ITreeNode Category { get; set; }
}
```
***

For more information, refer to the following topic: [Categorized List](xref:112838).

It is not necessary to display Issue List Views using the `CategorizedListEditor`. For example, you can use an ordinary [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) for nested Issue List Views:

1. Invoke the [Model Editor](xref:112582) for the Windows Forms application project.
2. Right-click the **Views** node and select **Add…** | **ListView** in the invoked context menu.
	
	![AddListViewNode](~/images/addlistviewnode117298.png)

3. For the newly created node, specify the `Id` property and set the `ModelClass` property to the type that implements the `ICategorizedItem` interface (for example, `Issue`).
4. Right-click the new node and choose **Generate content**.
5. Navigate to the Detail View node that defines the Detail View with a collection of `ICategorizedItem` objects (for example, `ProjectArea`).
6. Locate the child View Item node that corresponds to this collection. Set its `View` property to the node that you created with the previous steps.

    ![CategorizedListEditor_GridListEditor](~/images/categorizedlisteditor_gridlisteditor115621.png)

## Access a Control in Tree List Editors

[!include[access-control-tree-list-editor](~/templates/access-control-tree-list-editor.md)]

## Filtering a Tree List

List View Tree List controls - @DevExpress.Blazor.DxTreeList and [TreeList](xref:2434) - provide advanced filtering features. For example, the controls support filtering operators and can filter root and child objects. Follow the links below for more information:
* [DxTreeList Filtering](xref:405000) 
* [TreeList Filtering](xref:405003)  

The following resource uses these features in XAF applications:

* The **List Editors | Tree | Filtering** section in the **Feature Center** demo (_[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_) or the [Feature Center demo online](https://demos.devexpress.com/XAF/FeatureCenter/TreeListEditorFilterDemoObject_ListView/)

### Collapse/Expand Tree List Nodes

The following code snippet uses `ExpandAll` or `CollapseAll` methods of the [Blazor.DxTreeList](xref:DevExpress.Blazor.DxTreeList) component to expand or collapse all Tree List nodes:

```csharp
public partial class DXItem : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxTreeListEditor editor) {
            editor.TreeListModel.ComponentInstanceCaptured += (s, e) => {
                // Expand all nodes.
                e.ComponentInstance.ExpandAll();
                // Collapse all nodes.
                e.ComponentInstance.CollapseAll();
            };
        }
    }
}
```