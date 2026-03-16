---
uid: "113564"
title: Criteria Properties
seealso:
- linkId: 402956
  altText: Localize Reports and Filter Editor in ASP.NET Core Blazor Applications
- linkId: "402188"
---
# Criteria Properties

When you build an XAF application, you may need a property that stores filter criteria (an expression that follows [Criteria Language Syntax](xref:4928)). You can display such properties using the following editors:

* A Filter Builder control
* An editor that allows users to type criteria and display a Filter Builder in a popup (refer to the sections below)
 
> [!NOTE]
> To see an example of how to use Criteria Property Editors, refer to the following topic: [How to: Use Criteria Property Editors](xref:113143).
> 
> To see Criteria Property Editors in action, refer to the **Property Editors** | **Criteria Properties** section in the **Feature Center** demo installed with XAF. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Examples

* [Criteria Properties in XPO](xref:113565)
* [Criteria Properties in EF Core](xref:113578)
* [How to use Criteria Property Editors](https://github.com/DevExpress-Examples/xaf-how-to-use-criteria-property-editors)

## ASP.NET Core Blazor

XAF's ASP.NET Core Blazor UI supports multiple Property Editors that work with filter criteria.

> [!NOTE]
> Apply @DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute to properties that store filter criteria. XAF generates **FilterPropertyEditor** controls for such properties. If necessary, you can change the editor type. See available options below. 

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

### FilterPropertyEditor

![|XAF ASP.NET Core Blazor Filter Property Editor|](~/images/filter-property-editor-blazor-devexpress.png)

Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.FilterEditorModel`.

Component: `DevExpress.ExpressApp.Blazor.Components.FilterEditor`. This internal component initializes and configures the JavaScript [Filter Editor](xref:113888). It does not have public API.

The default Property Editor with tree-like and text-based criteria construction.

### PopupFilterPropertyEditor

![XAF ASP.NET Core Blazor Popup Filter Property Editor](~/images/popup-filter-property-editor-blazor-devexpress.png)

Component Model: `DevExpress.ExpressApp.Blazor.Components.Models.DxTextBoxModel`.

Component: [](xref:DevExpress.Blazor.DxTextBox) shipped with the DevExpress ASP.NET Core Blazor Library.

A Property Editor for string properties that store filter criteria. It creates a pop-up Detail View with a `FilterPropertyEditor` item.

To access the `FilterPropertyEditor` in the pop-up Detail View, implement a View Controller for the `DevExpress.ExpressApp.Editors.CriteriaProvider` type. For more information on how to access a Property Editor in a Detail View, refer to the following topic: [](xref:402153).

To enable this Property Editor, use either of the following techniques:

In the Model Editor
:   Specify it in the `PropertyEditorType` property of the required **BOModel** | **\<Class\>** | **OwnMembers** | **\<Member\>** node or **Views** | **\<DetailView\>** | **Items** | **\<PropertyEditor\>** node.

In code
:   Decorate the property with @DevExpress.Persistent.Base.EditorAliasAttribute and pass `EditorAliases.PopupCriteriaPropertyEditor` as the attribute's parameter.

### CriteriaPropertyEditor

![XAF ASP.NET Core Blazor Criteria Property Editor](~/images/xaf-blazor-criteria-property-editor.png)

Class: `DevExpress.ExpressApp.Blazor.Editors.CriteriaPropertyEditor`.

`CriteriaPropertyEditor` displays a text box and supports expression validation. Knowledge of [Criteria Language Syntax](xref:4928) is required to work with this Property Editor.

For information on how to enable this editor in your application, refer to the following topic: [How to specify an XAF Property Editor for properties and types](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute).

> ![IMPORTANT]
> **CriteriaPropertyEditor** based on @DevExpress.Blazor.DxFilterBuilder is currently available in a [Community Technology Preview (CTP)](https://www.devexpress.com/aboutus/pre-release.xml).

### Property Visibility Customization in Filter Editors

You can use the `FilterEditorModel.CustomizePropertyVisibility` delegate to control property visibility in filter editors. The following example hides key members in Filter Editors. The change applies to grids and `PopupFilterPropertyEditor` controls:

```csharp{12-15}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Editors;
using Microsoft.AspNetCore.Components;

namespace YourSolutionName.Blazor.Server.Controllers {
    public class KeyPropertyInFilterEditorController : ObjectViewController<DetailView, CriteriaProvider> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<FilterPropertyEditor>(this, editor => {
                editor.ComponentModel.CustomizePropertyVisibility =
                EventCallback.Factory.Create<CustomizePropertyVisibilityEventArgs>(this, (e) => {
                    if (e.MemberInfo.Owner.KeyMember == e.MemberInfo) {
                        e.Visible = false;
                    }
                });
            });
        }
    }
}
```

## Windows Forms

XAF's Windows Forms UI supports multiple Property Editors that work with filter criteria.

> [!NOTE]
> Apply @DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute to properties that store filter criteria. XAF generates **FilterPropertyEditor** controls for such properties. If necessary, you can change the editor type. See available options below.

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### AdvancedCriteriaPropertyEditor

![XAF Windows Forms Advanced Criteria Property Editor](~/images/xaf-winforms-advanced-criteria-property-editor.png)
	
Control: [DevExpress.DataAccess.UI.FilterEditorControl](xref:DevExpress.DataAccess.UI.FilterEditorControl).
	
Repository Item: None.
	
The default Property Editor with tree-like and text-based criteria construction.
	
To display `AdvancedCriteriaPropertyEditor` for criteria properties, set the static @DevExpress.XtraEditors.WindowsFormsSettings.UseAdvancedFilterEditorControl property value to @DevExpress.Utils.DefaultBoolean.True or @DevExpress.Utils.DefaultBoolean.Default.

### CriteriaPropertyEditor

![XAF Windows Forms Criteria Property Editor](~/images/xaf-winforms-criteria-property-editor.png)
	
Control: `DevExpress.XtraFilterEditor.FilterEditorControl`.
	
Repository Item: None.
	
This Property Editor displays a **Filter Builder** control with two tabs. The **Filter** tab allows users to construct conditions through an easy-to-use UI. The **Text** tab allows users to type the criteria.
	
To display `CriteriaPropertyEditor` for criteria properties, set the static @DevExpress.XtraEditors.WindowsFormsSettings.UseAdvancedFilterEditorControl property value to @DevExpress.Utils.DefaultBoolean.False.

### PopupCriteriaPropertyEditor

![XAF Windows Forms Pop-up Criteria Property Editor](~/images/xaf-winforms-popup-criteria-property-editor.png)
	
Control: `DevExpress.ExpressApp.Win.Editors.PopupCriteriaEdit`.
	
Repository Item: `RepositoryItemPopupCriteriaEdit`, a descendant of the [](xref:DevExpress.XtraEditors.Repository.RepositoryItemButtonEdit) repository item from the XtraEditors Library.
	
Use this Property Editor to display a `CriteriaPropertyEditor` in a separate window and thus save space on the Detail form.
	
To use this Property Editor, assign it to the `PropertyEditorType` property of the required **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node or [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node.
	
`PopupCriteriaPropertyEditor` creates a pop-up Detail View with the `CriteriaPropertyEditor` item that uses the `DevExpress.DataAccess.UI.FilterEditorControl` or `DevExpress.XtraFilterEditor.FilterEditorControl` component internally (depending on the static @DevExpress.XtraEditors.WindowsFormsSettings.UseAdvancedFilterEditorControl property value). Implement a View Controller for the Detail View of the `DevExpress.ExpressApp.Editors.CriteriaProvider` type and access the `CriteriaPropertyEditor.Control` property. Use the technique described in the following topic to do this: [](xref:402153).

## Syntax Limitations in ASP.NET Core Blazor and Windows Forms Criteria Property Editors

The tree-like criteria construction in Criteria Property Editors does not support advanced syntaxes, such as:
- [Function Criteria Operators](xref:113307)
- [Object Parameters](xref:113278)
- [Current Object Parameter in XPO applications](xref:113204)
- [Free Joins](xref:8130)

If a criteria should contain such elements, users can switch to the Text tab and type in the expression. XAF validates the expressions on the server side and applies the filter.