---
uid: DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchMode
name: FullTextSearchMode
type: Property
summary: Specifies the way in which the **FullTextSearch** [Actions](xref:112622) performs its search.
syntax:
  content: public SearchMode FullTextSearchMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Filtering.SearchMode
    description: A [](xref:DevExpress.ExpressApp.Filtering.SearchMode) enumeration value that specifies the way in which the **FullTextSearch** Action performs its search. The default value is [SearchMode.SearchInObject](xref:DevExpress.ExpressApp.Filtering.SearchMode.SearchInObject).
seealso: []
---
The `FullTextSearchMode` enumeration exposes the following values:

`SearchInObject`
:   Default value. **FullTextSearch** Action searches individual words from the word combination typed by a user in different properties included in the search scope.
`SearchInProperty`
:   **FullTextSearch** Action searches the word combination in each property included in the search scope.
