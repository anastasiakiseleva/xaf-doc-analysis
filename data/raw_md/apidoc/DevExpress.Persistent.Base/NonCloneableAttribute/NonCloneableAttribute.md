---
uid: DevExpress.Persistent.Base.NonCloneableAttribute
name: NonCloneableAttribute
type: Class
summary: Applied to a business class property. Specifies that the target property's value cannot be cloned when you use the [Clone Object Module](xref:112835) to clone objects.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field)]
    public sealed class NonCloneableAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.NonCloneableAttribute._members
  altText: NonCloneableAttribute Members
---
You can apply this attribute to a business class' field or property, to prohibit cloning of its value via the [Clone Object Module](xref:112835).