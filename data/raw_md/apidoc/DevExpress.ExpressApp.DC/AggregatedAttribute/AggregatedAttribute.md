---
uid: DevExpress.ExpressApp.DC.AggregatedAttribute
name: AggregatedAttribute
type: Class
summary: Applied to business class properties. Indicates that a property or field references other aggregated persistent objects.
syntax:
  content: 'public class AggregatedAttribute : Attribute'
seealso:
- linkId: DevExpress.ExpressApp.DC.AggregatedAttribute._members
  altText: AggregatedAttribute Members
---
An aggregated object is a dependent object that is linked to its owner and cannot exist on its own. For example, `Address` and `PhoneNumber` business classes are usually not available in the navigation control and root `ListView` because they are created from the context of their parent object.

For Entity Framework Core and [non-persistent](xref:116516) objects, apply `DC.AggregatedAttribute` to [reference](xref:113572) or [collection](xref:113568) type properties. For example, you may have an aggregated `Address` reference type property and an aggregated collection of `PhoneNumber` objects. For more information on how to use the attribute, see [One-to-Many (Aggregated)](xref:402958#one-to-many-aggregated).

If your application uses XPO, apply [Xpo.AggregatedAttribute](xref:DevExpress.Xpo.AggregatedAttribute).