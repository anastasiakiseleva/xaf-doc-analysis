---
uid: DevExpress.ExpressApp.XafApplication.DefaultCollectionSourceMode
name: DefaultCollectionSourceMode
type: Property
summary: Specifies the default mode of operation for Collection Sources created by the [](xref:DevExpress.ExpressApp.XafApplication).
syntax:
  content: |-
    [DefaultValue(CollectionSourceMode.Proxy)]
    public CollectionSourceMode DefaultCollectionSourceMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.CollectionSourceMode
    description: A [](xref:DevExpress.ExpressApp.CollectionSourceMode) enumeration value specifying the default mode of operation for Collection Sources. By default, the [CollectionSourceMode.Proxy](xref:DevExpress.ExpressApp.CollectionSourceMode.Proxy) value is set.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.Mode
---
This property is used in the [XafApplication.CreateCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCollectionSource*) and [XafApplication.CreatePropertyCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreatePropertyCollectionSource*) methods. Note that it is overridden by the [CollectionSourceModeAttribute.Mode](xref:DevExpress.ExpressApp.CollectionSourceModeAttribute.Mode) parameter value of the [](xref:DevExpress.ExpressApp.CollectionSourceModeAttribute), if this attribute is applied to the collection property for whose List View a Collection Source is currently created.

For detailed information on Collection Sources, refer to the [](xref:DevExpress.ExpressApp.CollectionSourceBase) class description.