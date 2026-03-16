---
uid: DevExpress.Persistent.Base.ObjectFormatter
name: ObjectFormatter
type: Class
summary: Represents a string formatter. Exposes the static helper [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method that replaces format items in the specified string with the property values of the specified object.
syntax:
  content: 'public class ObjectFormatter : ICustomFormatter, IFormatProvider'
seealso:
- linkId: DevExpress.Persistent.Base.ObjectFormatter._members
  altText: ObjectFormatter Members
- linkId: DevExpress.Persistent.Base.ObjectFormatter.Format*
- linkId: DevExpress.Persistent.Base.CustomFormatObjectEventArgs.EmptyEntriesMode
- linkId: "113173"
---
The **ObjectFormatter** is an auxiliary class that exposes the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method. This method can be used to create calculated properties in persistent classes. It takes an object and a string that contains format items. The method treats all the format items as the property names of the object. It replaces all the format items in the passed string with property values of the passed object.