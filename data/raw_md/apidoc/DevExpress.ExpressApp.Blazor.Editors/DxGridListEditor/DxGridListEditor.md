---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor
name: DxGridListEditor
type: Class
summary: '[List Editor](xref:113189) that can be used in XAF ASP.NET Core Blazor applications to display [List Views](xref:112611) in a UI.'
syntax:
  content: 'public class DxGridListEditor : DxGridListEditorBase'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor._members
  altText: DxGridListEditor Members
---
List Views use **List Editors** to display object collections in a UI. The `DxGridListEditor` displays data in a table:

![DxGridListEditor OverView](~/images/blazor_dxgridlisteditor_overview.png)

To display object collections, the `DxGridListEditor` uses an instance of the [DxGrid](xref:DevExpress.Blazor.DxGrid) class.

Features include:

- Client and Server mode for XPO and EF Core
- Data editing
- Protected content placeholders for secured data rows
- Property editors as cell templates
- Grouping, sorting, and filtering
- Group and total summaries
- Save layout settings in the Application Model
- Selection API
- Context-dependent menu toolbar
- Conditional appearance for cells
- Column resizing
- Column chooser
- [ServerView, InstantFeedbackView, InstantFeedback](xref:118450), and [DataView](xref:118452) data access modes
- PDF export
- [Virtual scrolling](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled)

### Enable the DxGridListEditor

The `DxGridListEditor` is enabled by default for v22.1+ projects.

### DxGridListEditor in a Project Upgraded from Older Versions

If you updated your project from v21.2 or earlier, do the following:

1. Open the _MySolution\Blazor.Server\Model.xafml_ file. In the Model Editor, go to **ApplicationName | Views**. Set the `DefaultListEditor` property to `DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor`.

    ![enable dxgridlisteditor in model editor](~/images/enable-dxgridlisteditor-in-model-editor.png)

2. If you enabled the `DxGridListEditor` manually in v21.2, remove the corresponding code from your application. To see this code, use the selector at the top of this page to switch to the **V21.2** documentation version.

3. If you edited `DxGridListEditor` model properties, update your code according to the following tutorial: [](xref:402154).

### Limitations

* `DxGridListEditor` does not support [Batch Edit](xref:113249#in-place-editing-customization-the-inlineeditmode-property) in [Server](xref:118450) data access mode.
* `DxGridListEditor` does not support [Queryable](xref:402925) data access mode.