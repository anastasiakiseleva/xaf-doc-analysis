---
uid: DevExpress.ExpressApp.BaseObjectSpace.ConvertStringToSorting(System.String)
name: ConvertStringToSorting(String)
type: Method
summary: Converts the sorting string into the sorting list.
syntax:
  content: public static IList<SortProperty> ConvertStringToSorting(string sortingString)
  parameters:
  - id: sortingString
    type: System.String
    description: A string which contains the names of the columns against which data source contents are sorted.
  return:
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An **IList\<**[](xref:DevExpress.Xpo.SortProperty)**>** object that specifies sorting.
seealso: []
---
The format of the _sortingString_ string is described in the [XPServerCollectionSource.DefaultSorting](xref:DevExpress.Xpo.XPServerCollectionSource.DefaultSorting) topic.