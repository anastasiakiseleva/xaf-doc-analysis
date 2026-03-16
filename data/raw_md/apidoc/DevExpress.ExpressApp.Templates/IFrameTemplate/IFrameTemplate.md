---
uid: DevExpress.ExpressApp.Templates.IFrameTemplate
name: IFrameTemplate
type: Interface
summary: Declares members implemented by [Frame Templates](xref:112609).
syntax:
  content: public interface IFrameTemplate
seealso:
- linkId: DevExpress.ExpressApp.Templates.IFrameTemplate._members
  altText: IFrameTemplate Members
---
The **XAF** design is based on the [concept of abstract elements and actual controls](xref:112607). A [Frame (Window)](xref:112608) is an abstract entity. It can be displayed by any control. However, to support the relation with **XAF** elements, this contol must implement the **IFrameTemplate** interface.

The [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface has a descendant - [](xref:DevExpress.ExpressApp.Templates.IWindowTemplate), which declares members needed to display independent Windows.
