---
uid: DevExpress.ExpressApp.CollectionSourceModeAttribute
name: CollectionSourceModeAttribute
type: Class
summary: Specifies the mode of operation for the Collection Sources created by List Property Editors representing the **CollectionSourceModeAttribute**'s target property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true)]
    public class CollectionSourceModeAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceModeAttribute._members
  altText: CollectionSourceModeAttribute Members
- linkId: DevExpress.ExpressApp.CollectionSourceBase
---
By default, collection properties are displayed by the ListPropertyEditor. This Property Editor presents a List View in a grid. You can specify in which mode a Collection Source for this List View will be created. To do this, apply the **CollectionSourceMode** attribute to the target collection property and pass a boolean value. This value will be set to the Collection Source's [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property. There are two Collection Source modes: Normal and Proxy. In the Normal mode, the Collection Source's Object Space creates an XPCollection of objects of the specified type. In the Proxy mode, two collections are created: an original collection, as in the Normal mode, and an intermediate proxy collection. The proxy collection is the original collection's wrapper, initially required to support interfaces required for built-in XAF features. You can use the Proxy mode in the following scenario. If you filter the Collection Source's collection (e.g. using the [Criteria Property of a List View's Collection Source](xref:112988)), the [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) property will return a filtered collection. But in the Proxy mode, the filter is applied to the proxy collection. The original collection remains unfiltered and can be accessible. For details, refer to the [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) property description.

By default, the ListPropertyEditor creates a Collection Source in the Proxy mode. If you need to change this behavior with respect to a particular collection property, apply the **CollectionSourceMode** attribute to the property. If the source code of the property is not available, the attribute can be added in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
    base.CustomizeTypesInfo(typesInfo);
    XafTypesInfo.Instance.FindTypeInfo(typeof(Person)).FindMember("Phones").AddAttribute(
        new CollectionModeAttribute(CollectionSourceMode.Normal));
}
```
***

If you use a [Server](xref:118450) Mode for a nested List View, its Collection Source is created only in the Normal mode .
