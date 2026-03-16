---
uid: DevExpress.ExpressApp.DynamicCollectionBase.#ctor(DevExpress.ExpressApp.IObjectSpace,System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty},System.Boolean)
name: DynamicCollectionBase(IObjectSpace, Type, CriteriaOperator, IList<SortProperty>, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.DynamicCollectionBase class with specified settings.
syntax:
  content: public DynamicCollectionBase(IObjectSpace objectSpace, Type objectType, CriteriaOperator criteria, IList<SortProperty> sorting, bool inTransaction)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) for processing the collection objects.
  - id: objectType
    type: System.Type
    description: A type of objects in the collection.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The filter criteria. The collection contains only objects that match this criteria.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: A list of @DevExpress.Xpo.SortProperty objects that specify the sort order for the collection.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the specified *criteria* and *sorting* parameters are applied to all objects (in the database and retrieved); otherwise, **false**.'
seealso: []
---
