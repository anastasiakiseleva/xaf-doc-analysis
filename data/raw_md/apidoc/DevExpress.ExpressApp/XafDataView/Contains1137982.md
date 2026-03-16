---
uid: DevExpress.ExpressApp.XafDataView.Contains(System.Object)
name: Contains(Object)
type: Method
summary: Determines whether the [](xref:DevExpress.ExpressApp.XafDataView) contains a specific data record.
syntax:
  content: public bool Contains(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A [](xref:System.Object) which is a data record to locate in the data view.
  return:
    type: System.Boolean
    description: '**true**, if the record is found; otherwise, **false**.'
seealso: []
---
This method retrieves data from database and populates the data view's records list when this list is not yet initialized. Otherwise, the cached data record list is used. To remove the cache, use the [XafDataView.Reload](xref:DevExpress.ExpressApp.XafDataView.Reload) method.