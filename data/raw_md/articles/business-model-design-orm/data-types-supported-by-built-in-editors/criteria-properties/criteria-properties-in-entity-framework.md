---
uid: "113578"
title: Criteria Properties in EF Core
seealso:  
- linkId: "117395"
---
# Criteria Properties in EF Core

The example below illustrates how to implement [Criteria Properties](xref:113564) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
[Browsable(false)]
public virtual string DataTypeName {
    get { return fDataType == null ? string.Empty : fDataType.FullName; }
    set {
        ITypeInfo typeInfo = XafTypesInfo.Instance.FindTypeInfo(value);
        fDataType = typeInfo == null ? null : typeInfo.Type;
    }
}
private Type fDataType;
[NotMapped, ImmediatePostData]
public Type DataType {
    get { return fDataType; }
    set {
        if (fDataType == value) return;
        fDataType = value;
        Criteria = string.Empty;
        CriteriaInPopupWindow = string.Empty;
    }
}

[CriteriaOptions("DataType")]
[FieldSize(FieldSizeAttribute.Unlimited)]
[VisibleInListView(true)]
[EditorAlias(EditorAliases.CriteriaPropertyEditor)]
public virtual string Criteria { get; set; }

[CriteriaOptions("DataType")]
[FieldSize(FieldSizeAttribute.Unlimited)]
[VisibleInListView(true)]
[EditorAlias(EditorAliases.PopupCriteriaPropertyEditor)]
public virtual string CriteriaInPopupWindow { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***