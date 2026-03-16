---
uid: DevExpress.ExpressApp.Validation.PersistenceValidationController.DeleteContextValidating
name: DeleteContextValidating
type: Event
summary: Occurs when an object that will be deleted is validated.
syntax:
  content: public event EventHandler<DeleteContextValidatingEventArgs> DeleteContextValidating
seealso: []
---
Handle this event to customize the list of objects to validate in the **Delete** context. The [DeleteContextValidatingEventArgs.DeletingObject](xref:DevExpress.ExpressApp.Validation.DeleteContextValidatingEventArgs.DeletingObject) parameter contains a null value if an object is already marked as deleted, or refers to an object that will be deleted. By default, the object that is deleted and all its aggregates are validated.