---
uid: DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.GetTypesInfo
name: GetTypesInfo()
type: Method
summary: Returns [metadata information](xref:113669) on types used in an XAF application.
syntax:
  content: public static ITypesInfo GetTypesInfo()
  return:
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object supplying metadata on types used in an XAF application.
seealso: []
---
Since the **GetTypesInfo** method is static, you can call in from any appropriate context. However, it is recommended to call the [XpoTypesInfoHelper.ForceInitialize](xref:DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.ForceInitialize) method before using **GetTypesInfo**, because the required metadata information may be not initialized yet.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Xpo;
// ...
XpoTypesInfoHelper.ForceInitialize();
ITypesInfo typesInfo = XpoTypesInfoHelper.GetTypesInfo();
```
***

Refer to the [How to: Use XAF Reports in a non-XAF Application](xref:114515) topic to see an example on how to use the **GetTypesInfo** method.