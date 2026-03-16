---
uid: DevExpress.Persistent.Base.FileTypeFilterAttribute.GetExtensions
name: GetExtensions()
type: Method
summary: Returns the list of file extensions associated with the current file type filter.
syntax:
  content: public List<string> GetExtensions()
  return:
    type: System.Collections.Generic.List{System.String}
    description: A **List\<String>** object which specifies file extensions associated with the current file type filter.
seealso: []
---
By default, this method returns a list of strings, sorted using the [List\<T>.Sort](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.sort#System_Collections_Generic_List_1_Sort) method. To disable this and preserve the initial order of items, set the static **DevExpress.ExpressApp.FileAttachments.Win.FileTypeFiltersLogic.AllowSortExtensions** property to **false**. You can initialize this property before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called in the _Program.cs_ file.
