---
uid: DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.ForceInitialize
name: ForceInitialize()
type: Method
summary: Forces the initialization of the [metadata information](xref:113669) on XPO [business classes](xref:113664).
syntax:
  content: public static void ForceInitialize()
seealso: []
---
Since the **ForceInitialize** method is static, you can call in from any appropriate context.

# [C#](#tab/tabid-csharp)

```csharp
XpoTypesInfoHelper.ForceInitialize();
```
***

The [XpoTypesInfoHelper.GetXpoTypeInfoSource](xref:DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.GetXpoTypeInfoSource) calls the **ForceInitialize** method internally. So, there is no need to call **ForceInitialize** manually before using **GetXpoTypeInfoSource**.

Refer to the [How to: Use XAF Reports in a non-XAF Application](xref:114515) topic to see an example on how to use the **ForceInitialize** method.