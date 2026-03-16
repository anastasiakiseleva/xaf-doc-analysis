---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.Captions
name: Captions
type: Property
summary: Specifies the display captions associated with the values of the enumeration represented by the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor).
syntax:
  content: public ICollection<string> Captions { get; }
  parameters: []
  return:
    type: System.Collections.Generic.ICollection{System.String}
    description: An **ICollection\<String>** object representing the display captions associated with the values of the enumeration represented by the **EnumDescriptor**.
seealso: []
---
Generally there's no need to use this method, unless you are implementing a [custom Property Editor](xref:113097) that displays captions of an enumeration. In this instance, you may use this property as the data source of the display captions.