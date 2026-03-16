---
uid: DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor
name: DxTreeListEditor
type: Class
summary: A List Editor you can use in XAF ASP.NET Core Blazor applications to display data as a tree-like structure.
syntax:
  content: 'public class DxTreeListEditor : DxGridListEditorBase'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor._members
  altText: DxTreeListEditor Members
- linkId: "112836"
- linkId: "405312"
- linkId: "112839"
- linkId: "112837"
---

List Views use List Editors to display object collections. `DxTreeListEditor` is a List Editor that displays data in the form of a tree. This editor is implemented in the [TreeList Editors](xref:112836) module.

![XAF ASP.NET Core Blazor Tree List Editor, DevExpress](~/images/xaf-blazor-treelist-editor-devexpress.png)

To display tree-like collections, the `DxTreeListEditor` uses an instance of the @DevExpress.Blazor.DxTreeList class. It supports the following features:

* [Client](xref:118449) and [Queryable](xref:402925) mode. [Queryable](xref:402925) mode is available for [flat data](xref:112836#flat-data-structure) only.
* Tree-like structure in the UI for `ITreeNode` objects
* Tree-like structure for [flat data](xref:112836#flat-data-structure) objects with "Key - Parent Key" relationship 
* Data editing
* Protected content placeholders for secured data rows
* [Loading child nodes on demand](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.LoadChildrenOnDemand)
* Property editors as cell templates
* Sorting and filtering
* Summaries
* Saving layout settings in the Application Model
* [Selection API](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.TreeListSelectionColumnModel)
* Context-dependent menu toolbar
* Conditional appearance for cells
* Column resizing
* Column chooser
* PDF export

> [!NOTE]
> `DxTreeListEditor` does not support the following features:
> 
> * Server, ServerView, InstantFeedback, InstantFeedbackView, and DataView modes
> * Best fit column width
> * Node images for `ITreeNode` objects

`DxTreeListEditor` is available out of the box in XAF projects for objects that implement the `ITreeNode` interface. To enable it for flat data objects, specify the `DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor` list editor type in the `IModelListView.EditorType` model option.

For an example, refer to the `Departments` List View in the [XAF ASP.NET Core Blazor demo](https://demos.devexpress.com/XAF/BlazorMainDemo).
