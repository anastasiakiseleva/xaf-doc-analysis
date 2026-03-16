---
uid: DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.GetXpoTypeInfoSource
name: GetXpoTypeInfoSource()
type: Method
summary: Returns an object providing access to the [](xref:DevExpress.Xpo.Metadata.XPDictionary).
syntax:
  content: public static XpoTypeInfoSource GetXpoTypeInfoSource()
  return:
    type: DevExpress.ExpressApp.DC.Xpo.XpoTypeInfoSource
    description: An **XpoTypeInfoSource** object providing access to the **XPDictionary**.
seealso: []
---
If the **XpoTypeInfoSource** object is not yet initialized, the **GetXpoTypeInfoSource** method forces its initialization by calling the [XpoTypesInfoHelper.ForceInitialize](xref:DevExpress.ExpressApp.Xpo.XpoTypesInfoHelper.ForceInitialize) method internally.

Since the **GetXpoTypeInfoSource** method is static, you can call in from any appropriate context.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Xpo;
using DevExpress.ExpressApp.DC.Xpo;
// ...
XpoTypeInfoSource xpoTypeInfoSource = XpoTypesInfoHelper.GetXpoTypeInfoSource();
```
***

You can access the [](xref:DevExpress.Xpo.Metadata.XPDictionary) object as follows:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Xpo.Metadata;
using DevExpress.ExpressApp.Xpo;
// ...
XPDictionary xpDictionary = XpoTypesInfoHelper.GetXpoTypeInfoSource().XPDictionary;
```
***

More examples on how to use the **GetXpoTypeInfoSource** method are provided in the following topics:

* [Access XAF Application Data in a non-XAF Application](xref:113709)
* [How to: Use XAF Reports in a non-XAF Application](xref:114515)
* [How to: Use the Integrated Mode of the Security System in Non-XAF Applications](xref:113558)
