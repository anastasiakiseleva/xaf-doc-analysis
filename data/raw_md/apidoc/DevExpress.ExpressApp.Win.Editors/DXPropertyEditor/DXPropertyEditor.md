---
uid: DevExpress.ExpressApp.Win.Editors.DXPropertyEditor
name: DXPropertyEditor
type: Class
summary: A base class for Property Editors that use Developer Express Windows Forms controls.
syntax:
  content: 'public abstract class DXPropertyEditor : WinPropertyEditor, IInplaceEditSupport, IAppearanceFormat, IAppearanceBase'
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.DXPropertyEditor._members
  altText: DXPropertyEditor Members
- linkId: "113097"
- linkId: DevExpress.ExpressApp.Editors.PropertyEditorAttribute
---
Inherit from this class to implement a custom Property Editor using a control from the **XtraEditors** library. All the controls from this library support in-place editing. It is a mechanism that allows you to embed an editor into container controls. To support in-place editing, these editors have a Repository Item. This item stores properties and event handlers used to set up the editor. Repository Items can be created as stand-alone objects to embed editors of particular types into container controls. 
For details, see [Repositories and Repository Items](xref:114580).
The **XAF** utilizes this feature to provide the in-place editing functionality in the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) (the [List Editor](xref:113189) that uses **XtraGrid** control).

The simplest implementation of the **DXPropertyEditor** class' descendant requires a single step:

1. Override the **CreateControlCore** method. This method returns the Property Editor's control (see [How to: Implement a Property Editor Based on a Custom Control (WinForms)](xref:112679)). The following code snippet illustrates this:

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Win.Editors;
//...
[PropertyEditor(typeof(String), true)]
public class MyStringPropertyEditor : DXPropertyEditor {
    public MyStringPropertyEditor(Type objectType, IModelMemberViewItem model)
       : base(objectType, model) { }
    protected override object CreateControlCore() {
        StringEdit control = new StringEdit();            
        control.Properties.Appearance.ForeColor = Color.Coral;
        return control;
    }
}
```
***

The following image demonstrates a business object's property which is displayed via the implemented Property Editor in a Detail View:

![DXPropertyEditor1](~/images/dxpropertyeditor1116098.png)

In a List View, the column which displays the business object property is represented by a simple label, since the Repository Item is not created, by default:

![DXPropertyEditor2](~/images/dxpropertyeditor2116099.png)

The implemented Property Editor does not support in-place editing in the List Views that are represented by the **GridListEditor** List Editor. To implement the in-place editing support, two additional steps should be taken:

2.  Override the **CreateRepositoryItem** method. It is called by the **GridListEditor** List Editor to create a repository item for a column.

3.  Override the **SetupRepositoryItem** method. In this method, perform the customization of the control's settings, if needed. This method is called when creating an in-place editor for the GridListEditor's column. In addition, this method is called after a Property Editor has been created in a Detail View. So, the implemented customization will affect the controls created both in the Detail View and List View. It is necessary to call the base SetupRepositoryItem method in the overridden method to perform common control initialization. The following code snippet illustrates this:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraEditors.Repository;
//...
[PropertyEditor(typeof(String), true)]
public class MyStringPropertyEditor : DXPropertyEditor {
    public MyStringPropertyEditor(Type objectType, IModelMemberViewItem model)
        : base(objectType, model) { }
    protected override object CreateControlCore() {
        StringEdit control = new StringEdit();
        control.Properties.Appearance.ForeColor = Color.Coral;
        return control;
    }
    protected override RepositoryItem CreateRepositoryItem() {
        return new RepositoryItemStringEdit();
    }
    protected override void SetupRepositoryItem(RepositoryItem item) {
        base.SetupRepositoryItem(item);
        item.Appearance.ForeColor = Color.Coral;            
    }
}
```
***

The following image demonstrates a business object's property, displayed via the implemented Property Editor in a Detail View:

![DXPropertyEditor1](~/images/dxpropertyeditor1116098.png)

In a List View, the column which displays the business object property uses the Property Editor's Repository Item. So, in edit mode, the property is displayed in a List View using the same options as in the Detail View:

![DXPropertyEditor3](~/images/dxpropertyeditor3116100.png)

&nbsp;

Compared to the [](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor) class, the **DXPropertyEditor** class introduces additional members:

| Member | Description |
|---|---|
| @DevExpress.ExpressApp.Win.Editors.DXPropertyEditor.Control | Returns a `DevExpress.XtraEditors.BaseEdit` class descendant that represents the Property Editor's control. |
| @DevExpress.ExpressApp.Win.Editors.DXPropertyEditor.CustomSetupRepositoryItem | Occurs after the creation of a Property Editor's control. |
| @DevExpress.ExpressApp.Win.Editors.DXPropertyEditor.RepositoryItemsTypesWithMandatoryButtons | Used to determine the visibility state of the Property Editor control's buttons. |

When implementing a [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class descendant, the following protected members, which are not described in the documentation, can be overridden:

| Member | Description |
|---|---|
| `CreateRepositoryItem` | Used to support the [](xref:DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport) interface. This method is called when a column is created in an editable XtraGrid. The created repository item is assigned to the column's **ColumnEdit** property. This behavior allows the display of a business property in the same manner in a Detail and List View. |
| `SetRepositoryItemReadOnly` | Called in the **SetupRepositoryItem** and **OnAllowEditChanged** methods. Override this method to perform specific actions when the [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit) mode is changed. |
| `SetupRepositoryItem` | Called in the **OnControlCreated** method. Override this method to perform additional repository item initialization. |
| `OnCustomSetupRepositoryItem` | Called in the **SetupRepositoryItem** method. Raises the [DXPropertyEditor.CustomSetupRepositoryItem](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor.CustomSetupRepositoryItem) event. |

The **DXPropertyEditor** class implements the [](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat) interface, so that the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) can change the appearance format of a property to which a [conditional appearance rule](xref:113286) is applied.

To see an example of a [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class descendant implementation, refer to the [How to: Implement a Property Editor Using a DevExpress WinForms Control](xref:113015) topic.

> [!TIP]
> [!include[CanUpdateControlEnabled_Note](~/templates/canupdatecontrolenabled_note111203.md)]
