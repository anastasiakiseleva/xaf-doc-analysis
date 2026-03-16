---
uid: DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute
name: XafDefaultPropertyAttribute
type: Class
summary: Applied to business classes. Specifies the default property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = true)]
    public class XafDefaultPropertyAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute._members
  altText: XafDefaultPropertyAttribute Members
---
This interface is a replacement for the [DefaultPropertyAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.defaultpropertyattribute) that can be applied both to classes and interfaces. Use this interface to specify the default property, as it is demonstrated in the [How to: Specify a Display Member (for a Lookup Editor, Detail Form Caption, etc.)](xref:113525) topic.

Default property values are displayed in the following:

* detail form captions;
* the leftmost columns of List Views;
* Lookup List Views;
* Lookup Editors in an unexpanded state.
