---
uid: DevExpress.ExpressApp.CollectionSourceBase.ObjectSpace
name: ObjectSpace
type: Property
summary: Provides access to the [Object Space](xref:113707) used by the Collection Source to interact with the database.
syntax:
  content: public IObjectSpace ObjectSpace { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space used by the Collection Source to interact with the database.
seealso: []
---
Generally, different List Views use different **ObjectSpaces**. However, nested List Views that represent non-aggregated collections share the same **ObjectSpace** with their root Detail Views.