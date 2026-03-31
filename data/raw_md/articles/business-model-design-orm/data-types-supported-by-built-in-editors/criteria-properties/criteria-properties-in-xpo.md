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
***

See the [](xref:DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute) attribute description for details on using this attribute.