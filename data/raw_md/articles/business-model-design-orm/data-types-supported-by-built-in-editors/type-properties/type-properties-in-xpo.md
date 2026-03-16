---
uid: "113580"
seealso: []
title: Type Properties in XPO
owner: Ekaterina Kiseleva
---
# Type Properties in XPO

The following example illustrates how to implement [Type Properties](xref:113579) in an XPO persistent class.

```csharp
private string dataTypeName;
[Browsable(false)]
[Persistent("DataType")]
public string DataTypeName {
    get { return dataTypeName; }
    set {
        Type type = XafTypesInfo.Instance.FindTypeInfo(value) == null ? null : 
            XafTypesInfo.Instance.FindTypeInfo(value).Type;
        if (_dataType != type) {
            _dataType = type;
        }
        //if (!IsLoading && value != dataTypeName) {

        //}
        SetPropertyValue<string>(nameof(DataTypeName), ref dataTypeName, value);
    }
}

private Type _dataType;
[TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
[ImmediatePostData, NonPersistent]
public Type DataType {
    get { return _dataType; }
    set {
        if (_dataType != value) {
            _dataType = value;
            DataTypeName = (value == null) ? null : value.FullName;
        }
    }
}
```

> [!important]
> Do not use properties with [Value Converters](xref:2053) in [criteria expressions](xref:4928) executed on the database server side.
> 
> Value Converters change how the application saves and reads data in the database through special code in your application. However, the database does not recognize this special code. When a criterion is translated to a database query, a conversion implemented programmatically may not be applied or may be applied multiple times, leading to incorrect or unexpected results.