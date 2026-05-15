---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.CollectionSource
name: CollectionSource
type: Property
summary: Returns the Collection Source associated with the current `DxPivotGridListEditor`.
syntax:
  content: public CollectionSourceBase CollectionSource { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.CollectionSourceBase
    description: An object that provides access to the underlying collection of business objects displayed by the Pivot Grid List Editor.
seealso: []
---
A Collection Source retrieves a typed collection of objects from an `ObjectSpace`, stores them in the internal @DevExpress.ExpressApp.CollectionSourceBase.Collection, and supplies this collection to a List View. The Collection Source exposes methods for data access, filtering, sorting, and other operations applied to the underlying collection.