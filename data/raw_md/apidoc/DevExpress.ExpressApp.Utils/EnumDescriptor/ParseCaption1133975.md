---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.ParseCaption(System.String)
name: ParseCaption(String)
type: Method
summary: Returns the enumeration value corresponding to a particular display caption.
syntax:
  content: public object ParseCaption(string caption)
  parameters:
  - id: caption
    type: System.String
    description: A string representing the display caption which corresponds to a value of the enumeration represented by the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor).
  return:
    type: System.Object
    description: An object representing the enumeration value corresponding to the specified display caption.
seealso: []
---
Generally there's no need to use this method, unless you are implementing a [custom Property Editor](xref:113097) which displays captions of an enumeration, and allows selecting one of them. In this instance, you may need to call this method to determine the enumeration value a user selected.