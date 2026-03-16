---
uid: DevExpress.ExpressApp.FetchObjectsEventArgs.#ctor(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty},System.Int32,System.Boolean)
name: FetchObjectsEventArgs(Type, CriteriaOperator, IList<SortProperty>, Int32, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.FetchObjectsEventArgs class with specified settings.
syntax:
  content: public FetchObjectsEventArgs(Type objectType, CriteriaOperator criteria, IList<SortProperty> sorting, int topReturnedObjects, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A type of objects in the collection.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The filter criteria to be applied to the collection.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: A list of @DevExpress.Xpo.SortProperty objects that specify the sort order for the collection.
  - id: topReturnedObjects
    type: System.Int32
    description: The maximum number of objects that can be retrieved from the collection.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the specified *criteria* and *sorting* parameters are applied to all objects (in the database and retrieved); otherwise, **false**.'
seealso: []
---
