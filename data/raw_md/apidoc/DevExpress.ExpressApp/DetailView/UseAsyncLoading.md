---
uid: DevExpress.ExpressApp.DetailView.UseAsyncLoading
name: UseAsyncLoading
type: Field
summary: Specifies whether the [IModelAsync.UseAsyncLoading](xref:DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading) property is visible in the Model Editor.
syntax:
  content: public static bool UseAsyncLoading
  return:
    type: System.Boolean
    description: '**true**, if the [IModelAsync.UseAsyncLoading](xref:DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading) property is visible in the Model Editor; otherwise, **false**.'
seealso: []
---
When [asynchronous data loading](xref:401747) is enabled, only the current object of a Detail View is loaded asynchronously, its associated collections are loaded in the main thread and this locks the UI. 

[!include[<UseAsyncLoading>](~/templates/solution_wizard_enables_property_in_new_projects.md)]

[!include[DetailView-UseAsyncLoading-notes](~/templates/DetailView-UseAsyncLoading-notes.md)]

Refer to the [Asynchronous Data Loading](xref:401747) topic for more information.
