---
uid: DevExpress.ExpressApp.BaseObjectSpace.ConvertSortingToString(System.Collections.Generic.IList{DevExpress.Xpo.SortProperty})
name: ConvertSortingToString(IList<SortProperty>)
type: Method
summary: Returns the string representation of a given sort list.
syntax:
  content: public static string ConvertSortingToString(IList<SortProperty> sorting)
  parameters:
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An **IList\<**[](xref:DevExpress.Xpo.SortProperty)**>** object that specifies sorting to be converted.
  return:
    type: System.String
    description: A string which contains the names of the columns against which data source contents are sorted.
seealso: []
---
The format of the returned string is compatible with the [XPServerCollectionSource.DefaultSorting](xref:DevExpress.Xpo.XPServerCollectionSource.DefaultSorting) property.