---
uid: DevExpress.ExpressApp.ObjectViewController
name: ObjectViewController
type: Class
summary: A base class for [View Controllers](xref:112621) intended for Object Views.
syntax:
  content: 'public class ObjectViewController : ViewController<ObjectView>'
seealso:
- linkId: DevExpress.ExpressApp.ObjectViewController._members
  altText: ObjectViewController Members
---
This Controller derives from the [](xref:DevExpress.ExpressApp.ViewController`1) class and sets the generic type parameter to [](xref:DevExpress.ExpressApp.ObjectView). The **ObjectViewController** Controller does not perform any operations. The only purpose of this Controller is to set the generic type parameter to **ObjectView**. You can use **ObjectViewController** as the base class for a custom Controller to ensure that the custom Controller is activated for List Views and Detail Views only.