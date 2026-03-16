---
uid: DevExpress.ExpressApp.Editors.ListEditor.StartIncrementalSearch(System.String)
name: StartIncrementalSearch(String)
type: Method
summary: Starts an incremental search for the specified string.
syntax:
  content: public virtual void StartIncrementalSearch(string searchString)
  parameters:
  - id: searchString
    type: System.String
    description: The text to locate.
seealso: []
---
Generally, you do not need to call this method. It is automatically used by Lookup Property Editors to start the incremental search. Consider the following scenario. A Lookup Property Editor is selected but not activated:

![StartIncrementalSearch1](~/images/startincrementalsearch1116114.png)

Then an end-user presses the **B** key. The lookup dropdown is opened and the **B** character is passed to the Property Editor's **StartIncrementalSearch** method. 
If the number of the objects in the data source collection bound to the current Property Editor is bigger than the [IModelOptions.LookupSmallCollectionItemCount](xref:DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount) property value of the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelOptions) node,  the **B** character will be displayed in the search dialog:

![StartIncrementalSearch3](~/images/startincrementalsearch3116116.png)

Otherwise, the [List Editor](xref:113189)'s control will start the incremental search using the **B** character as the first one:

![StartIncrementalSearch2](~/images/startincrementalsearch2116115.png)

The search dialog can be enabled in a Lookup Property Editor regardless of the number of objects contained in the List View's collection source. See, [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925).