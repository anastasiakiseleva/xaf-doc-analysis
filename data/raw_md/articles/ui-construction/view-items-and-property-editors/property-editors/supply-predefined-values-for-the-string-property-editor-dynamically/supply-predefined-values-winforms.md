---
uid: "113101"
seealso:
- linkId: "403100"
- linkId: "113097"
title: 'Supply Predefined Values for the String Property Editor Dynamically (WinForms)'
---
# Supply Predefined Values for the String Property Editor Dynamically (WinForms)

This topic describes implementation of a custom Property Editor for a Windows Forms application. A custom Property Editor used to edit a business object's **CultureCode** (locale) property of the **String** type is implemented here. The dropdown list of the Property Editor's control will display the cultures installed in an end-user's Windows operating system.

> [!NOTE]
> [!include[IModelCommonMemberViewItem.PredefinedValues Note](~/templates/imodelcommonmemberviewitem.predefinedvalues-note111397.md)]

The image below shows the resulting Property Editor:

![CustomPropertyEditor](~/images/custompropertyeditor116095.png)

By default, XAF creates the **StringPropertyEditor** for **String** type properties. This Property Editor displays a dropdown list of items if the corresponding **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's **RowCount** property is set to 0 and the **PredefinedValues** property contains a predefined list values for the dropdown. However, if you do not know the values before run time it is necessary to implement a custom Property Editor.

Since you are going to use a control supplied by DevExpress, implement a custom Property Editor by overriding the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class methods. You can inherit this class directly, or inherit one of its descendants (e.g., **StringPropertyEditor**). [!include[PublicEditor](~/templates/publiceditor111797.md)] So, the following methods must be overridden.

1. Override the **CreateControlCore** method to return the **ComboBoxEdit** control.
2. Override the **CreateRepositoryItem** method to return **RepositoryItemComboBox** type item, because it is the appropriate type for the **ComboBoxEdit** control.
3. Override the **SetupRepositoryItem** method to populate the control's dropdown list with items. We use the **CultureInfo.GetCultures** method to retrieve the cultures installed.

To specify that the implemented Property Editor can be used for the **String** type properties, the **PropertyEditor** attribute is applied:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Globalization;

using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.XtraEditors;
using DevExpress.XtraEditors.Controls;
using DevExpress.XtraEditors.Repository;
using DevExpress.ExpressApp.Model;
//...
[PropertyEditor(typeof(String), "CultureInfoPropertyEditor", false)]
public class CustomStringEditor : StringPropertyEditor {
    public CustomStringEditor(Type objectType, IModelMemberViewItem info)
        : base(objectType, info) {
    }
    protected override object CreateControlCore() {
        return new ComboBoxEdit();
    }
    protected override RepositoryItem CreateRepositoryItem() {
        return new RepositoryItemComboBox();
    }
    protected override void SetupRepositoryItem(
        DevExpress.XtraEditors.Repository.RepositoryItem item) {
        base.SetupRepositoryItem(item);
        foreach (CultureInfo culture in CultureInfo.GetCultures(
            CultureTypes.InstalledWin32Cultures)) {
            ((RepositoryItemComboBox)item).Items.Add(
                culture.EnglishName + "(" + culture.Name + ")");
        }
        ((RepositoryItemComboBox)item).TextEditStyle = TextEditStyles.DisableTextEditor;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System
Imports System.Globalization

Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Editors
Imports DevExpress.ExpressApp.Win.Editors
Imports DevExpress.XtraEditors
Imports DevExpress.XtraEditors.Controls
Imports DevExpress.XtraEditors.Repository
Imports DevExpress.ExpressApp.Model
'...
<PropertyEditor(GetType(String), "CultureInfoPropertyEditor", False)> _
Public Class CustomStringEditor
    Inherits StringPropertyEditor
    Public Sub New(ByVal objectType As Type, ByVal info As IModelMemberViewItem)
        MyBase.New(objectType, info)
    End Sub
    Protected Overrides Function CreateControlCore() As Object
        Return New ComboBoxEdit()
    End Function
    Protected Overrides Function CreateRepositoryItem() As RepositoryItem
        Return New RepositoryItemComboBox()
    End Function
    Protected Overrides Sub SetupRepositoryItem( _
    ByVal item As DevExpress.XtraEditors.Repository.RepositoryItem)
        MyBase.SetupRepositoryItem(item)
        For Each culture As CultureInfo In CultureInfo.GetCultures( _
        CultureTypes.InstalledWin32Cultures)
            CType(item, RepositoryItemComboBox).Items.Add( _
            culture.EnglishName & "(" & culture.Name & ")")
        Next culture
        CType(item, RepositoryItemComboBox).TextEditStyle = TextEditStyles.DisableTextEditor
    End Sub
End Class
```

***

Apply the [](xref:DevExpress.Persistent.Base.EditorAliasAttribute) attribute to use the implemented Property Editor for a business object's **CultureCode** property:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
//...
[EditorAlias("CultureInfoPropertyEditor")]
public String CultureCode {
   get { return GetPropertyValue<String>(nameof(CultureCode)); }
   set { SetPropertyValue(nameof(CultureCode), value); }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.Model
'...
<EditorAlias("CultureInfoPropertyEditor")> _
Public Property CultureCode() As String
   Get
      Return GetPropertyValue(Of String)(NameOf(CultureCode))
   End Get
   Set(ByVal value As String)
      SetPropertyValue(NameOf(CultureCode), value)
   End Set
End Property
```

***

Here, the **EditorAlias** attribute changes the **PropertyEditorType** property of the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelMember) node, that defines the **CultureCode** property. Alternatively, you can do it via the [Model Editor](xref:112582).

[!include[IComplexViewItem-note](~/templates/IComplexViewItem-note.md)]

> [!NOTE]
> You can see the code demonstrated here along with more examples on custom property editors in the Feature Center Demo installed with **XAF**.
