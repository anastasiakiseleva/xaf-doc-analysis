---
uid: DevExpress.Persistent.Base.NotClonedInfoAttribute
name: NotClonedInfoAttribute
type: Class
summary: Applied to a business class. Specifies the business class' string property, which can hold the property values that were not cloned.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface)]
    public sealed class NotClonedInfoAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.NotClonedInfoAttribute._members
  altText: NotClonedInfoAttribute Members
---
This attribute is considered when cloning objects via the [Clone Object Module](xref:112835). The **NotClonedInfo** attribute's constructor takes a single string parameter. The parameter specifies the string property which can hold the property values that were not cloned.

When the actual type of the object being cloned differs from the target type, there may be properties which do not exist in the target type. You can apply the **NotClonedInfo** attribute to the target business class and specify a string property. In this instance, the values of the non-existent properties will be converted to the string representation, and stored to the specified property. Property values are separated by a semicolon.