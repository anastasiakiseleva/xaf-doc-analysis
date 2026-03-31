---
uid: "113581"
seealso: []
title: Type Properties in EF Core
---
# Type Properties in EF Core

The example below illustrates how to implement [Type Properties](xref:113579) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel;
using System.ComponentModel.DataAnnotations.Schema;
using DevExpress.ExpressApp.Utils;
// ...
[NotMapped]
[TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
public Type DataType {
    get {
        Type result = null;
        if (!String.IsNullOrWhiteSpace(DataTypeName)) {
            ITypeInfo typeInfo = XafTypesInfo.Instance.FindTypeInfo(DataTypeName);
            if (typeInfo != null) {
                result = typeInfo.Type;
            }
        }
        return result;
    }
    set {
        if (value != null) {
            DataTypeName = value.FullName;
        }
        else {
            DataTypeName = "";
        }
    }
}
[Browsable(false)]
public virtual string DataTypeName { get; set; }
```

***