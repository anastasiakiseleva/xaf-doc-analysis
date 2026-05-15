---
uid: "113565"
seealso:
- linkId: "113143"
title: Criteria Properties in XPO
---
# Criteria Properties in XPO

The example below illustrates how to implement [Criteria Properties](xref:113564) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
private string dataTypeName;
[Browsable(false)]
public string DataTypeName {
    get { return dataTypeName; }
    set {
        Type type = XafTypesInfo.Instance.FindTypeInfo(value) == null ? null :
            XafTypesInfo.Instance.FindTypeInfo(value).Type;
        if(dataType != type) {
            dataType = type;
        }
        if(!IsLoading && value != dataTypeName) {
            Criteria = String.Empty;
            CriteriaInPopupWindow = String.Empty;
        }
        SetPropertyValue<string>(nameof(DataTypeName), ref dataTypeName, value);
    }
}

private Type dataType;
[TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
[ImmediatePostData, NonPersistent]
public Type DataType {
    get { return dataType; }
    set {
        if(dataType != value) {
            dataType = value;
            DataTypeName = (value == null) ? null : value.FullName;
        }
    }
}

private string criteria;
[CriteriaOptions("DataType")]
[Size(SizeAttribute.Unlimited)]
[ModelDefault("RowCount", "0")]
[VisibleInListView(true)]
[EditorAlias(EditorAliases.CriteriaPropertyEditor)]
public string Criteria {
    get { return criteria; }
    set { SetPropertyValue<string>(nameof(Criteria), ref criteria, value); }
}

private string criteriaInPopupWindow;
[CriteriaOptions("DataType")]
[Size(SizeAttribute.Unlimited)]
[ModelDefault("RowCount", "0")]
[VisibleInListView(true)]
[EditorAlias(EditorAliases.PopupCriteriaPropertyEditor)]
public string CriteriaInPopupWindow {
    get { return criteriaInPopupWindow; }
    set { SetPropertyValue<string>(nameof(CriteriaInPopupWindow), ref criteriaInPopupWindow, value); }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Private _dataTypeName As String
<Browsable(False)> _
Public Property DataTypeName() As String
    Get
        Return _dataTypeName
    End Get
    Set(ByVal value As String)
        Dim type As Type = If(XafTypesInfo.Instance.FindTypeInfo(value) Is Nothing, Nothing, _
        XafTypesInfo.Instance.FindTypeInfo(value).Type)
        If _dataType <> type Then
            _dataType = type
        End If
        If (Not IsLoading) AndAlso value <> _dataTypeName Then
            Criteria = String.Empty
            CriteriaInPopupWindow = String.Empty
        End If
        SetPropertyValue(Of String)(NameOf(DataTypeName), _dataTypeName, value)
    End Set
End Property

Private _dataType As Type
<TypeConverter(GetType(LocalizedClassInfoTypeConverter)), ImmediatePostData, NonPersistent> _
Public Property DataType() As Type
    Get
        Return _dataType
    End Get
    Set(ByVal value As Type)
        If _dataType <> value Then
            _dataType = value
            DataTypeName = If(value Is Nothing, Nothing, value.FullName)
        End If
    End Set
End Property

Private _criteria As String
<CriteriaOptions("DataType"), Size(SizeAttribute.Unlimited), _
ModelDefault("RowCount", "0"), VisibleInListView(True), EditorAlias(EditorAliases.CriteriaPropertyEditor)> _
Public Property Criteria() As String
    Get
        Return _criteria
    End Get
    Set(ByVal value As String)
        SetPropertyValue(Of String)(NameOf(Criteria), _criteria, value)
    End Set
End Property

Private _criteriaInPopupWindow As String
<CriteriaOptions("DataType"), Size(SizeAttribute.Unlimited), _
ModelDefault("RowCount", "0"), VisibleInListView(True), _
EditorAlias(EditorAliases.PopupCriteriaPropertyEditor)> _
Public Property CriteriaInPopupWindow() As String
    Get
        Return _criteriaInPopupWindow
    End Get
    Set(ByVal value As String)
        SetPropertyValue(Of String)(NameOf(CriteriaInPopupWindow), _criteriaInPopupWindow, value)
    End Set
End Property
```

***

See the [](xref:DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute) attribute description for details on using this attribute.