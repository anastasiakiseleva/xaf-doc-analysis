---
uid: DevExpress.ExpressApp.Data.KeyAttribute
name: KeyAttribute
type: Class
summary: Applied to properties of [non-persistent classes](xref:116516). Specifies that a target property is a key property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
    public class KeyAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Data.KeyAttribute._members
  altText: KeyAttribute Members
---
A Key property is required if you are going to access a non-persistent object by a key using the [NonPersistentObjectSpace.ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event. An example of using this event together with the **KeyAttribute** attribute is provided in the [How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471) topic.