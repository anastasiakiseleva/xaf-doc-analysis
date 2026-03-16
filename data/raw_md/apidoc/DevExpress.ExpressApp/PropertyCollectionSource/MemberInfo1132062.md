---
uid: DevExpress.ExpressApp.PropertyCollectionSource.MemberInfo
name: MemberInfo
type: Property
summary: Provides access to the **IMemberInfo** object that contains metadata information on the collection property represented by the [](xref:DevExpress.ExpressApp.PropertyCollectionSource).
syntax:
  content: public IMemberInfo MemberInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object that contains metadata information on the collection property represented by the **PropertyCollectionSource**.
seealso: []
---
Use the following members of the object returned by this property to get information on the collection property:

* The collection property's value: **GetValue** and **SetValue**
* Common information on the collection property:
    
    **MemberType**, **IsReadOnly**, **IsStructField**, **IsPersistent**, **IsKey**, **IsAggregated** and **Name**.