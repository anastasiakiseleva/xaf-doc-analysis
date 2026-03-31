---
uid: "113015"
seealso:
- linkId: "113097"
title: 'Implement a Property Editor Using a DevExpress WinForms Control'
---
# Implement a Property Editor Using a DevExpress WinForms Control

This topic demonstrates how to implement a [Property Editor](xref:112612) with a custom mask. This Property Editor will use the [](xref:DevExpress.XtraEditors.CalcEdit) editor from the **XtraEditors** library. A currency mask will be set for this editor.

The image below shows the resulting Property Editor:

![CalcEditPropertyEditor](~/images/calceditpropertyeditor115924.png)

&nbsp;

Since we are going to use an editor from the **XtraEditors** library, our Property Editor should be inherited from the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class. This class supports the editor's capability to be used for inplace editing. It exposes extra methods for this. [!include[PublicEditor](~/templates/publiceditor111797.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Win.Editors;
//...
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {

}
```
***

When implementing a Property Editor, you should apply the **PropertyEditor** attribute to it. This attribute represents an indicator for the [Application Model](xref:112580) loader. The classes that use this attribute can be set to display properties of the type specified by the attribute's parameter.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Win.Editors;
//...
[PropertyEditor(typeof(decimal), true)]
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {

}
```
***

The Property Editor is now available within Property Editor types that can display decimal properties. To set a Property Editor to be automatically used for all properties of a specified data type, pass **true** as the second attribute parameter.

The **DXPropertyEditor** class sets the control's **EditValue** property as a binding property. However, the **CalcEdit** control converts the edit value to the Decimal type. The editor's decimal value can be accessed by the **Value** property, so you can set the **Value** property as a binding property.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Model;
//...
[PropertyEditor(typeof(decimal), true)]
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {
   public MyDecimalCalcEditPropertyEditor(Type objectType, IModelMemberViewItem model) 
      : base(objectType, model) {
      this.ControlBindingProperty = "Value";
   }
}
```
***

To specify the CalcEdit editor as a control to be used to display the Property Editor's property, override the **CreateControlCore** method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraEditors;
//...
[PropertyEditor(typeof(decimal), true)]
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {
   protected override object CreateControlCore() {
      return new CalcEdit();
   }
//...
}
```
***

To specify the required settings for the Property Editor, override the **SetupRepositoryItem** method (see [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor)). This method's _item_ parameter specifies the default repository item created for the CalcEdit editor (see [CalcEdit.Properties](xref:DevExpress.XtraEditors.CalcEdit.Properties)).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraEditors.Repository;
//...
[PropertyEditor(typeof(decimal), true)]
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {
   protected override void SetupRepositoryItem(RepositoryItem item) {
      base.SetupRepositoryItem(item);
         ((RepositoryItemCalcEdit)item).Mask.EditMask = "C";
         ((RepositoryItemCalcEdit)item).Mask.UseMaskAsDisplayFormat = true;
   }
   //...
}
```
***

In the code snippet above, the Currency mask is set for the editor. The same mask is used as the display format.

To use the Property Editor inplace (for example, in an editable [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor)), override the **CreateRepositoryItem** method and return the required repository item.

# [C#](#tab/tabid-csharp)

```csharp
[PropertyEditor(typeof(decimal), true)]
public class MyDecimalCalcEditPropertyEditor : DXPropertyEditor {
   protected override RepositoryItem CreateRepositoryItem() {
      return new RepositoryItemCalcEdit();
   }
   //...
}
```
***

> [!NOTE]
> Overriding the **CreateRepositoryItem** method is optional. This is only required if you are going to use the Property Editor in a cell of an editable List Editor. Note that a new [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) object is created to initialize the [GridColumn.ColumnEdit](xref:DevExpress.XtraGrid.Columns.GridColumn.ColumnEdit) property and then this object is immediately disposed. So, the custom PropertyEditor descendant is an incorrect place for event handlers. Instead, handle events or override corresponding _protected virtual_ methods in your [](xref:DevExpress.XtraEditors.Repository.RepositoryItem) class, introduce necessary properties and initialize them in the **CreateRepositoryItem** method of your Property Editor.

[!include[IComplexViewItem-note](~/templates/IComplexViewItem-note.md)]

To see the Property Editor in use, set it for a decimal property in the Model Editor invoked for the Windows Forms application project. To do this, use the **PropertyEditorType** property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** or [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node.
